import os
import subprocess
introduction="file:///C:/Users/bradl/OneDrive/Startup/home.html"
theword = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

cmd = [theword , introduction]
exists = os.path.isfile(introduction)
print(exists)
if exists:
	print(introduction + " exists")
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	for line in process.stdout:
		print(line)
exit(0)
#results=input("Is homepage started?")


