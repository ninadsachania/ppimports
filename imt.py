#! /usr/bin/python3

# Author: Ninad Sachania
# Aim: Takes all the `import mod[, mod]*` lines out of a .py file and sorts them via their length.
# It serves no other purpose than to make the import lines at the top of a .py file pretty and organized.

import sys
import re


def main():
    filename = ' '.join(sys.argv[1:])
    f = open(filename, 'r')

    r = re.compile('^import*')

    lines = []

    for line in f:
        if r.match(line.strip()):
            lines.append(line.strip().rstrip('\n'))

    # an empty set
    imports = set()

    # remove the lines
    for i in lines:
        imts = i.split(' ')[1:]

        for imt in imts:
            # Won't add duplicate modules
            imports.add(imt.rstrip(','))

    # sort according to length of the module name
    modules = [x for x in imports]
    modules.sort(key=len)

    for module in modules:
        print('import ' + str(module))


if __name__ == '__main__':
    main()
