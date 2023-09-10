import csv
import json
from github import Auth
from github import Github

csv_file = 'gdsc.csv'
json_file = 'data.json'
GITHUB_TOKEN = ""
github = Github(GITHUB_TOKEN)
username = "gdsc-kits"
repository_name = "gdsc-kits.github.io"

#=========================================================================

def remove_file():
    file_path = "data.json"
    repository = github.get_user(username).get_repo(repository_name)
    file = repository.get_contents(file_path)
    commit_message = "Delete json file"
    repository.delete_file(
        path=file.path,
        message=commit_message,
        sha=file.sha
    )
    print("File deleted successfully!")

def save_files():
    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    with open(f'data.json', 'rb') as file:
        data = file.read()
    repo = g.get_repo(f'{username}/{repository_name}')
    repo.create_file(f'{json_file}', 'updating json file', data, branch='main') 
    print("file uploaded")

def csv_to_jason():
    data = []
    with open(csv_file, 'r') as csv_input:
        csv_reader = csv.DictReader(csv_input)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w') as json_output:
        json.dump(data, json_output, indent=4)
    print(f'Conversion from CSV to JSON completed. Output saved to {json_file}')   
print('''
   _____ _____   _____  _____ 
  / ____|  __ \ / ____|/ ____|
 | |  __| |  | | (___ | |     
 | | |_ | |  | |\___ \| |     
 | |__| | |__| |____) | |____ 
  \_____|_____/|_____/ \_____|         
''')
print("make sure the file name is gdsc.csv and no other file is present")
print("press ENTER to confirm")
a = input()
if a=="gdsc":
    csv_to_jason()
    remove_file()
    save_files()
    