#!/bin/bash -e
# Generates pip dependency files for build and test purposes
# NOTE: The generated requirements files are named in a weird
#       way here because we are trying to prevent requires.io
#       from picking up test dependencies and reporting on them
#       to our users. It seems to pick up quite a variety of
#       file patterns, recursively within the repo. *.reqs
#       seems to be a suitable exception
# NOTE: The requirements files generated by this script are
#       referenced by the tox.ini config file at build time.
#       Any changes to this pattern will need to be reflected
#       there as well.
rm -rf src/*.egg-info
rm -rf build
rm -rf dist
virtualenv -p `pyenv which python3` tmp
source ./tmp/bin/activate
pip install -e ".[dev]"
pip freeze --exclude-editable > ./requirements.txt
deactivate
rm -rf tmp

# Update dependencies specific for ReadTheDocs
virtualenv -p `pyenv which python3` tmp
source ./tmp/bin/activate
pip install sphinx sphinxcontrib-apidoc sphinx-rtd-theme
pip freeze > ./docs/requirements.txt
deactivate
rm -rf tmp