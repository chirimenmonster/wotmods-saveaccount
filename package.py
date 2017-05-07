import os
import py_compile
import zipfile

SRC = 'mod_saveaccount.py'
WOTMOD = 'chirimen.saveaccount_1.2.2.wotmod'

MOD_REL_DIR = 'scripts/client/gui/mods'
WOTMOD_DIR = 'res'

def split(path):
    head, tail = os.path.split(path)
    if not head:
        return [ tail ]
    result = split(head)
    result.append(path)
    return result

def main():
    mod = os.path.splitext(SRC)[0] + '.pyc'
    py_compile.compile(file=SRC, cfile=mod, dfile=os.path.join(MOD_REL_DIR, SRC), doraise=True)

    try:
        os.remove(WOTMOD)  
    except:
        pass

    list = split(os.path.join(WOTMOD_DIR, MOD_REL_DIR, mod))
    list.pop()
    
    paths = []
    for d in list:
        paths.append(('.', d))
    
    paths.append((mod, os.path.join(WOTMOD_DIR, MOD_REL_DIR, mod)))
    paths.append(('meta.xml',   'meta.xml'      ))
    paths.append(('readme.txt', 'readme.txt'    ))
    
    with zipfile.ZipFile(WOTMOD, 'w', compression=zipfile.ZIP_STORED) as package_file:
        for source, target in paths:
            package_file.write(source, target, zipfile.ZIP_STORED)

if __name__ == "__main__":
    main()
