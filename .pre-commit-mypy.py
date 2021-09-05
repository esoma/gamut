
# python
import os
import subprocess
import sys

repo = os.path.dirname(os.path.realpath(__file__))
process = subprocess.run(['pip', 'install', '-e', repo], capture_output=True)
if process.returncode != 0:
    sys.stderr.write('Failed to install gamut:\n')
    sys.stderr.write(process.stderr.decode())
    sys.exit(process.returncode)

process = subprocess.run(['mypy', *sys.argv[1:]])
sys.exit(process.returncode)
