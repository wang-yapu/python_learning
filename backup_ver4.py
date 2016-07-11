# Filename:backup_ver4.py
import os,time

source = ['/Users/wyp/python_learning/backup_ver2.py','/Users/wyp/python_learning/continue.py ']
target_dir = '/Users/wyp/python_learning/'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment -->')
if len(comment) == 0:
	target = today + os.sep + now +'.zip'
else:
	target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory',today

zip_command = "zip -rcv '%s' %s" % (target,' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to',target
else:
	print 'Backup FAILED'
