import glob
import sys
import os
import json

'''
This will print in terminal all the project dependencies of a NodeJS project as
well as there licenses.

Usage:
$ python licenseextractor.py /path/to/your/node/project/

Your project needs to be npm-installed because this scripts goes into node_modules
'''


project_folder = sys.argv[-1]

if not os.path.isdir(project_folder):
    print("This CLI takes a single argument: the folder of you project to analyse")
    exit()

all_package_json_paths = sorted( glob.glob(project_folder + '/node_modules/*/package.json') )


for i in all_package_json_paths:
    with open(i, 'r') as myfile:
        package_json_string = myfile.read()
        package_json_data = json.loads(package_json_string)

        try:
            package_name = package_json_data["name"]
            license = "unknown"
            try:
                license = package_json_data["license"]
            except:
                None

            print(package_name, ":", license)
        except:
            None
