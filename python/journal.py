import os
import datetime
import subprocess
src = "C:/Users/bradl/OneDrive/Documents/Journal/template.docx"
now = datetime.datetime.now()
theyear = now.year
theday = '%02d' % now.day
themonth = '%02d' % now.month
dst="C:/Users/bradl/OneDrive/Documents/Journal/"+str(theyear)+str(themonth)+str(theday)+".docx"
print(theyear)
print(theday)
print(themonth)
print (src)
print(dst)
exists = os.path.isfile(dst)
print(exists)
if exists:
    print(dst + " exists")
else:
    from shutil import copyfile
    copyfile(src, dst)
    print("copying "+src+" to "+dst)
theword = "C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE"
cmd = [theword , dst]
process = subprocess.Popen(cmd)
cmdtemplate = [theword , src]
process2= subprocess.Popen(cmdtemplate)


