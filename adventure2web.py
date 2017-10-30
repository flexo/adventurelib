'''adventure2web.py -- compile an adventurelib game for the web.'''
import os
import shutil
import sys
import subprocess
import adventurelib

def preprocess(src, dest):
    drop = False
    with open(src) as sf, open(dest, 'w') as df:
        for line in sf:
            if line.replace(' ', '').startswith('#ifnotweb'):
                drop = True
                continue
            if line.replace(' ', '').startswith('#endnotweb'):
                drop = False
                continue
            if not drop:
                df.write(line)

def main():
    target_dir = sys.argv[1]
    game_file = sys.argv[2] # TODO - proper command line parsing

    print('preparing target directory...')
    # copy user and adventurelib files into the target directory
    adlib_orig = adventurelib.__file__
    adlib_orig_dir, adlib_orig_file = os.path.split(adlib_orig)
    adlib_target = os.path.join(target_dir, 'adventurelib.py')
    game_buildname = os.path.join(target_dir, 'webgamemain.py')
    webpy_buildname = os.path.join(target_dir, 'web.py')

    os.makedirs(target_dir)
    # TODO - what if user has multiple files?
    shutil.copy(game_file, game_buildname)
    shutil.copy(adlib_orig, adlib_target + '.orig')
    shutil.copy(os.path.join(adlib_orig_dir, 'web.html'),
                os.path.join(target_dir, 'web.html'))
    shutil.copy(os.path.join(adlib_orig_dir, 'web.py'),
                webpy_buildname)

    print('preparing adventurelib for web...')
    preprocess(adlib_target + '.orig', adlib_target)
    os.unlink(adlib_target + '.orig')

    print('compiling...')
    try:
        proc = subprocess.run(['transcrypt', '-b', '-n', '-m', webpy_buildname])
        proc.check_returncode()
        print('[TODO Information on how to open the html file]') # TODO
    except subprocess.CalledProcessError:
        traceback.print_exc()
        print('Error: the game failed to compile.')

