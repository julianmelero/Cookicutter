import subprocess


print("Initializing a git repository...")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m' , 'Initial commit'])

print("This is the beginning....")
