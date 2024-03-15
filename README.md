a simple Anime Game Mod Randomizer

This Python script is designed to manage a set of folders and subfolders for Anime Game mods by enabling and disabling them randomly. The script ensures that a new random mod is selected every time it is run.
Prerequisites

    Python 3.x installed on your system
    Anime Game mods organized in the following directory structure:

    G:\3DMigoto\Mods\character
    ├── character1
    ├── character2
    ├── character3
    ...
    └── character99

Setup

    Create a file named subfolders.txt in the same directory as the script. This file should contain the list of subfolders (character names) that the script will manage. Each subfolder should be on a separate line.
    Create a file named excluded_mods.txt in the same directory as the script. This file should contain the list of mods that you do not want the script to modify. Each excluded mod should be on a separate line.
    Create a file named suffixes.txt in the same directory as the script. This file should contain the dictionary of suffixes for different types of mods for each character. Each entry should be in the format character: "suffix1", "suffix2", with each entry on a separate line.

Usage

    Run the script using the command:

    python mod_manager.py

    The script will perform the following actions:
        Disable all currently enabled mods within each subfolder by adding the "DISABLED_" prefix to the mod folder name.
        Randomly choose a currently disabled mod in each subfolder and enable it by removing the "DISABLED_" prefix from the mod folder name.
        For characters with defined suffixes, create separate sections to run through the random enabling of mods for each suffix.
        Print out the mods that were enabled and disabled during the script execution.
    The script will handle the following scenarios:
        If a mod folder is already disabled (has the "DISABLED_" prefix), it will not be disabled again.
        If a randomly chosen mod is in the excluded_mods.txt file, the script will choose another mod that is not excluded.
        If the script encounters a permission error or access denied exception, it will handle it gracefully.
        The script will prevent enabling a mod that was just disabled.

Configuration

    subfolders.txt: Add or remove subfolders (character names) to manage different sets of mods.
    excluded_mods.txt: Add or remove mods that you want to exclude from the random enabling/disabling process.
    suffixes.txt: Modify the dictionary of suffixes for each character to define different types of mods.

Notes

    The script assumes that the mod folders are located in the directory G:\3DMigoto\Mods\character. If your mods are located in a different directory, update the main_directory variable in the script accordingly.
    The script uses the os module to interact with the file system and the random module to perform random selections.
    The script prints out informative messages to indicate which mods were enabled or disabled during each run.

Feel free to customize and extend the script based on your specific requirements for managing Anime Game mods.
