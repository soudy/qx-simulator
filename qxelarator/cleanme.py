# script to clean temporary files generated by installation

import os
import shutil

dirs = ['build', 'cbuild', 'dist', 'qxelarator.egg-info']
files = ['qxelarator/qxelarator.py']

for dir in dirs:
	try:
		shutil.rmtree(dir)
	except OSError:
		pass

for file in files:
    try:
        os.remove(file)
    except OSError:
        pass
