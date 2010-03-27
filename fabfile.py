import os.path
from fabric.api import *

env.project_name = os.path.split(os.path.dirname(os.path.abspath(__file__)))[-1]
env.production = False

def staging():
    env.hosts = ['s5.wservices.ch']
    env.user = 'philippbosch'

def production():
    raise NotImplemented

def deploy():
    if env.production:
        input = prompt('Are you sure you want to deploy to the production server?', default="n", validate=r'^[yYnN]$')
        if input not in ['y','Y']:
            exit()
    run('export WORKON_HOME=$HOME/.virtualenvs && source $HOME/bin/virtualenvwrapper_bashrc && workon %(project_name)s && cd ~/%(project_name)s && git pull origin master && ./manage.py migrate && ./manage.py syncdb && ~/init/%(project_name)s restart' % { 'project_name': env.project_name })

def install_requirements():
    run('export WORKON_HOME=$HOME/.virtualenvs && source $HOME/bin/virtualenvwrapper_bashrc && workon %(project_name)s && cd ~/%(project_name)s && pip install -r requirements.txt && ~/init/%(project_name)s restart' % { 'project_name': env.project_name })

def get_media():
    run('cd %(project_name)s/media && tar -cvzf media.tar.gz uploads cms_page_media' % { 'project_name': env.project_name })
    get('%(project_name)s/media/media.tar.gz' % { 'project_name': env.project_name }, 'media.tar.gz')
    run('rm %(project_name)s/media/media.tar.gz' % { 'project_name': env.project_name })

def get_dump():
    run('cd %(project_name)s && mysqldump %(user)s_%(project_name)s > %(project_name)s.sql' % { 'project_name': env.project_name, 'user': env.user })
    get('%(project_name)s/%(project_name)s.sql' % { 'project_name': env.project_name }, '%(project_name)s.sql' % { 'project_name': env.project_name })
    run('rm %(project_name)s/%(project_name)s.sql' % { 'project_name': env.project_name })
    
    input = prompt('Import dump into database?', default="y", validate=r'^[yYnN]$')
    if input in ['y','Y']:
        # quick & dirty: just take the first host and ignore others that might exist
        local('mysql %(project_name)s < %(project_name)s.sql.%(hostname)s' % { 'project_name': env.project_name, 'hostname': env.hosts[0] })
        local('rm %(project_name)s.sql.%(hostname)s' % { 'project_name': env.project_name, 'hostname': env.hosts[0] })
