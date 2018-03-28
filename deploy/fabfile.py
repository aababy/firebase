# encoding=utf8
'''
Created on 2016-08-18

@author: jingyang <jingyang@nexa-corp.com>

Usage:
    fab staging deploy
    fab prod deploy
'''
from fabric.api import local
from fabric.context_managers import lcd, cd
from fabric.operations import put, run
from fabric.state import env


PROJECT_NAME = "jigsaw"
PROJECT_DIR = "/var/project/jigsaw/"  # project dir on server


def staging():
    global PROJECT_NAME
    global PROJECT_DIR
    
    PROJECT_NAME='jigsaw_test'
    PROJECT_DIR = "/var/project/jigsaw_test/"
    env.user = "jigsaw"
    env.hosts = ["10.0.2.251"]

def prod():
    env.user = "jigsaw"
    env.hosts = ["jigsaw.stm.com"]
    # env.key_filename =r'D:\home\myopenssh'


def archive():
    with lcd(".."):
        local("git archive -o deploy/{}.tar.gz HEAD".format(PROJECT_NAME)) #master catch


def upload():
    with cd(PROJECT_DIR):
        put("{}.tar.gz".format(PROJECT_NAME), ".")


def extract():
    with cd(PROJECT_DIR):
        run("tar xf {}.tar.gz".format(PROJECT_NAME))


def deploy():
    archive()
    upload()
    extract()

def test():
    run('ls')