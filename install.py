import os
import subprocess

print('Installing PIP')
subprocess.run(['/usr/bin/python3', '-m', 'ensurepip', '--upgrade'], check=True)

print('Installing PIP packages')
subprocess.run(['/usr/bin/python3', '-m', 'pip', 'install', '--no-cache-dir', '-r', 'requirements.txt'], check=True)

print('Cleaning up')
for root, _, files in os.walk('/home'):
    for file in files:
        if file.endswith('.pyc'):
            os.remove(os.path.join(root, file))
for root, _, files in os.walk('/tmp'):
    for file in files:
        os.remove(os.path.join(root, file))