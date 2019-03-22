import subprocess
import os
from os import walk

def maketags():
    thecommand="C:/Users/bradl/OneDrive/Downloads/Emacs/emacs-26.1-x86_64/bin/etags.exe"
    mypath="C:/Users/bradl/AppData/Roaming/.emacs.d/elpa/org-9.2"
    otags="c:/Users/bradl/OneDrive/dropbox/.emacs.d/brad.el"
    outputtags="c:/Users/bradl/OneDrive/Startup/python/orgtags"
    outputorgtags="c:/Users/bradl/OneDrive/Startup/python/tags"
    cmd=[thecommand,otags,"-o",outputorgtags]
    print(cmd)
    process = subprocess.Popen(cmd)
    f = []
    theprefix = ""
    for (dirpath, dirnames, filenames) in walk(mypath):
        for file in filenames:
            if file.endswith(".el"):
                thefile=os.path.join(mypath,file)
                print(thefile)
                if (theprefix == ""):
                    cmd = [thecommand, thefile, "-o", outputtags]
                else:
                    cmd = [thecommand, theprefix, thefile, "-o", outputtags]
                print(cmd)
                process = subprocess.Popen(cmd)
                theprefix="-a"
if __name__ == '__main__':
    maketags()
    exit()