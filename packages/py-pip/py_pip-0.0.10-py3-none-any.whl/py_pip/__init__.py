import sys
import subprocess
import pkgutil
import os
import pkg_resources  # todo replace deprecated module
import importlib
import logging
from pathlib import Path


default_target_path = ""
python_interpreter = sys.executable  # can be changed externally, e.g. in Maya

_cached_installed_packages = []


def _prep_env() -> dict:
    """Add custom python paths to the environment, to support dynamically added paths """
    my_env = os.environ.copy()

    # avoid paths not in sys.path passed to pip,
    # e.g. paths set in PYTHONPATH, are ignored in apps like Blender. So shouldn't be passed to pip
    my_env["PYTHONPATH"] = os.pathsep.join(sys.path)

    # clear paths, to avoid passing external python modules to pip
    for key in ["PATH", "PYTHONHOME", "PYTHONUSERBASE"]:
        if key in my_env:
            del my_env[key]
    
    # add git path back
    str_paths = os.environ.get("PATH", "")
    paths = str_paths.split(os.pathsep)
    git_paths = [p for p in paths if "git" in p.lower()]  # todo make less HACKY, since we just check if git is in the path
    if git_paths:
        my_env["PATH"] = os.pathsep.join(git_paths)
    else:
        logging.warning("py_pip couldn't detect git in PATH, ensure a folder in PATH contains the name 'git'")

    # prevent pip from using the user site
    my_env["PYTHONNOUSERSITE"] = "1"

    return my_env


def run_command_process(command) -> subprocess.Popen:
    """returns the subprocess, use to capture the output of the command while running"""
    my_env = _prep_env()
    print(F"run_command_process command: {command}")
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=my_env)


def run_command(command) -> (str, str):
    """
    Run command and return output and error
    Returns (stdOut, stdErr) output and error are bytes, use .decode() to convert to string
    """
    process = run_command_process(command)
    output, error = process.communicate()
    return output, error


def list():
    """return tuple of (name, version) for each installed package"""
    output, error = run_command([python_interpreter, "-m", "pip", "list"])

    # Parse the output of the pip list command
    packages = []
    raw = output.decode()
    
    for line in raw.split("\n")[2:-1]:  # 2-1 skips the first lines
        split_text = line.split()  # assumes version and package name dont contain spaces
        if split_text:
            name, version = split_text[:2]  # TODO edit packages contain a 3rd value: path 
            packages.append((name, version))

    global __cached_installed_packages
    __cached_installed_packages = packages
    return packages


def get_version(package_name, cached=False) -> str:
    """
    Return installed package version or empty string
    use_cached: requires running list before use. speed up get_version since pip list is slow
    """
    if cached:
        global __cached_installed_packages
        packages = __cached_installed_packages
    else:
        packages = list()
    for name, version in packages:
        if name == package_name:
            return version
    return ""
    

def get_location(package_name: str) -> "str|None":

    # todo cleanup
    def find_package_location(name: str) -> "str|None":
        try:
            distribution = pkg_resources.get_distribution(name)
            return distribution.location
        except pkg_resources.DistributionNotFound:
            logging.warning(f"Package '{name}' not found.")
            return None

    try:
        loader = pkgutil.get_loader(package_name)
        if loader is not None:
            package_location = os.path.dirname(loader.get_filename())
            return package_location
        else:
            return find_package_location(package_name)
    except ImportError as e:
        logging.error(f"Error while trying to locate package '{package_name}'. Error: {e}")
        return None


def install_process(package_name: "str|List[str]"=None,
                    target_path: "str|pathlib.Path"=None,
                    force=False,
                    upgrade=False,
                    requirements=None,
                    options=None,
                    ):
    """
    target_path: path where to install module too, if default_target_path is set, use that
    to fix possible import issues, invalidate caches after installation with 'importlib.invalidate_caches()'
    """
    command = [python_interpreter, "-m", "pip", "install"]
    if package_name:
        command.append(package_name)
    if requirements:
        command.extend(["-r", str(requirements)])
    if force:
        command.append("--force-reinstall")
    if upgrade:
        command.append("--upgrade")
    target_path = target_path or default_target_path
    if target_path:
        command.extend(["--target", str(target_path), "--no-user"])
    if options:
        command.extend(options)
    return run_command_process(command)


def _print_error(error, package_name=None):
    if error:
        if package_name:  # can be none if we e.g. install from requirements, so there's no package
            msg = f"There was an install error for package '{package_name}'"
        else:
            msg = "There was an install error"
        logging.error(msg)

        try:
            txt = error.decode()
            for line in txt.splitlines():
                logging.error(line)
        except Exception as e:
            logging.error("failed to decode subprocess error", e)
            logging.error(error)


def install(package_name: "str|List[str]"=None,
            invalidate_caches: bool = True,
            target_path: "str|pathlib.Path"=None,
            force=False,
            upgrade=False,
            requirements: "str|pathlib.Path"=None,
            options=None,  # list[str] extra options to pass to pip install, e.g. ["--editable"]
            ):
    """
    pip install a python package
    package_name: name of package to install (extra args can be passed in the package_name kwarg)
    invalidate_caches: if True, invalidate importlib caches after installation
    target_path: path where to install module too, if default_target_path is set, use that
    """
    process = install_process(package_name=package_name, target_path=target_path, force=force, upgrade=upgrade, requirements=requirements, options=options)
    output, error = process.communicate()
    _print_error(error, package_name=package_name)

    # exception on fail, TODO test if this doesn't trigger warnings, e.g. a pip version is outdated warning
    return_code = process.returncode
    if return_code != 0:
        # Treat non-zero return code as a package installation failure
        raise RuntimeError(f"Package installation failed with return code {return_code}: {error}")
        
    # TODO if editable install, we add a pth file to target path.
    # but target path might not be in site_packages, and pth might not be processed.
    # if target_path:
    #     import site
    #     site.addsitedir(pth_path)
    #     site.removeduppaths()

    if invalidate_caches:
        importlib.invalidate_caches()
    return output, error    


def get_package_modules(package_name):
    # Get a list of modules that belong to the specified package
    package_modules = []
    package_loader = pkgutil.get_loader(package_name)
    file_name = package_loader.get_filename()  # e.g. "C:\Users\hanne\AppData\Roaming\Blender Foundation\Blender\3.2\scripts\addons\modules\plugget\__init__.py"
    if not Path(file_name).is_dir():  # todo test with a .py file instead of package
        file_name = str(Path(file_name).parent)  # # e.g. "C:\Users\hanne\AppData\Roaming\Blender Foundation\Blender\3.2\scripts\addons\modules\plugget"

    if package_loader is not None:
        for _, module_name, _ in pkgutil.walk_packages([file_name]):
            full_module_name = f"{package_name}.{module_name}"
            package_modules.append(full_module_name)

    return package_modules


def unimport_modules(package_name):
    """unload any package's imported modules from memory"""
    for module_name in get_package_modules(package_name):
        if module_name in sys.modules:
            logging.debug(f"deleting module {module_name}")
            del sys.modules[module_name]


def uninstall(package_name=None, unimport=True, yes=True, requirements=None):  # dependencies=False
    """
    custom kwargs
    delete_module: if True, delete the module from sys.modules, it's the opposite of importing the module

    pip kwargs
    yes: if True, Don’t ask for confirmation of uninstall deletions
    """
    # todo uninstall dependencies

    command = [python_interpreter, "-m", "pip", "uninstall"]
    if package_name:
        command.append(package_name)
    if yes:
        command.append("-y")
    if requirements:
        command.extend(["-r", str(requirements)])
    output, error = run_command(command)

    # todo add unimport support if we uninstall from requirements
    try:
        if unimport: 
            unimport_modules(package_name)
    except Exception as e:
        logging.warning(f"unimport failed: {e}")

    return output, error
