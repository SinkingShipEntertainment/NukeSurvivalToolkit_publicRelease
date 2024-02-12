""" Nuke Survival Toolkit
    https://github.com/CreativeLyons/NukeSurvivalToolkit_publicRelease/tree/master


    When Updating NukeSurvivalToolkit for Sinking Ship Entertainment:
    ----------------------------------------------------------------
    1) Update the init.py and menu.py for compatibility with SSE pipeline
       - make sure all the sub-folders are visible to the farm (add them to the nuke plugin path)
       - we have to add them ALL because some of the tools contain scripts
         that expect to be able to find things in those folders.

    2) Make sure you go through EVERY tool to ensure it is python 3 and linux compatible
       - almost all most issues are with print statements in expressions
       - a few issues are due to very old tools that no longer work in newer versions of nuke
       - for now, we just leave the complete NST toolset in place, but we may want to
         vet these tools more carefully.

"""

import os
import nuke

# Add nuke plugin paths
NST_FolderPath = os.path.dirname(__file__).replace('\\', '/')

nuke.pluginAddPath('{0}/gizmos'.format(NST_FolderPath))
nuke.pluginAddPath('{0}/python'.format(NST_FolderPath))
nuke.pluginAddPath('{0}/icons'.format(NST_FolderPath))
nuke.pluginAddPath('{0}/images'.format(NST_FolderPath))
nuke.pluginAddPath('{0}/nk_files'.format(NST_FolderPath))
