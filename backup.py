import os
import time

source = ['/home/iris/mine/ByteofPython_Code']
target = '/home/iris/mine/backup'

comment = input("Enter some comment:")

if not os.path.exists(target):
    os.mkdir(target)

date = target + os.sep + time.strftime("%Y%m%d")

if len(comment) != 0:
    time = date + os.sep + time.strftime("%H%M%S") + '_' + \
            comment.replace(' ','_') + '.zip'
else:
    time = date + os.sep + time.strftime("%H%M%S") + '.zip'

if not os.path.exists(date):
    os.mkdir(date)

zip_command = "zip -r {} {}".format(time," ".join(source))

if os.system(zip_command) == 0:
    print('Succussful Backup to', date)
else:
    print('Backup FAILED!')
    
