#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Convenience wrapper for starting an appengine tool."""


import os
import sys

if not hasattr(sys, 'version_info'):
  sys.stderr.write('Very old versions of Python are not supported. Please '
                   'use version 2.5 or greater.\n')
  sys.exit(1)
version_tuple = tuple(sys.version_info[:2])
if version_tuple < (2, 4):
  sys.stderr.write('Error: Python %d.%d is not supported. Please use '
                   'version 2.5 or greater.\n' % version_tuple)
  sys.exit(1)
if version_tuple == (2, 4):
  sys.stderr.write('Warning: Python 2.4 is not supported; this program may '
                   'break. Please use version 2.5 or greater.\n')

DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
SCRIPT_DIR = os.path.join(DIR_PATH, 'google', 'appengine', 'tools')

EXTRA_PATHS = [
  DIR_PATH,
  os.path.join(DIR_PATH, 'lib', 'django'),
  os.path.join(DIR_PATH, 'lib', 'webob'),
  os.path.join(DIR_PATH, 'lib', 'yaml', 'lib'),
]

SCRIPT_EXCEPTIONS = {
  "dev_appserver.py" : "dev_appserver_main.py"
}

if __name__ == '__main__':
  sys.path = EXTRA_PATHS + sys.path
  script_name = os.path.basename(__file__)
  script_name = SCRIPT_EXCEPTIONS.get(script_name, script_name)
  script_path = os.path.join(SCRIPT_DIR, script_name)
  execfile(script_path, globals())
