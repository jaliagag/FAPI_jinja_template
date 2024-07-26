from github import Github
from os import environ
from datetime import datetime

# Authentication is defined via github.Auth
from github import Auth

# using an access token
# auth = Auth.Token(environ["GHPPT"])


# # Public Web Github
# g = Github(auth=auth).get_user()
# dnd = g.get_repo("dnd_notes")
# latest_commit = dnd.get_commits()[0]
# commit_data = {
#     'repo': "dnd_notes",
#     'sha': latest_commit.sha,
#     # 'author': latest_commit.author.login,
#     'message': latest_commit.commit.message,
#     'date': latest_commit.commit.author.date
# }


# print(commit_data)

def get_latest_commits(repo_list, token):
    auth = Auth.Token(token)
    g = Github(auth=auth).get_user()
    commits = []

    for repo_name in repo_list:
        repo = g.get_repo(repo_name)
        latest_commit = repo.get_commits()[0]
        try: 
            commit_data = {
              'repo': repo_name,
              'sha': latest_commit.sha,
              'author': latest_commit.author.login, 
              'message': latest_commit.commit.message,
              'date': latest_commit.commit.author.date.strftime("%B %d, %Y, %H:%M:%S %Z")
            }
        except AttributeError:
            commit_data = {
              'repo': repo_name,
              'sha': latest_commit.sha,
              'author': "not found",
              'message': latest_commit.commit.message,
              'date': latest_commit.commit.author.date.strftime("%B %d, %Y, %H:%M:%S %Z")
            }


        commits.append(commit_data)

    return commits


repos = [ "django_2024", "dnd_notes"]
token = environ.get("GHPPT")
commits = get_latest_commits(repos, token)
print(commits)

# repos.close()
