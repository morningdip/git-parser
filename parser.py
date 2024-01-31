import re
import sys
import csv

GIT_COL = ['Hash ID', 'Short Hash ID', 'Owner', 'Commit Date', 'Commit Relative Date', 'Title']


def parse_commit(input):
    commits = []
    for i in input:
        hash_id, shord_hash_id, owner, commit_date, commit_relative, title = i.split(',')
        commits.append([hash_id, shord_hash_id, owner, commit_date, commit_relative, title])

    with open('commit_log.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(GIT_COL)
        csv_writer.writerows(commits)


if __name__ == '__main__':
    parse_commit(sys.stdin.readlines())
