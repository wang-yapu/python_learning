import os,time
source = ['/Users/wyp/python_demo/continue.py','/Users/wyp/python_demo/if.py']
target_dir = '/Users/wyp/'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to',target
else:
	print 'Backup FAILED'
