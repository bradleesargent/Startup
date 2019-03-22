import subprocess
import os
shutdown="c:/Windows/System32/shutdown.exe"
shutcommand = [shutdown,"/s","/i"]
results=input("Shut down the computer?")
results=input("Are you sure?")
process = subprocess.Popen(shutcommand)
