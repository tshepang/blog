import os
from fabric.api import local, task, settings, hide

OUTPUTDIR = '.output'


@task(alias='make')
def build():
    local('rm -fr {}/*'.format(OUTPUTDIR))
    local('pelican --settings settings.py')


@task
def push():
    local('cd {} && git add --all && git commit -am "build" '
          '&& git push origin master'.format(OUTPUTDIR))
    with settings(hide('warnings'), warn_only=True):
        local('hg push')


@task(default=True)
def all():
    build()
    push()
