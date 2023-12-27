import subprocess

readme = input('Enter readMe: ')
commit_message = input('Enter commit message: ')
branch = input('Enter branch[main/master]: ')
repo_url = input('Enter origin url: ')

# Command to create README.md and add initial content
create_readme_command = f'echo {readme} >> README.md'

# Commands for initializing Git repository and pushing to GitHub
git_commands = [
    'git init',
    'git add README.md',
    f'git commit -m {commit_message}',
    f'git branch -M {branch}',
    f'git remote add origin {repo_url}',
    f'git push -u origin {branch}'
]

# Execute the commands
subprocess.run(create_readme_command, shell=True)

for command in git_commands:
    subprocess.run(command, shell=True)
