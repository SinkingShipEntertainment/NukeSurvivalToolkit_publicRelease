name = 'NukeSurvivalToolkit'

version = '2.1.1.sse.1.1.0'

authors = [
    'CreativeLyons',
]

description = '''Nuke plugins'''

with scope('config') as c:
    # Determine location to release: internal (int) vs external (ext)
    # NOTE: Modify this variable to reflect the current package situation
    release_as = 'ext'

    # The 'c' variable here is actually rezconfig.py
    # 'release_packages_path' is a variable defined inside rezconfig.py

    import os
    if release_as == 'int':
        c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_INT']
    elif release_as == 'ext':
        c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_EXT']

requires = [
    "nuke",
]

private_build_requires = [
]

variants = [
    #['platform-linux', 'arch-x86_64', 'os-centos-7'],
]


build_command = 'rez python {root}/rez_build.py'
uuid = 'repository.NukeSurvivalToolkit_publicRelease'


def pre_commands():
    pass

def commands():

    # NOTE: REZ package versions can have ".sse." to separate the external
    # version from the internal modification version.
    split_versions = str(version).split(".sse.")
    external_version = split_versions[0]
    internal_version = None
    if len(split_versions) == 2:
        internal_version = split_versions[1]

    env.NUKESURVIVALTOOLKIT_VERSION = external_version
    env.NUKESURVIVALTOOLKIT_PACKAGE_VERSION = external_version
    if internal_version:
        env.NUKESURVIVALTOOLKIT_PACKAGE_VERSION = internal_version

    env.NUKESURVIVALTOOLKIT_ROOT.append("{root}")
    env.NUKESURVIVALTOOLKIT_LOCATION.append("{root}")
    env.REZ_NUKESURVIVALTOOLKIT_ROOT = '{root}'

    env.NUKE_PATH.append('{root}/NukeSurvivalToolkit')  # so Nuke can find it

def post_commands():
    pass
