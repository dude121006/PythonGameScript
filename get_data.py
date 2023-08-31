import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"


def FindAllGamePaths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
        break

    return game_paths

def CreateNewDir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def GetDirNames(paths, toStrip):
    NewDirNames = []

    for path in paths:
        _,dirName = os.path.split(path)
        NewDirName = dirName.replace(toStrip, '')
        NewDirNames.append(NewDirName)

    return NewDirNames 
    

def Main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = FindAllGamePaths(source_path)
    new_game_dirs = GetDirNames(game_paths, "_game")
    print(new_game_dirs)

    CreateNewDir(target_path)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("Enter only 3 arguments")
    
    source, target = args[1:]
    Main(source, target)