#!/usr/bin/env python
import subprocess

# -- Configuration
KEEP_MOST_RECENT = 2
BRANCHES_TO_SAVE = [
    'master',
    'develop',
]

# -- Prune Branches
def main():
    sorted_branches = subprocess.check_output(['git', 'for-each-ref',
            '--sort=-committerdate', 'refs/heads/'])
    branches_list = sorted_branches.split("\n")
    branch_names = get_branch_names(branches_list)
    branches_to_remove = branch_names[KEEP_MOST_RECENT:]
    delete_git_branches(branches_to_remove)


def get_branch_names(branches_list):
    branch_names = []
    for branch in branches_list:
        if not branch:
            continue
        branch_name = branch.split('/')[-1]
        if branch_name not in BRANCHES_TO_SAVE:
            branch_names.append(branch_name)

    return branch_names


def delete_git_branches(branches_to_remove):
    for branch in branches_to_remove:
        try:
            subprocess.call(['git', 'branch', '-d', branch])
        except Exception as err:
            print "Failed to delete git branch %s: %s" % (branch, err)


if __name__ == '__main__':
    main()
