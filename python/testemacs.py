import datetime
import os
import subprocess
now = datetime.datetime.now()
theyear = now.year
theday = '%02d' % now.day
themonth = '%02d' % now.month
from datetime import date
weeknumber = '%02d' % date.today().isocalendar()[1]
weekday = date.today().weekday()
filename="C:/Users/bradl/OneDrive/Documents/Journal/"+str(theyear)+str(weeknumber)+".org"
filename2="C:/Users/bradl/OneDrive/Documents/Journal/"+str(theyear)+str(themonth)+str(theday)+".org"
emacs="C:/Users/bradl/OneDrive/emacs/bin/runemacs.exe"
book="C:/Users/bradl/OneDrive/dropbox/catholic/Project/book/book.org"
import Tkinter as tk
import ttk
cmd = [emacs , filename,filename2]
process = subprocess.call(cmd,shell=True)
