if ".%1"=="." goto doall
goto %1

:doall
python AddTags.py

:end
cd \Users\bradl\OneDrive\Startup\python

