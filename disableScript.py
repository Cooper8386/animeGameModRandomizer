import os
import random
import json

# Directory path
directory = "G:\\3DMigoto\\Mods\\character"

# Read subfolders from JSON file
with open("subfolders.json", "r") as file:
    subfolders = json.load(file)

# Read excluded mods from JSON file
with open("excluded_mods.json", "r") as file:
    excluded_mods = json.load(file)

# Function to disable a mod by adding the "DISABLED_" prefix
def disable_mod(mod_path):
    mod_name = os.path.basename(mod_path)
    if not mod_name.startswith("DISABLED_") and mod_name not in excluded_mods:
        new_mod_name = "DISABLED_" + mod_name
        new_mod_path = os.path.join(os.path.dirname(mod_path), new_mod_name)
        os.rename(mod_path, new_mod_path)
        return f"Disabled mod: {mod_name}"
    elif mod_name in excluded_mods:
        return f"Skipped excluded mod: {mod_name}"

# Function to enable a mod by removing the "DISABLED_" prefix
def enable_mod(mod_path):
    mod_name = os.path.basename(mod_path)
    if mod_name.startswith("DISABLED_") and mod_name[9:] not in excluded_mods:
        new_mod_name = mod_name[9:]
        new_mod_path = os.path.join(os.path.dirname(mod_path), new_mod_name)
        os.rename(mod_path, new_mod_path)
        return f"Enabled mod: {new_mod_name}"
    elif mod_name[9:] in excluded_mods:
        return f"Skipped excluded mod: {mod_name}"

# Iterate over each subfolder
for subfolder in subfolders:
    subfolder_path = os.path.join(directory, subfolder)
    print(f"Subfolder: {subfolder}")
    
    # Get a list of mod folders in the subfolder
    mod_folders = [folder for folder in os.listdir(subfolder_path) if os.path.isdir(os.path.join(subfolder_path, folder))]
    
    # Disable all mods in the subfolder except excluded mods
    disabled_mods = []
    for mod_folder in mod_folders:
        mod_path = os.path.join(subfolder_path, mod_folder)
        result = disable_mod(mod_path)
        if result:
            disabled_mods.append(result)
    
    # Get a list of enabled mods (excluding excluded mods)
    enabled_mods = [folder for folder in mod_folders if not folder.startswith("DISABLED_") and folder not in excluded_mods]
    
    # Randomly enable one mod in the subfolder (if there are any enabled mods left)
    if enabled_mods:
        random_mod = random.choice(enabled_mods)
        mod_path = os.path.join(subfolder_path, random_mod)
        result = enable_mod(mod_path)
        if result:
            disabled_mods.append(result)
    
    # Print the changes made in the subfolder
    if disabled_mods:
        print("\n".join(disabled_mods))
    else:
        print("No changes made in this subfolder.")
    print()
