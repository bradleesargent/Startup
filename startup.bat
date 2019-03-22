@echo off
set thecmd=start CMD /K 
set thedir=C:\Users\bradl\OneDrive\Startup\bin\
echo %thecmd%
echo %thedir%
mode 1000
IF ".%1"=="." GOTO DOALL
GOTO %1


:DOALL
:python
cls
choice /C 1234567890SCV /M "V)isual Studio Code,C)md S)hutdown 0) Netbeans, 1) Powershell, 2) intellij, 3) Pycharm, 4) Eclipse, 5) Python-start, 6) Emacs, 7) Edit this, 8) Jdeveloper, 9) Word"
set thetest=%ERRORLEVEL%
echo choice%thetest%
pause
goto choice%thetest%



:choice1
:choice2
:choice3
:choice4
:choice5
:choice7
:choice8
:choice9
:choice10
:choice11
:choice12
:choice13
%thecmd% %thedir%choice%thetest%.bat
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


