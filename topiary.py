#!/usr/bin/env python
import subprocess

# -- Configuration
KEEP_MOST_RECENT = 2
BRANCHES_TO_SAVE = [
    'master',
    'develop',
]

# -- Prune
def main():
    sorted_branches = subprocess.check_output(['git', 'for-each-ref',
            '--sort=-committerdate', 'refs/heads/'])
    print sorted_branches


if __name__ == '__main__':
	main()
