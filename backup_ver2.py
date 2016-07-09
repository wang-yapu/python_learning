# Filename: backup_ver2.py

import os,time

source = ['/Users/wyp/python_demo/if.py','/Users/wyp/python_demo/using_name.py']
target_dir = '/Users/wyp/'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)   #make directory
	print 'Successfully created directory',today

target = today + os.sep + now + '.zip'

zip_command = "zip -r '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
