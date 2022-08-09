#! /bin/bash

cd ~/git/eduardofilo.mkdocs
source /home/edumoreno/.virtualenvs/eduardofilo.mkdocs/bin/activate
cd ~/git/eduardofilo.github.io
git pull origin
git reset HEAD .
git checkout -- .
mkdocs gh-deploy --config-file ../eduardofilo.mkdocs/mkdocs.yml --remote-branch master
cd ~/git/eduardofilo.mkdocs
