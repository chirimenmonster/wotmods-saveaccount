import os
import shutil
import py_compile
import zipfile
import urllib
import ConfigParser
from string import Template

SCRIPT_NAME = 'mod_saveaccount.py'

ALT_SCRIPT_NAME = 'mod_preferredserver.py'
ALT_SCRIPT_LOCATION = 'https://raw.githubusercontent.com/chirimenmonster/wotmods-preferredserver/v0.3/mods/'
ALT_SCRIPT_URL = ALT_SCRIPT_LOCATION + ALT_SCRIPT_NAME

WOTMOD_ROOTDIR = 'res'
SCRIPT_RELDIR = 'scripts/client/gui/mods'

BUILD_DIR = 'build'

SRCS = [
    (SCRIPT_NAME, SCRIPT_RELDIR),
    'meta.xml',
    'readme.txt'
]

def compile_python(src, dstdir, virtualdir):
    basename = os.path.basename(src)
    dstfile = os.path.splitext(basename)[0] + '.pyc'
    py_compile.compile(file=src, cfile=os.path.join(dstdir, dstfile), dfile=os.path.join(virtualdir, basename), doraise=True)
    return dstfile

def apply_template(src, dstdir, parameters):
    basename = os.path.basename(src)
    dst = os.path.join(dstdir, basename)
    with open(src, 'r') as in_file, open(dst, 'w') as out_file:
        out_file.write(Template(in_file.read()).substitute(parameters))
    return basename

def split(path):
    head, tail = os.path.split(path)
    if not head:
        return [ tail ]
    result = split(head)
    result.append(path)
    return result
    
def main():
    inifile = ConfigParser.SafeConfigParser()
    inifile.read('config.ini')

    class config:
        name        = inifile.get('mod', 'name')
        author      = inifile.get('mod', 'author')
        version     = inifile.get('mod', 'version')
        description = inifile.get('mod', 'description')
        support_url = inifile.get('mod', 'support_url')
        github_page = inifile.get('mod', 'github_page')
        wot_version = inifile.get('wot', 'version')

    parameters = dict(
        package     = '{}.{}_{}.wotmod'.format(config.author, config.name, config.version).lower(),
        package_id  = '{}.{}'.format(config.author, config.name).lower(),
        name        = config.name,
        author      = config.author,
        version     = config.version,
        description = config.description,
        support_url = config.support_url,
        github_page = config.github_page,
        wot_version = config.wot_version
    )

    try:
        shutil.rmtree(BUILD_DIR)
    except:
        pass
    
    create_package(SRCS, os.path.join(BUILD_DIR, 'vanilla'), parameters)

    urllib.urlretrieve(ALT_SCRIPT_URL, os.path.join(BUILD_DIR, ALT_SCRIPT_NAME))
    SRCS.append((os.path.join(BUILD_DIR, ALT_SCRIPT_NAME), SCRIPT_RELDIR))
    name = config.name + 'Plus'
    parameters['package'] = '{}.{}_{}.wotmod'.format(config.author, name, config.version).lower()
    parameters['name'] = name
    parameters['version'] = config.version + '+'

    create_package(SRCS, os.path.join(BUILD_DIR, 'plus'), parameters)

    
def create_package(files, build_dir, parameters):
    try:
        shutil.rmtree(build_dir)
    except:
        pass
    os.makedirs(build_dir)

    paths = []
    for target in files:
        if isinstance(target, list) or isinstance(target, tuple):
            src, reldir = target
            file = apply_template(src, build_dir, parameters)
            dst = compile_python(os.path.join(build_dir, file), build_dir, reldir)
            paths.append((dst, os.path.join(WOTMOD_ROOTDIR, reldir, dst)))
        else:
            dst = apply_template(target, build_dir, parameters)
            paths.append((dst, dst))

    package_path = os.path.join(build_dir, parameters['package'])
    with zipfile.ZipFile(package_path, 'w', compression=zipfile.ZIP_STORED) as package_file:
        for source, target in paths:
            for dir in split(target)[0:-1]:
                try:
                    package_file.getinfo(dir + '/')
                except KeyError:
                    package_file.write('.', dir, zipfile.ZIP_STORED)
            package_file.write(os.path.join(build_dir, source), target, zipfile.ZIP_STORED)

if __name__ == "__main__":
    main()
