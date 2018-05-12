#!/usr/bin/env python
from fabric.api import *

env.source_dir = '' # source dir where the repo is checked out
env.theme_source_dir = '' #dir within source dir where theme is checked out
env.theme_dir = '' # dir where theme is on the webservers 'htdocs'

def prod():
    env.hosts = ['0.0.0.0']
    env.user = 'user'
    env.group = 'group'
    env.branch = 'deploy_branch'
    env.instance = 'production'
    env.key_filename = '' # path to .pem file

def deploy():
    with cd(env.source_dir):
        run('git pull origin master')
        run('rm -rf %(theme_dir)s' % env)
        run('cp -R %(theme_source_dir)s %(theme_dir)s' % env)
