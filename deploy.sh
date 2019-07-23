#! /bin/bash

cd ~/git/eduardofilo.mkdocs
source /home/edumoreno/.local/share/virtualenvs/eduardofilo.mkdocs-h5zpApr9/bin/activate
cd ~/git/eduardofilo.github.io
git reset HEAD .
git checkout -- .
mkdocs gh-deploy --config-file ../eduardofilo.mkdocs/mkdocs.yml --remote-branch master
cd ~/git/eduardofilo.mkdocs
