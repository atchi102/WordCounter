#!/usr/bin/python
# import collections
#
#
# with open("./Output/") as file:
#     for line in file:
#         wordcount.update(line.split())
#
# for k,v in wordcount.iteritems():
#     print k, v


import os
import sys
import collections

walk_dir = sys.argv[1]
wordcount = collections.Counter()

print('walk_dir = ' + walk_dir)

print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    print('list_file_path = ' + list_file_path)

    with open(list_file_path, 'wb') as list_file:
        for subdir in subdirs:
            print('\t- subdirectory ' + subdir)

        for filename in files:
            file_path = os.path.join(root, filename)

            print('\t- file %s (full path: %s)' % (filename, file_path))

            with open(file_path) as f:
                for line in f:
                    wordcount.update(line.split())

for k,v in wordcount.iteritems():
    print k, v
