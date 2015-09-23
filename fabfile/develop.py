from fabric.api import sudo, run


def develop():
    sudo('apt-get install -y vim')
    sudo('apt-get install -y git')
    sudo('apt-get install -y tree')
    sudo('apt-get install -y ranger')
    sudo('apt-get install -y xclip')
    sudo('apt-get install -y cloc')
    run('git clone http://github.com/zhorzh/dotfiles /home/zhorzh/dotfiles')
    run('mv /home/zhorzh/dotfiles/.vimrc /home/zhorzh && \
        mv /home/zhorzh/dotfiles/.bashrc /home/zhorzh && \
        mv /home/zhorzh/dotfiles/.gitconfig /home/zhorzh')
    run('git clone https://github.com/VundleVim/Vundle.vim.git \
        /home/zhorzh/.vim/bundle/Vundle.vim')
