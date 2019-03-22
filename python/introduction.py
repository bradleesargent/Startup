import os
import subprocess
introduction="C:/Users/bradl/OneDrive/Startup/starters/introduction.docx"
theword = "C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE"

cmd = [theword , introduction]
exists = os.path.isfile(introduction)
print(exists)
if exists:
	print(introduction + " exists")
	process = subprocess.Popen(cmd)
exit()
