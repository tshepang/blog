import os
from fabric.api import local, task

OUTPUTDIR = os.path.join(os.path.expanduser("~/tmp"), 'blog')


@task(alias='make')
def build():
    local('rm -fr {}/*'.format(OUTPUTDIR))
    local('liquidluck build')


@task
def push():
    local('cd {} && git add . && git commit -am "build" '
          '&& git push origin master'.format(OUTPUTDIR))
    local('hg push')


@task(default=True)
def all():
    build()
    push()
