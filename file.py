import sys
import subprocess

subprocess.check_call(
    [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

subprocess.check_call(
    [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
