import subprocess

commit_message = input('Enter commit message: ')


# Commands for initializing Git repository and pushing to GitHub
git_commands = [
    'git add .',
    f'git commit -m {commit_message}',
    'git push'
]


for command in git_commands:
    subprocess.run(command, shell=True)
