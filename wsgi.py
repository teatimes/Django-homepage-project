#!/usr/bin/python
import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "src.settings.common"
## GETTING-STARTED: make sure the next line points to your django project dir:
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'src'))
from distutils.sysconfig import get_python_lib
os.environ['PYTHON_EGG_CACHE'] = get_python_lib()

application = get_wsgi_application()
