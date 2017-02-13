#!/usr/bin/env

import os


def clean_old_dotfiles(dotfile_list):
    home_url = os.popen('echo $HOME').read().rstrip('\n')
    home_list = os.listdir(home_url)
    for f in dotfile_list:
        if f in home_list:
            os.system('rm ' + home_url + '/' + f)
            print ('Clean the old file :' + f)


def ln_new_dotfiles(dotfile_list):
    thisdir = os.popen('pwd').read().rstrip('\n')
    for f in dotfile_list:
        os.system('ln -s {0}/dotfiles/{1} ~/{1}'.format(thisdir, f))


def main():
    print "Check for basic softwares..."
    os.system('sudo bash ./scripts/basicInstall.sh')
    print "Try to config git..."
    os.system('bash ./scripts/setupGit.sh')

    print "Begin to ln the dotfiles..."
    dotfile_list = os.listdir('./dotfiles')
    clean_old_dotfiles(dotfile_list)
    ln_new_dotfiles(dotfile_list)

    print "Update global .gitconfig..."
    os.system('bash ./scripts/setupGit.sh')

if __name__ == '__main__':
    main()
