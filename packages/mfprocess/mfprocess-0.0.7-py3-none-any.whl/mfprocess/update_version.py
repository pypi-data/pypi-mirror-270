import sys
import fileinput

new_version = sys.argv[1]

# Replace the version placeholder in setup.py with the new version
with fileinput.FileInput("../setup.py", inplace=True) as file:
    for line in file:
        print(line.replace('{{VERSION_PLACEHOLDER}}', new_version), end='')
