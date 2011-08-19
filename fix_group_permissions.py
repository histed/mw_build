#!/usr/bin/env python
#
#  Set up permissions so that anyone in the admin group can install MWorks components
#
#  Must run this with sudo
#
#  histed 100804

import os, sys

paths = [ "/Library/Application Support/MWorks",
          "/Library/Frameworks/MWorksCore.framework", 
          "/Library/Frameworks/MWorksCocoa.framework", 
          "/Applications/MWClient.app",
          "/Applications/MWServer.app",
          "/Applications/MWEditor.app" ]

if not (os.getuid() == 0):
    print "Error: must run this script with sudo"
    sys.exit(-1)

for p in paths:
    print "Fixing groups and permissions in %s" % p
    os.system('find "%s" -print0 | xargs -0 chgrp admin' % p)
    os.system('find "%s" -type f -print0 | xargs -0 chmod g+rw' % p)
    os.system('find "%s" -type d -print0 | xargs -0 chmod g+rwx' % p)

    print ("Fixing owners in %s" % p)
    os.system('find "%s" -print0 | xargs -0 chown %s' % (p, os.getenv('SUDO_USER')))

print "Done."
