#
import os
import sys
import time, datetime
#import docker
#import subprocess
#from collections import deque
#from git import Repo
#import tarfile
from git import Repo, RemoteProgress


def log(log_text):
    print(datetime.datetime.now(), '   ', log_text, flush=True)


def error(log_text):
    log('ERROR: ' + log_text)
    sys.exit(1)


class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message, flush=True)


log('Starting installation from GITHUB')

# Get environment variables
REPO_URL = os.getenv('REPO_URL', '')
if REPO_URL == '':
    error('No repository specified - You need to set the environment variable REPO_URL.')
log('GitHub repository: %s' % REPO_URL)
GIT_USERNAME = os.getenv('GIT_USERNAME', '')
GIT_PASSWORD = os.getenv('GIT_PASSWORD', '')
# GIT_USERNAME empty XOR GIT_PASSWORD empty
if (GIT_USERNAME == '' or GIT_PASSWORD == '') and not (GIT_USERNAME == '' and GIT_PASSWORD == ''):
    error('You need to specify either both of GIT_USERNAME and GIT_PASSWORD or NONE.')
BASE_DIR = os.getenv('BASE_DIR', '~/repo')
REPO_BRANCH = os.getenv('REPO_BRANCH', 'master')
log('Branch: %s' % REPO_BRANCH)

# make sure git gets the credentials
act_dir = os.path.dirname(os.path.abspath(__file__))
log(act_dir)
os.environ['GIT_ASKPASS'] = os.path.join(act_dir, 'askpass.py')

# clone REPO
BASE_DIR = os.path.expanduser(BASE_DIR)
os.mkdir(BASE_DIR)
log('Cloning into %s' % BASE_DIR)

Repo.clone_from(REPO_URL, BASE_DIR, branch=REPO_BRANCH, progress=CloneProgress())

log('Starting run-me.py')
os.system('pip3 install -r '+BASE_DIR+'/requirements.txt')
os.system('python3 '+BASE_DIR+'/run-me.py')
