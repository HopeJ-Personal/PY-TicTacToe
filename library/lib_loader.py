import importlib.util
import json
import sys
import os

__all__ = []  # Will hold the names of exported symbols

imported_modules = {}  # This will hold module references
loaded_symbols = {}    # This will hold all callable functions/classes

def accessiblefiles(path):
    hiddenfile = ["karel.jpg","stock_karel.jpg","labs","rightArrow.gif","leftArrow.gif"]
    fileextensions = [".py",".txt"]
    contents = os.listdir(path)
    files = []
    try:
        for item in contents:
            if item[0] != "." and item not in hiddenfile:
                files.append(item)
    except OSError as e:
        print(f"error accessing the directory: {e}")
    return files

def accessiblefolders(path):
    contents = accessiblefiles(path)
    files = []
    folders = []
    for x in contents:
        if any(ext in x for ext in [".py", ".txt"]):
            files.append(x)
        else:
            if x not in files and x not in folders:
                folders.append(x)
    return folders

def libraryhandler():
    global loaded_symbols, __all__

    path = os.getcwd()
    indexs = []
    manifests = []
    uuids_present = []
    uuids_dependencies = []
    imported_modules.clear()
    loaded_symbols.clear()

    if "library" in accessiblefiles(os.getcwd()):
        libcon = accessiblefolders("library")
        print("[lib-loader.py]: A library folder was detected")
        print(f"[lib-loader.py]: Attempting to load {len(libcon)} libraries in this project")

        for x in libcon:
            for y in accessiblefiles(os.path.join(path, "library", x)):
                tpath = os.path.join(path, "library", x, y)
                if y == "index.py":
                    indexs.append(tpath)
                if y == "manifest.json":
                    manifests.append(tpath)

        # Dependency checking
        for x in manifests:
            with open(x, 'r') as f:
                contents = json.load(f)
                uuids_present.append(contents["uuid"])
                contents_dependencies = contents.get('Dependencies', {})
                for dep in contents_dependencies.values():
                    uuids_dependencies.append(dep.get('UUID'))
        
        uuids_dependencies = list(set(uuids_dependencies))
        print(f"[dep check]: {uuids_present}")
        print(f"[dep check]: {uuids_dependencies}")
        
        uuids_dependencies = list(set(uuids_dependencies))
        for x in uuids_dependencies:
            if x not in uuids_present:
                print(f"{x} is a missing dependency")

        # Library Functionality Importing
        for file_path in indexs:
            module_name = os.path.splitext(os.path.basename(file_path))[0] + "_" + str(len(imported_modules))

            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                if spec is None:
                    print(f"Warning: Could not create module spec for {file_path}")
                    continue

                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                imported_modules[module_name] = module

                # Pull out all functions/classes
                for name, obj in vars(module).items():
                    if not name.startswith('__'):
                        if callable(obj):  # function or class
                            loaded_symbols[name] = obj
                            globals()[name] = obj
                            __all__.append(name)

            except Exception as e:
                print(f"Error importing module from {file_path}: {e}")