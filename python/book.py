import datetime
import os
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import Menu
win = tk.Tk()
win.title("Emacs")
menuBar = Menu(win)
win.config(menu=menuBar)
therow = 0

class thefile:
    def __init__(self, filename):
        self.filename=filename
        self.file = open(filename, "w")

    def appointments(self):
        if (theyear == 2019 and theday == 23 and themonth == 2):
            self.todo("* TODO Appointment by phone with the social security")
        if (theyear == 2019 and theday == 18 and themonth == 3):
            self.todo("* TODO Sleep center appointment")
        if (weekday == 1 or weekday == 3):
            self.veronica()

    def otter(self):
        self.todo("* TODO Move the messages from visual voice mail to otter")

    def joblinks(self):
        self.write("(brad-job-browse)")
        
    def todo(self,arg):
        self.write(arg)
        self.insertScheduleDeadline()
        
    def laundry(self):
        if (weekday == 5):
            self.todo("* TODO Laundry [/]\n** TODO Darks [/]\n*** TODO Wash Darks\n*** TODO Dry Darks\n*** TODO Put darks away\n** TODO Colors [/]\n*** TODO Wash colors\n*** TODO Dry colors\n*** TODO Put colors away\n** TODO Whites [/]\n*** TODO Wash whites\n*** TODO Dry whites\n*** TODO Put whites away\n")
            
    def novena(self):
        if (weekday == 2):
            self.write("* TODO Attend Novena")
            self.insertSchedule("18:30")
            self.properties("120")
            self.insertDeadline()
            
    def close(self):
        self.file.close()
        
    def link(self,name,link):
        self.write("[["+link+"]["+name+"]]")

    def joblink(self):
        self.link("jobs","c:/Users/bradl/OneDrive/Documents/Jobs/jobs.org")

    def job(self,title):
        self.todo(title)
        self.joblink()
        
    def youtube(self):
        self.todo("* TODO Make Youtube Video\n** Prepare/Record Script\n:PROPERTIES:\n:Effort: 30\n:END:\n** Record Video\n:PROPERTIES:\n:Effort: 30\n:END:\n** Edit Video\n:PROPERTIES:\n:Effort: 30\n:END:\n** Publish Video\n:PROPERTIES:\n:Effort: 30\n:END:\n")

    def header(self):
        self.file.write("* GOAL BRING IN $2500 A MONTH INCOME\n")
        self.file.write("* TODO PICK THE THING TO DO FOR THE DAY\n")
        for i in range(50):
            self.write("** TODO Pick thing to do number "+str(i))
        self.file.write("* HEADER\n")
        self.file.write("; -*- mode: Org; eval: (auto-fill-mode 1); -*-\n") 
        self.file.write("#+STARTUP: indent\n")
        self.file.write("#+TODO: TODO PRAY(@) DOING CURRENT | DONE\n")
        self.file.write("#+TODO: JOB JOB_MOVE_TO_JOBS ACTIVE | APPLIED REJECTED\n")
        self.file.write("#+TODO: CALL | CALLED\n")
        self.file.write("#+TODO: ACCEPTED RATE RTR CONFIRMED INTERVIEW INTERVIEWED | REJECTED JOB_OFFER\n")
        self.file.write("#+TODO: PRAY PRAYING | PRAYED\n")
        self.file.write("#+TODO: EMAIL READ_EMAIL | REPLIED\n")
        self.file.write("#+TODO: FIND_NEXT_PAPER PUT_PAPER_IN_SCANNER SCAN | SCANNED\n")
        self.file.write("#+TODO: PRAY_FOR_PHONE_CALL PREPARE_TO_CALL WRITE_SCRIPT CALLING | LEFT_A_MESSAGE CALL_BACK_AGAIN_LATER BUSY_CALL_LATER CALLED CALLED_SUBMITTED\n")

    def write(self,theline):
        self.file.write(theline+"\n")

    def contactcompanies(self):
        for i in range(5):
            self.write("* TODO Find remote company "+str(i))
            self.insertScheduleDeadline()
        for i in range(5):
            self.write("* TODO Find remote recruiter "+str(i))
            self.insertScheduleDeadline()
    
    def insertScheduleDeadline(self,*argv):
        hasMultiple=False
        for arg in argv:  
                hasMultiple=True
        self.file.write("DEADLINE: ")
        self.file.write("<"+str(theyear)+"-"+str(themonth)+"-"+str(theday)+">")
        self.file.write("\n")
        if (hasMultiple):
                self.properties(argv)
        else:
                self.properties()
        self.file.write("SCHEDULED: ")
        self.file.write("<"+str(theyear)+"-"+str(themonth)+"-"+str(theday)+">")
        self.file.write("\n")
        
    def properties(self,*argv):
        hasMultiple=False
        for arg in argv:  
            hasMultiple=True
            theProperty=arg
        if (hasMultiple):
            self.write(":PROPERTIES:\n:Effort: "+str(theProperty)+"\n:END:")
        else:
            self.write(":PROPERTIES:\n:Effort: 30\n:END:")

    def insertDeadline(self,*argv):
        hasMultiple=False
        for arg in argv:  
                hasMultiple=True
                theDeadline=arg
        if (hasMultiple):
                self.file.write("DEADLINE: ")
                self.file.write("<"+str(theyear)+"-"+str(themonth)+"-"+str(theday)+" "+theDeadline+" >")
                self.file.write("\n")
        else:
                self.file.write("DEADLINE: ")
                self.file.write("<"+str(theyear)+"-"+str(themonth)+"-"+str(theday)+">")
                self.file.write("\n")

    def insertSchedule(self,*argv):
        hasMultiple=False
        for arg in argv:  
                hasMultiple=True
                theschedule=arg
        self.file.write("SCHEDULED: ")
        if (hasMultiple):
                self.write("<"+str(theyear)+"-"+str(themonth)+"-"+str(theday)+" "+theschedule+">")
        else:
                self.write("<"+str(theyear)+"-"+str(themonth)+"-"+str(theday)+">")

    def prayers(self):
        self.todo("* PRAY to your guardian angel")
        self.write("Angel of God\nMy Guardian dear\nTo whom Gods love commits me here\nEver this day be at my side\nTo light and guard\nrule and guide.\n")
        self.todo("* PRAY the verses of scripture from the Mass\n")
        self.todo("* PRAY Consecration to Mary\n")
        self.write("[[https://keep.google.com/#NOTE/1iWfdLt4Ony5dvvh4lYEJ1uIjJcdW2CZxvOp0VcdPsB8IAqC6FYblXw_kL3v6Ln8PZew][Consecration to Mary]]")
        self.todo("* PRAY Apostleship of Prayer\n")
        self.write("[[https://keep.google.com/#NOTE/1vnUIHv2W99XSWwIRB8Lke_mP9NAn54uR27ggHSHDJfi1--70H-LlP9WjbCCX][The Apostleship of Prayer]]")
        self.write("1. [ ] God, our Father,")
        self.write("2. [ ] I offer You my day.")
        self.write("3. [ ] I offer You my prayers, thoughts, words, actions, joys, and sufferings")
        self.write("4. [ ] in union with the Heart of Jesus,")
        self.write("5. [ ] who continues to offer Himself")
        self.write("6. [ ] in the Eucharist")
        self.write("7. [ ] for the salvation of the world.")
        self.write("8. [ ] May the Holy Spirit, Who guided Jesus,")
        self.write("9. [ ] be my guide and my strength today")
        self.write("10. [ ] so that I may witness to your love.")
        self.write("11. [ ] With Mary,")
        self.write("12. [ ] the mother of our Lord")
        self.write("13. [ ] and the Church,")
        self.write("14. [ ] I pray for all Apostles of Prayer")
        self.write("15. [ ] and for the prayer intentions proposed")
        self.write("16. [ ] by the Holy Father this month.")
        self.write("17. [ ] Amen.")
        self.todo("* PRAY The Litany of Humility")
        self.todo("* PRAY to Saint Dymphna\n")
        self.todo("* PRAY Litany of the Sick\n")
        self.todo("* PRAY your Prayer Requests\n")
        self.todo("[[file:c:/Users/bradl/Dropbox/15 Prayers/prayerrequests.org][Prayer Requests]]\n")
        self.rosary()
        self.loh()        


    def flexjobs(self):
            self.write("* TODO search flexjobs for remote java positions \n")
            self.write("[[https://www.flexjobs.com/members][Flexjobs]]\n")
            self.write("[[https://www.flexjobs.com/search?search=remote+java+developer&exclude=&location=&country=&jobtypes%5B%5D=Freelance&schedule%5B%5D=Flexible+Schedule&tele_level%5B%5D=All+Telecommuting&will_travel%5B%5D=&accolade=][Remote Freelance Flexible Hours]]\n")

    def church(self):
        self.todo("* TODO Get dressed for church")
        self.todo("* TODO Go to church\n")
    
    def rosary(self):
        self.file.write("* PRAY the Rosary [/]\n")
        self.file.write("** PRAY the Rosary Prefix [/]\n")
        self.initialhailmary()
        self.file.write("** PRAY the Rosary Joyful Mysteries [/]\n")
        self.file.write("*** PRAY the Rosary Joyful Mystery The Incarnation [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Joyful Mystery The Visitation [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Joyful Mystery The Nativity [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Joyful Mystery The Presentation [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Joyful Mystery Finding Jesus in the Temple [/]\n")
        self.hailmary()
        self.file.write("** PRAY the Rosary Lumionous Mysteries [/]\n")
        self.file.write("*** PRAY the Rosary Luminous Mystery The Baptism of Jesus [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Luminous Mystery The Wedding at Cana [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Luminous Mystery Preaching the Gospel [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Luminous Mystery The Transfiguration [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Luminous Mystery The Eucharist [/]\n")
        self.hailmary()
        self.file.write("** PRAY the Rosary Sorrowful Mysteries [/]\n")
        self.file.write("*** PRAY the Rosary Sorrowful Mystery The Agony in the Garden [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Sorrowful Mystery The Scourging [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Sorrowful Mystery The Crowining with Thorns [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Sorrowful Mystery Carrying the Cross [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Sorrowful Mystery The Crucifixion [/]\n")
        self.hailmary()
        self.file.write("** PRAY the Rosary Glorious Mysteries [/]\n")
        self.file.write("*** PRAY the Rosary Glorious Mystery The Resurrection [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Glorious Mystery The Ascension [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Glorious Mystery The Descent of the Holy Spirit [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Glorious Mystery The Assumption of Mary [/]\n")
        self.hailmary()
        self.file.write("*** PRAY the Rosary Glorious Mystery The Crowining of Mary [/]\n")
        self.hailmary()

    def loh(self):
        self.file.write("* PRAY the liturgy of the hours Invitatory\n")
        self.insertSchedule(" 06:00")
        self.properties()
        self.insertDeadline()
        self.file.write("[[https://www.divineoffice.org][Divine Office]]\n")
        self.file.write("* PRAY the liturgy of the hours Office of Readings\n")
        self.file.write("SCHEDULED:")
        self.file.write("<"+str(theyear)+"-"+str(themonth)+"-"+str(theday)+">")
        self.file.write("\n")
        self.properties()
        self.insertDeadline()
        self.file.write("* PRAY the liturgy of the hours Morning Prayer 6:00 p.m.\n")
        self.insertSchedule(" 07:00")
        self.properties()
        self.insertDeadline()
        self.file.write("[[https://www.divineoffice.org][Divine Office]]\n")
        self.file.write("* PRAY the liturgy of the hours Midmorning Prayer 9:00 a.m.\n")        
        self.insertSchedule(" 09:00")
        self.file.write("* PRAY the liturgy of the hours Midday Prayer 12:00 p.m.\n")
        self.insertSchedule(" 12:00")
        self.properties()
        self.insertDeadline()
        self.file.write("[[https://www.divineoffice.org][Divine Office]]\n")
        self.file.write("* PRAY the liturgy of the hours Midafternoon Prayer 3:00 p.m.\n")
        self.insertSchedule(" 15:00")
        self.file.write("[[https://www.divineoffice.org][Divine Office]]\n")
        self.file.write("* PRAY the liturgy of the hours Evening Prayer\n")
        self.insertSchedule(" 19:00")
        self.properties()
        self.insertDeadline()
        self.file.write("[[https://www.divineoffice.org][Divine Office]]\n")
        self.file.write("* PRAY the liturgy of the hours Night Prayer\n")
        self.properties()
        self.insertDeadline()
        self.insertSchedule(" 22:00")
        self.file.write("[[https://www.divineoffice.org][Divine Office]]\n")







    def theourfather(self):
        self.file.write("- [ ] Our Father, [/]\n")
        self.file.write(" - [ ] Our Father, \n")
        self.file.write(" - [ ] Who art in Heaven, \n")
        self.file.write(" - [ ] hallowed be Thy name; \n")
        self.file.write(" - [ ] Thy Kingdom come,\n")
        self.file.write(" - [ ] Thy will be done \n")
        self.file.write(" - [ ] on earth as it is in Heaven. \n")
        self.file.write(" - [ ] Give us this day \n")
        self.file.write(" - [ ] our daily bread; \n")
        self.file.write(" - [ ] and forgive us our trespasses \n")
        self.file.write(" - [ ] as we forgive those who trespass against us; \n")
        self.file.write(" - [ ] and lead us not into temptation, \n")
        self.file.write(" - [ ] but deliver us from evil. \n")
        self.file.write(" - [ ] Amen. \n")


        
    def theglorybe(self):
        self.file.write("- [ ] Glory be [/]\n")
        self.file.write(" - [ ] Glory be to the Father\n")
        self.file.write(" - [ ] and to the Son and to the Holy Spirit. \n")
        self.file.write(" - [ ] As it was in the beginning \n")
        self.file.write(" - [ ] is now, \n")
    
    def thehailmary(self):
        self.file.write("- [ ] Hail Mary [/]\n")
        self.file.write(" - [ ] Hail Mary\n")
        self.file.write(" - [ ] Full of Grace\n")
        self.file.write(" - [ ] the Lord is with thee.\n")
        self.file.write(" - [ ] Blessed are thou among women \n")
        self.file.write(" - [ ] and blessed is the fruit of thy womb Jesus.\n")
        self.file.write(" - [ ] Holy Mary Mother of God,\n")
        self.file.write(" - [ ] pray for us sinners now \n")
        self.file.write(" - [ ] and at the hour of our death\n")
        self.file.write(" - [ ] Amen.\n")
    
    def hailmary(self):
        self.insertScheduleDeadline()
        self.theourfather()
        for number in range(10):
            self.thehailmary()
            self.theglorybe()
            self.fatimaprayer()

    def veronica(self):
        self.file.write("* TODO Take Veronica to school\n")
        self.insertSchedule("10:30")
        self.properties("120")
        self.insertDeadline("12:30")
        self.file.write("* TODO Pick up Veronica from school\n")
        self.insertSchedule("12:30")
        self.properties("120")
        self.insertDeadline("13:30")

    def fatimaprayer(self):
        self.file.write("- [ ] Fatima Prayer [/]\n")
        self.file.write(" - [ ] Oh my Jesus\n")
        self.file.write(" - [ ] Forgive us our sins\n")
        self.file.write(" - [ ] Save us from the fires of hell\n")
        self.file.write(" - [ ] And lead all souls to heaven\n")
        self.file.write(" - [ ] especially those in most need of thy mercy, can you say Muslims\n")

        
        

    def initialhailmary(self):
        self.insertScheduleDeadline()
        self.file.write("- [ ] Recite the Apostles Creed\n")
        self.theourfather()
        for number in range(3):
                self.thehailmary()
        self.theglorybe()
        self.fatimaprayer()

    def isfile(self):
        return os.path.exists(self.filename)

    def getmore(self):
        from tkinter import simpledialog

        self.newtodo=simpledialog.askstring("Input","Enter any more things you want to get done today?",
                                        parent=win)
        while (self.newtodo != ""):
                self.todo("* TODO "+self.newtodo+"\n")
                self.newtodo = simpledialog.askstring("Input","Enter any more things you want to get done today?",
                                                      parent=win)


def isfile2():
    return os.path.exists(filename2)

def isfile():
    return os.path.exists(filename)

        
        
        
now = datetime.datetime.now()
theyear = now.year
theday = '%02d' % now.day
themonth = '%02d' % now.month
from datetime import date
weeknumber = '%02d' % date.today().isocalendar()[1]
weekday = date.today().weekday()
filename="C:/Users/bradl/OneDrive/Documents/Journal/"+str(theyear)+str(weeknumber)+".org"
filename2="C:/Users/bradl/OneDrive/Documents/Journal/"+str(theyear)+str(themonth)+str(theday)+".org"

def makeweeklyfile():
    if isfile():
        print(filename+" exists")
    else:
        print ("writing "+filename)
        theweeklyfile = thefile(filename)
        theweeklyfile.header()
        theweeklyfile.contactcompanies()
        theweeklyfile.close()

    
def makedaily():
    if (isfile2()):
        print(filename2 + " exists")
    else:
        print ("writing "+filename2)
        thedailyfile=thefile(filename2)
        thedailyfile.header()
        thedailyfile.getmore()
        thedailyfile.otter()
        thedailyfile.laundry()
        thedailyfile.todo("* TODO Go for walk number 1\n")
        thedailyfile.todo("* TODO Go for walk number 2\n")
        thedailyfile.todo("* TODO Go for walk number 3\n")
        thedailyfile.todo("* TODO Increase hacker rank\n")
        thedailyfile.todo("* TODO Get started with developing spring\n")
        thedailyfile.link("Org file for spring boot","c:/Users/bradl/OneDrive/Documents/Projects/SpringSysRefCursor/SpringSysRefCursor.org")

        thedailyfile.write("* TODO Do linkedin courses linkedin for remote jobs\n")
        thedailyfile.insertSchedule("9:40")
        thedailyfile.properties("120")
        thedailyfile.insertDeadline("10:30")
        thedailyfile.write("(find-file \"c:/Users/bradl/OneDrive/Downloads/LinkedIn/courses.org\" t)")
        thedailyfile.write("[[https://www.linkedin.com/learning/me?trk=nav_neptune_learning][LinkedIn Learning]]")
        thedailyfile.todo("* TODO Try to sell something of mine on facebook.\n")
        thedailyfile.todo("* TODO Try to look for a new car for Veronica and Nadia.\n")
        thedailyfile.write("(find-file \"c:/Users/bradl/OneDrive/Documents/Projects/CarForVeronicaAndNadia/CarForVeronicaAndNadia.org\" t)\n")
        thedailyfile.todo("* TODO Do Lamas Project\n")
        thedailyfile.write("(find-file \"c:/Users/bradl/OneDrive/Documents/Projects/QubainFamilyTree/QubainFamilyTree.org\" t)")
        for i in range(10):
            thedailyfile.todo("* TODO Find Catholic job "+str(i))
        for i in range(4):
            thedailyfile.todo("* TODO Find Remote job "+str(i))
            thedailyfile.joblinks()
        thedailyfile.todo("* TODO Contact someone I know for a job")
        thedailyfile.contactcompanies()
        thedailyfile.todo("* TODO Work on your own website on google sites")
        thedailyfile.link("Google Sites","http://sites.google.com")
        thedailyfile.todo("* TODO Submit content for bradleesargent.wordpress.com")
        thedailyfile.todo("* TODO Submit content for bradthecathoilic.wordpress.com")
        thedailyfile.todo("* TODO Call friends")
        thedailyfile.todo("* TODO Get browse to work")
        thedailyfile.appointments()
        thedailyfile.novena()
        thedailyfile.write("* TODO Go to adoration")
        thedailyfile.insertSchedule("20:40")
        thedailyfile.properties("120")
        thedailyfile.insertDeadline("22:30")
        thedailyfile.write("* TODO Go to Mass")
        thedailyfile.insertSchedule("11:00")
        thedailyfile.properties("120")
        thedailyfile.insertDeadline("22:30")
        if (weekday == 6):
            thedailyfile.church()
        else:
            thedailyfile.job("* TODO Check email for remote jobs")
            thedailyfile.write("[[http://inbox.google.com/search/remote][Email]]")
            thedailyfile.job("* TODO Check linkedin for remote jobs")
            thedailyfile.write("[[https://www.linkedin.com/jobs/search/?keywords=%23remote%20%23java][Linkedin]]\n")
            thedailyfile.job("* TODO Check careerbuilder for remote jobs\n")
            thedailyfile.job("* TODO Check remote.io for remote jobs")
            thedailyfile.job("* TODO Check twitter for remote jobs")
            thedailyfile.write("[[https://twitter.com/search?src=typd&q=%23remote%20%23java][Remote Jobs on Twitter]]")
            thedailyfile.job("* TODO Check indeed for remote jobs\n")
            thedailyfile.write("[[https://www.indeed.com/q-Remote-Java-Developer-jobs.html][Indeed Remote Jobs]]\n")
            thedailyfile.job("* TODO Handle Phone Calls\n")
            thedailyfile.write("[[file:c:/Users/bradl/OneDrive/Documents/Jobs/phone.org][Remote Phone Calls]]")
            thedailyfile.todo("* TODO Handle This Weeks Weekly Applications\n")
            thedailyfile.write("[[file:"+filename+"][Weekly Applications]]")
            thedailyfile.todo("* TODO Contact Oscar Doctor [/]")
            thedailyfile.write("[[https://www.hioscar.com/auth/login?next=%2Fwelcome%2Fchecklist%2F][Oscar Insurance]]")
            thedailyfile.job("* TODO Check phone message for remote jobs [/]")
            thedailyfile.write("[[file:c:/Users/bradl/OneDrive/Documents/Jobs/phone.org][remote phone calls]]")


        thedailyfile.todo("* TODO Lunch\n")
        thedailyfile.todo("** TODO Prepare Lunch\n")
        thedailyfile.write("** TODO Clean Lunch Dishes\n")
        thedailyfile.write("* TODO Dinner\n")
        thedailyfile.todo("* TODO Get Dressed\n")
        thedailyfile.todo("* TODO Morning Rosary Nap\n")
        thedailyfile.todo("* TODO Afternoon Rosary Nap\n")
        thedailyfile.youtube()
        thedailyfile.write("* TODO Read a book\n")
        thedailyfile.insertScheduleDeadline(60)
        thedailyfile.write("[[http://read.amazon.com][Read a book]]\n")
        for i in range(7):
                thedailyfile.todo("* TODO Drink water cup "+str(i)+"\n")
        thedailyfile.write("[[file:"+filename+"][Weekly Applications]]\n")
        for i in range(7):
                thedailyfile.todo("* FIND_NEXT_PAPER Scan paper "+str(i)+"\n")
        
        thedailyfile.todo("* TODO Rome Reports\n")
        thedailyfile.write("[[https://www.romereports.com/en/][Rome Reports]]\n")
        thedailyfile.prayers()


def runme():
    if (weekday == 0):
        makeweeklyfile()
    makedaily()
    theinitfile="c:/Users/bradl/OneDrive/Startup/python/.emacs"
    theinit=open(theinitfile,"w")
    theinit.write("(find-file \""+filename+"\" t)\n")
    theinit.write("(find-file \""+filename2+"\" t)\n")
    theinit.close()
    batchfile=open("after.bat","w")
    batchfile.write("@ECHO ON\n")
    batchfile.write("runemacs\n")
    batchfile.close()
    exit()




def shutdown():
    thecmd="shutdown"
    thearg="/s"
    commands=[thecmd,thearg]
    subprocess.Popen(commands)

def logout():
    thecmd="shutdown"
    thearg="/l"
    commands=[thecmd,thearg]
    subprocess.Popen(commands)

def deleteweekly():
    os.remove(filename)
    mbox.showinfo(filename + "\ndeleted")

def deletedaily():
    os.remove(filename2)
    mbox.showinfo(filename2 + "\ndeleted")

def freemind():
    batchfile=open("after.bat","w")
    batchfile.write("@ECHO ON\n")
    batchfile.write("freemind\n")
    batchfile.close()
    exit()

def powershell():
    batchfile=open("after.bat","w")
    batchfile.write("@ECHO ON\n")
    batchfile.write("c:/windows/system32/WindowsPowerShell/v1.0/PowerShell_ISE.exe\n")
    batchfile.close()
    exit()

def intellij():
    batchfile=open("after.bat","w")
    batchfile.write("@ECHO ON\n")
    batchfile.write("\"C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2018.2.5/bin/idea64.exe\"\n")
    batchfile.close()
    exit()

def pycharm():
    batchfile=open("after.bat","w")
    batchfile.write("@ECHO ON\n")
    batchfile.write("\"C:/Program Files (x86)/JetBrains/PyCharm Community Edition 2018.3.3/bin/pycharm64.exe\"\n")
    batchfile.close()
    exit()


def eclipse():
    batchfile=open("after.bat","w")
    batchfile.write("@ECHO ON\n")
    batchfile.write("\"C:/Users/bradl/eclipse/jee-photon/eclipse/eclipse.exe\"\n")
    batchfile.close()
    exit()



fileMenu = Menu(menuBar,tearoff=0)
fileMenu.add_command(label="Emacs",command=runme)
menuBar.add_cascade(label="File",menu=fileMenu)

filenameframe = ttk.LabelFrame(win,text='Filenames')
filenameframe.grid(column=0,row=therow,padx=8,pady=4)

therow = therow + 1
alabel = ttk.Label(filenameframe,text=filename)
alabel.grid(sticky=tk.W,row=therow,column=1)

therow = therow + 1

blabel = ttk.Label(filenameframe,text=filename2)
blabel.grid(sticky=tk.W,row=therow,column=1)

therow = therow + 1

deleteframe = ttk.LabelFrame(win,text='Delete')
deleteframe.grid(column=0,row=therow,padx=8,pady=4)
therow = therow + 1
actiondeleteweekly  = ttk.Button(deleteframe,text = "Weekly file:"+filename, command=deleteweekly)
actiondeleteweekly.grid(row=therow,sticky=tk.W,column=1)

therow = therow + 1

actiondeletedaily  = ttk.Button(deleteframe,text = "Daily file:"+filename2, command=deletedaily)
actiondeletedaily.grid(sticky=tk.W,row=therow,column=1)

therow = therow + 1

runframe = ttk.LabelFrame(win,text='Run')
runframe.grid(column=0,row=therow,padx=8,pady=4)
therow = therow + 1
action = ttk.Button(runframe,text = "Emacs!", command=runme)
action.grid(sticky=tk.W,row=therow)
action.focus()

therow = therow + 1

actionfreemind = ttk.Button(runframe,text = "Freemind", command=freemind)
actionfreemind.grid(sticky=tk.W,row=therow)

therow = therow + 1

actionpowershell = ttk.Button(runframe,text = "Powershell", command=powershell)
actionpowershell.grid(sticky=tk.W,row=therow)


therow = therow + 1

actionintellij = ttk.Button(runframe,text = "Intellij", command=intellij)
actionintellij.grid(sticky=tk.W,row=therow)


therow = therow + 1
actionpycharm = ttk.Button(runframe,text = "pycharm", command=pycharm)
actionpycharm.grid(sticky=tk.W,row=therow)

therow = therow + 1

actioneclipse= ttk.Button(runframe,text = "Eclipse", command=eclipse)
actioneclipse.grid(sticky=tk.W,row=therow)


therow = therow + 1

actiondown = ttk.Button(runframe,text = "Shutdown", command=shutdown)
actiondown.grid(sticky=tk.W,row=therow)

therow = therow + 1

actionlogout = ttk.Button(runframe,text = "Logout", command=logout)
actionlogout.grid(sticky=tk.W,row=therow)

win.mainloop()


