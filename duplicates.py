import os
import sys
from collections import defaultdict


def get_fileinfo(searchpath):
    fileinfo = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(searchpath):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):
                fileinfo[filename, os.path.getsize(filepath)].append(filepath)
    return fileinfo


def get_duplicates(fileinfo):

    return {
        namesize: filelist
        for namesize, filelist in fileinfo.items()
        if len(filelist) > 1
    }


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('Syntax: duplicates.py <directory_path>')

    fileinfo = get_fileinfo(sys.argv[1])
    if not fileinfo:
        sys.exit('Path not exist or directory is empty')

    duplicates = get_duplicates(fileinfo)
    for namesize, filelist in duplicates.items():

        print('{} - {} bites found on the following path: '.format(
            namesize[0],
            namesize[1]
        ))

        for filepath in filelist:
            print('\t{}'.format(filepath))
