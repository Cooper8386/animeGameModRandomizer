import os
import random
import json


# Define the path to the main directory containing the subfolders
main_directory = "G:\\3DMigoto\\Mods\\character"

# Load the subfolders from the JSON file
with open('subfolders.json') as f:
    subfolders = json.load(f)

# Load the excluded mods from the JSON file
with open('exclude.json') as f:
    excluded_mods = json.load(f)

# Iterate through each subfolder
for subfolder in subfolders:
    # Define the path to the subfolder
    subfolder_path = os.path.join(main_directory, subfolder)

    # Get a list of all the mod folders in the subfolder
    mod_folders = [folder for folder in os.listdir(subfolder_path) if os.path.isdir(os.path.join(subfolder_path, folder))]

    # Iterate through each mod folder
    for mod_folder in mod_folders:
        # Check if the mod folder is excluded
        if mod_folder in excluded_mods:
            # If the mod folder is excluded, skip it
            print(f"Mod folder {mod_folder} is excluded, skipping.")
            continue

        # Check if the mod folder is already disabled
        if mod_folder.startswith("DISABLED_"):
            # If the mod folder is already disabled, do nothing
            print(f"Mod folder {mod_folder} is already disabled.")
        else:
            # If the mod folder is not disabled, disable it by adding the "DISABLED_" prefix
            new_name = "DISABLED_" + mod_folder
            os.rename(os.path.join(subfolder_path, mod_folder), os.path.join(subfolder_path, new_name))
            print(f"Mod folder {mod_folder} has been disabled.")