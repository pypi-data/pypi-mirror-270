from git import Repo

def get_latest_commit_message():
    repo = Repo(search_parent_directories=True)
    latest_commit = repo.commit()
    return latest_commit.message
