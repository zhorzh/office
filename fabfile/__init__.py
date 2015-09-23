from fabric.api import env
from develop import develop 
from setup import setup 

env.user = 'zhorzh'
env.hosts = ['46.101.145.122']
env.shell = '/bin/bash -l -i -c'
