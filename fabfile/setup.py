from fabric.api import sudo, run, cd
from fabtools import require, supervisor


def setup():
    sudo('apt-get update')
    sudo('apt-get install -y git')
    sudo('apt-get install -y postgresql postgresql-contrib libpq-dev')
    sudo('apt-get install -y nginx')
    sudo('apt-get install -y nodejs')
    sudo('ln -s /usr/bin/nodejs /usr/bin/node')
    sudo('apt-get install -y npm')
    sudo('npm install -g bower')
    sudo('apt-get install -y python-pip')
    sudo('apt-get install -y python-dev')
    sudo('pip install virtualenv')
    sudo('pip install virtualenvwrapper')
    sudo('pip install supervisor')

    postgres_user = 'office_application'
    postgres_database = 'office_database'
    postgres_password = '123'
    sudo('psql -c "CREATE USER {} WITH PASSWORD \'{}\'"'
         .format(postgres_user, postgres_password), user='postgres')
    sudo('psql -c "CREATE DATABASE {} WITH OWNER {}"'
         .format(postgres_database, postgres_user), user='postgres')

    sudo('mkvirtualenv office')

    sudo('chown -R zhorzh:developers /srv')
    sudo('chmod -R 775 /srv')
    run('git clone https://github.com/zhorzh/office /srv/office')

    with cd('/srv/office/server'):
        sudo('workon office && pip install -r requirements.txt')

    with cd('/srv/office/client'):
        run('bower install')

    require.supervisor.process(
        name='office',
        command='/home/zhorzh/.virtualenvs/office/bin/python \
            /home/zhorzh/.virtualenvs/office/bin/gunicorn \
            -b 0.0.0.0:5000 core:app',
        directory='/srv/office/server',
        stdout_logfile='/srv/office_supervisor.log',
        user='zhorzh')
    supervisor.restart_process('office')

    require.nginx.site(
        server_name='office',
        template_source='/srv/office/fabfile/nginx.template',
        port=5000,
        service_folder='office')
    require.nginx.disable('default')
    require.nginx.enable('office')
    sudo('service nginx restart')
