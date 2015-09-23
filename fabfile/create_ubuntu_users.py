from fabtools import require


def create_ubuntu_users():
    require.user(
        name='zhorzh',
        group='developers',
        shell='/bin/bash',
        ssh_public_keys='/home/zhorzh/.ssh/id_rsa.pub')
    require.users.sudoer(
        username='zhorzh',
        hosts='ALL',
        operators='ALL',
        passwd=False,
        commands='ALL')
    require.users.sudoer(
        username='root',
        hosts='ALL',
        operators='ALL',
        passwd=False,
        commands='ALL')
