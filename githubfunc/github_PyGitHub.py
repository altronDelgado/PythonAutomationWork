from github import Github
import os

# You can find all methods in this link. -> https://pygithub.readthedocs.io/en/latest/index.html

access_token=os.environ.get("GITHUB_TOKEN")

# using an access token
g = Github(access_token)
for repo in g.get_user().get_repos():
    # Repo list
    print(repo.name)

    # topics
    repo = g.get_repo("altronDelgado/test")
    repo.get_topics()

    # To get the list of branches!
    # repo = g.get_repo("<username>/<reponame>")
    repo = g.get_repo("altronDelgado/test")
    print(list(repo.get_branches()))

    # To get the list of all the stars in your repo!
    repo = g.get_repo("altronDelgado/test")
    print(repo.stargazers_count)

    # Get list of open issues!
    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        print(issue)

    repo = g.get_repo("altronDelgado/test")
    print(repo.full_name)

    # Get all of the contents of the root directory of the repository
    contents = repo.get_contents("")
    for content_file in contents:
        print(content_file)

    # Get all of the contents of the repository recursively
    repo = g.get_repo("altronDelgado/test")
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        print(file_content)

    # Create issue
    repo = g.get_repo("altronDelgado/test")
    repo.create_issue(title="This is a new test issue")

    # Get Pull Requests by Query
    repo = g.get_repo("altronDelgado/test")
    pulls = repo.get_pulls(state='open', sort='created', base='master')
    for pr in pulls:
        print(pr.number)
    
    # # Deleting a repo
    # try:
    #     repo = g.get_user().get_repo("test")
    #     repo.delete()
    #     print("Silindi.")
    # except:
    #     print("Tekrar dene.")