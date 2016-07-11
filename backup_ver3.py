#coding=utf-8
# Filename: backup_ver3.py

import os,time
 = ['/Users/wyp/python_demo/if.py','/Users/wyp/python_demo/using_name.py']
target_dir = '/Users/wyp/'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')
comment = raw_input('Enter a comment -->')
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

# 如果不存在子路径,创建
if not os.path.exists(today):
	 os.mkdir(today)
	 print 'Successfully created directory',today

# 调用系统命令
zip_command = "zip -r '%s' %s" % (target, ' '.join(source))

#运行备份
if os.system(zip_command) == 0:
	print 'Successful backup to',target
else:
	print 'Backup FAILED'
