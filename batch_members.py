from github import Github
from dotenv import load_dotenv
import os
import argparse

# make app nice with cli arguments
parser = argparse.ArgumentParser(description="Batch add users to a gh org")
parser.add_argument('user_file', type=str, help='a file with emails linked to github account, 1/line')

args = vars(parser.parse_args())

print('loading users...')

users = set()

print('reading emails from file...')
print(args.get('user_file'))
with open(args.get('user_file'), 'r') as fin:
    for line in fin.readlines():
        users.add(line.strip())

load_dotenv()

gh_username = os.getenv('GH_USERNAME')
gh_passws = os.getenv('GH_PASSWD')

org_name = os.getenv('GH_ORG')

print("authenticating...")
g = Github(gh_username, gh_passws)

org = g.get_organization(org_name)

print('inviting users...')
for user in users:
    org.invite_user(email=user)