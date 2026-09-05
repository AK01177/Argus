import tempfile

import git


def clone_repo_to_temp(repo_url):
    temp_dir = tempfile.mkdtemp()
    print(f"Cloning {repo_url} into {temp_dir}")

    git.Repo.clone_from(repo_url, temp_dir, depth=1)
    print("Clone Successful!")

    return temp_dir
