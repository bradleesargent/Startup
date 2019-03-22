import os
import datetime
import subprocess
class freemind:
        def __init__(self):
            self.now = datetime.datetime.now()
            self.bat="C:/Users/bradl/OneDrive/Startup/python/afterfreemind.bat"
            self.theyear = self.now.year
            self.theday = '%02d' % self.now.day
            self.themonth = '%02d' % self.now.month
            self.today = datetime.datetime.today()
            self.wholemonth=self.now.strftime("%B")
            self.basedir="C:\\Users\\bradl\\Dropbox\\14 Planning"
            self.topdir=os.path.join(self.basedir,str(self.theyear))
            self.freemind="C:\Program Files (x86)\FreeMind\FreeMind.exe"
            self.monthdir=os.path.join(self.topdir,str(self.themonth)+" "+self.wholemonth)
            self.filename=os.path.join(self.monthdir,self.theday)
            print(self.wholemonth)
            self.exists = os.path.exists(self.topdir)
            print("exists="+str(self.exists))
            print("topdir="+str(self.topdir))
            if self.exists:
                print (self.topdir+" exists")
            else:
                print ("making "+self.topdir)
                os.makedirs(self.topdir)
	
            print(self.monthdir)
            self.exists = os.path.exists(self.monthdir)
            if self.exists:
                print (self.monthdir+" exists")
            else:
                print ("making "+self.monthdir)
                os.makedirs(self.monthdir)
            self.exists=os.path.exists(self.filename)
            if self.exists:
                print(self.filename+" exists")
            else:
                print ("writing "+self.filename)
            f = open(self.filename, "w")
            f.write("<map version=\"1.0.1\">")
            f.write("<node TEXT=\""+self.wholemonth+" "+str(self.theday)+", "+str(self.theyear)+"\" />")
            f.write("</map>")
            f.close()
            f = open(self.filename, "r")
            print(f.read())
        def run(self):
            f=open(self.bat,"w")
            f.write("@echo on\n")
            f.write("\""+self.freemind+"\" \""+self.filename+"\"\n")
            f.close()
        def check(self):
            self.filexists=os.path.exists(self.bat)
            print(self.filexists)
thefreemind=freemind()
thefreemind.run()
thefreemind.check()
    
