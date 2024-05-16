# filename: __init__.py

'''
# -------------------------------------------------------------------------- #

# File Name:        __init__.py
# Version:          0.0.4
# Language:         python script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL: LOGIK-PROJEKT
# Created:          2024-04-20
# Modified:         2024-05-09
# Modifier:         Phil MAN - phil_man@mac.com

# Description:      This program is part of a library of custom functions
#                   and modules for autodesk flame.

# Installation:     Copy the 'LOGIK-PROJEKT' repo to your GitHub directory,
#                   e.g. '/home/$USER/workspace/GitHub'

# Attribution:      This script is derived from work originally authored by
#                   Michael Vaglienty: 'pyflame_lib_script_template.py'

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #
'''

# # Import classes or functions to expose them at the package level

# from classes_and_functions.functions.pyflame_script_01 import (
#     SomeClass as PyFlameSomeClass1
# )
# from classes_and_functions.functions.pyflame_script_02 import (
#     SomeClass as PyFlameSomeClass2
# )

# from classes_and_functions.classes.qt_ui_class_01 import (
#     SomeClass as QtUISomeClass1
# )
# from classes_and_functions.classes.qt_ui_class_02 import (
#     SomeClass as QtUISomeClass2
# )

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section imports the pyflame functions.
# ========================================================================== #

# from classes_and_functions.functions.pyflame_get_shot_name import (
#     pyflame_get_shot_name as pyflame_get_shot_name
# )
# from classes_and_functions.functions.pyflame_print import (
#     pyflame_print as pyflame_print
# )
# from classes_and_functions.functions.pyflame_get_flame_version import (
#     pyflame_get_flame_version as pyflame_get_flame_version
# )
# from classes_and_functions.functions.pyflame_file_browser import (
#     pyflame_file_browser as pyflame_file_browser
# )
# from classes_and_functions.functions.pyflame_resolve_shot_name import (
#     pyflame_resolve_shot_name as pyflame_resolve_shot_name
# )
# from classes_and_functions.functions.pyflame_resolve_path_tokens import (
#     pyflame_resolve_path_tokens as pyflame_resolve_path_tokens
# )
# from classes_and_functions.functions.pyflame_refresh_hooks import (
#     pyflame_refresh_hooks as pyflame_refresh_hooks
# )
# from classes_and_functions.functions.pyflame_open_in_finder import (
#     pyflame_open_in_finder as pyflame_open_in_finder
# )
# from classes_and_functions.functions.pyflame_load_config import (
#     pyflame_load_config as pyflame_load_config
# )
# from classes_and_functions.functions.pyflame_save_config import (
#     pyflame_save_config as pyflame_save_config
# )

# ========================================================================== #
# This section imports the Qt UI classes.
# ========================================================================== #

# from classes_and_functions.classes.FlameButton import (
#     FlameButton as FlameButton
# )
# from classes_and_functions.classes.FlameClickableLineEdit import (
#     FlameClickableLineEdit as FlameClickableLineEdit
# )
# from classes_and_functions.classes.FlameLabel import (
#     FlameLabel as FlameLabel
# )
# from classes_and_functions.classes.FlameLineEdit import (
#     FlameLineEdit as FlameLineEdit
# )
# from classes_and_functions.classes.FlameListWidget import (
#     FlameListWidget as FlameListWidget
# )
# from classes_and_functions.classes.FlameMessageWindow import (
#     FlameMessageWindow as FlameMessageWindow
# )
# from classes_and_functions.classes.FlamePasswordWindow import (
#     FlamePasswordWindow as FlamePasswordWindow
# )
# from classes_and_functions.classes.FlamePresetWindow import (
#     FlamePresetWindow as FlamePresetWindow
# )
# from classes_and_functions.classes.FlameProgressWindow import (
#     FlameProgressWindow as FlameProgressWindow
# )
# from classes_and_functions.classes.FlamePushButton import (
#     FlamePushButton as FlamePushButton
# )
# from classes_and_functions.classes.FlamePushButtonMenu import (
#     FlamePushButtonMenu as FlamePushButtonMenu
# )
# from classes_and_functions.classes.FlameQDialog import (
#     FlameQDialog as FlameQDialog
# )
# from classes_and_functions.classes.FlameSlider import (
#     FlameSlider as FlameSlider
# )
# from classes_and_functions.classes.FlameTextEdit import (
#     FlameTextEdit as FlameTextEdit
# )
# from classes_and_functions.classes.FlameTokenPushButton import (
#     FlameTokenPushButton as FlameTokenPushButton
# )
# from classes_and_functions.classes.FlameTreeWidget import (
#     FlameTreeWidget as FlameTreeWidget
# )
# from classes_and_functions.classes.FlameWindow import (
#     FlameWindow as FlameWindow
# )

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Changelist:
# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-07 - 21:48:20
# comments:              Refactored monolithic code to discreet modules
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-07 - 21:49:31
# comments:              Added docstrings
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-07 - 21:50:00
# comments:              Prep for initial production test
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-09 - 13:18:47
# comments:              Refactored code works in flame 2025. Time to tidy up.