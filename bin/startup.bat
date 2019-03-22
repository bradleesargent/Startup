@echo ON

:choice2
start  CMD /K "C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2018.2.5\bin\idea64.exe"
goto python

:choice3
start  CMD /K "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2018.3.3\bin\pycharm64.exe"
goto python

:choice4
start  CMD /K "C:\Users\bradl\eclipse\jee-photon\eclipse\eclipse.exe"
goto python

:choice5
cd \Users\bradl\OneDrive\Startup\python
call dopython.bat
GOTO python

:choice6
start  CMD /K "C:\Users\bradl\OneDrive\Downloads\Emacs\emacs-26.1-x86_64\bin\runemacs.exe"
GOTO python

:choice7
"C:\Users\bradl\AppData\Local\Programs\Microsoft VS Code\Code.exe" "C:\Users\bradl\OneDrive\Startup\startup.bat"
pause
start cmd /k "C:\Users\bradl\OneDrive\Startup\startup.bat"
goto end

:choice8
start  CMD /K C:\Oracle\Middleware\Oracle_Home\jdeveloper\jdeveloper.exe
goto python

:choice9
start  CMD /K "C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
goto python


:choice10
start CMD /K C:\Users\bradl\OneDrive\Downloads\Netbeans\netbeans\bin\netbeans64.exe
goto python

:choice11
call shutdown.bat
GOTO END

:choice12
start cmd
goto python

:choice13
start cmd /k "C:\Users\bradl\AppData\Local\Programs\Microsoft VS Code\Code.exe"
goto python

:PROGRAMS
start CMD /K  "C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2018.2.5\bin\idea64.exe"
start CMD /K "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2018.3.3\bin\pycharm64.exe"
start CMD /K "C:\Users\bradl\eclipse\jee-photon\eclipse\eclipse.exe"
GOTO END


:PW
start %windir%\system32\WindowsPowerShell\v1.0\PowerShell_ISE.exe
GOTO END

:PY
start CMD /K "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 2018.3.3\bin\pycharm64.exe"
GOTO END

:EM
runemacs dopython.bat
call dopython.bat
GOTO END


:H
ECHO PW START POWERSHELL ISE
ECHO PY START PYTHON
ECHO EM START EMACS
ECHO CMD START CMD
GOTO END

:CMD
START CMD
GOTO END

:END


