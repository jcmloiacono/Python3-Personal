# https://docs.fabfile.org/en/2.5/

from fabric.api import *

# host
env.hosts = [IP]

# username
env.user = 'USER'

# pecify path to server public key here:
env.key_filename = '~/.ssh/id_rsa.pub'


@task
def deploy():
    with cd('python-web-project'):
        run('git pull')

        with prefix('source myprojectenv/bin/activate'):
            run('pip install -r requirements.txt)

            run('python manange.py migrate')
            run('python manage.py collectstatic --noinput')

        sudo('systemctl daemon-reload')
        sudo('supervisorctl python-web-project')
        sudo('systemctl restart gunicorn')

    print('>>> Deploy completed!')
