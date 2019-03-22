$Server = Read-Host -Prompt 'Waiting to start...'
set-location c:/Users/bradl/OneDrive/Startup/python/
write-host brads python batch file
etags c:/Users/bradl/OneDrive/dropbox/.emacs.d/brad.el *.py
# echo starting freemind
python freemind.py
# python homepage.py
python intellij.py
# python journal.py
# emacs book.py
python book.py
python shutdown.py
get-command etags
