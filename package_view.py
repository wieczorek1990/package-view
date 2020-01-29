#!/usr/bin/env python3

import json
import os
import sys


if len(sys.argv) == 0:
    print('Usage:\n\tpackage_view.py directory')
    exit(1)

directory = sys.argv[1]
package_json_filepath = os.path.join(directory, 'package.json')
open_file = open(package_json_filepath, 'r')
dictionary = json.loads(open_file.read())

print(f"Name: {dictionary['name']}")
print(f"Description:\n\t{dictionary['description']}")
print(f"Author: {dictionary['author']}")
print(f"License: {dictionary['license']}")
print(f"Version: {dictionary['version']}")

