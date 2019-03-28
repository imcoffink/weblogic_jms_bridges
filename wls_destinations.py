# Configure WL1 <> WL2 JMS Bridge Destinations

import sys
import os
from java.lang import System
from bridges_conf import *

import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "u:p:c:j:k:l:", ["wl1user=", "wl1pass=", "wl1conn=", "wl2user=", "wl2pass=", "wl2conn="])
except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(2)

wl1user=''
wl1pass=''
wl1conn=''
wl2user=''
wl2pass=''
wl2conn=''

for opt, arg in opts:
    if opt == "-u":
        wl1user=arg
    elif opt == "-p":
        wl1pass=arg
    elif opt == "-c":
        wl1conn=arg
    elif opt == "-j":
		wl2user=arg
	elif opt == "-k":
		wl2pass=arg
	elif opt == "-l":
		wl2conn=arg

if wl1user == "":
    print "ERROR: Missing WL1 User parameter."
        sys.exit(2)
if wl1pass == "":
    print "ERROR: Missing WL1 Password parameter."
        sys.exit(2)
if wl1conn == "":
    print "ERROR: Missing WL1 Connection parameter."
        sys.exit(2)
if wl2user == "":
    print "ERROR: Missing WL2 User parameter."
        sys.exit(2)
if wl2pass == "":
    print "ERROR: Missing WL2 Password parameter."
        sys.exit(2)
if wl2conn == "":
    print "ERROR: Missing WL2 Connection parameter."
    sys.exit(2)

print 'All parameters are filled!'

print 'Creating JMS Bridge Destinations on WL Server 1'
connect(wl1user,wl1pass,wl1conn)
edit()
startEdit()

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl1to2srcdst)
if(ref == None):
	cmo.createJMSBridgeDestination("%s" % wl1to2srcdst)
	cd("/JMSBridgeDestinations/%s" % wl1to2srcdst)
	set('AdapterJNDIName',"%s" % adptjndinm)
	set('InitialContextFactory',"%s" % initctxtfctry)
	set('ConnectionFactoryJNDIName',"%s" % connfctryjndinm)
	set('DestinationJNDIName',"%s" % wl1to2srcdstjndiname)
else:
    print("%s already created." % wl1to2srcdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl1to2tgtdst)
if(ref == None):
	cmo.createJMSBridgeDestination("%s" % wl1to2tgtdst)
	cd("/JMSBridgeDestinations/%s" % wl1to2tgtdst)
	set('AdapterJNDIName',"%s" % adptjndinm)
	set('InitialContextFactory',"%s" % initctxtfctry)
	set('ConnectionFactoryJNDIName',"%s" % connfctryjndinm)
	set('DestinationJNDIName',"%s" % wl1to2tgtdstjndiname)
else:
    print("%s already created." % wl1to2tgtdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl2to1srcdst)
if(ref == None):
	cmo.createJMSBridgeDestination("%s" % wl2to1srcdst)
	cd("/JMSBridgeDestinations/%s" % wl2to1srcdst)
	set('AdapterJNDIName',"%s" % adptjndinm)
	set('InitialContextFactory',"%s" % initctxtfctry)
	set('ConnectionFactoryJNDIName',"%s" % connfctryjndinm)
	set('DestinationJNDIName',"%s" % wl2to1srcdstjndiname)
else:
    print("%s already created." % wl2to1srcdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl2to1tgtdst)
if(ref == None):
	cmo.createJMSBridgeDestination("%s" % wl2to1tgtdst)
	cd("/JMSBridgeDestinations/%s" % wl2to1tgtdst)
	set('AdapterJNDIName',"%s" % adptjndinm)
	set('InitialContextFactory',"%s" % initctxtfctry)
	set('ConnectionFactoryJNDIName',"%s" % connfctryjndinm)
	set('DestinationJNDIName',"%s" % wl2to1tgtdstjndiname)
else:
    print("%s already created." % wl2to1tgtdst)

activate()

print 'Exiting....'

disconnect()

print 'Creating JMS Bridge Destinations on WL Server 2'
connect(wl2user,wl2pass,wl2conn)
edit()
startEdit()

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl1to2srcdst)
if(ref == None):
	cmo.createJMSBridgeDestination("%s" % wl1to2srcdst)
	cd("/JMSBridgeDestinations/%s" % wl1to2srcdst)
	set('AdapterJNDIName',"%s" % adptjndinm)
	set('InitialContextFactory',"%s" % initctxtfctry)
	set('ConnectionFactoryJNDIName',"%s" % connfctryjndinm)
	set('DestinationJNDIName',"%s" % wl1to2srcdstjndiname)
else:
    print("%s already created." % wl1to2srcdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl1to2tgtdst)
if(ref == None):
	cmo.createJMSBridgeDestination("%s" % wl1to2tgtdst)
	cd("/JMSBridgeDestinations/%s" % wl1to2tgtdst)
	set('AdapterJNDIName',"%s" % adptjndinm)
	set('InitialContextFactory',"%s" % initctxtfctry)
	set('ConnectionFactoryJNDIName',"%s" % connfctryjndinm)
	set('DestinationJNDIName',"%s" % wl1to2tgtdstjndiname)
else:
    print("%s already created." % wl1to2tgtdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl2to1srcdst)
if(ref == None):
	cmo.createJMSBridgeDestination("%s" % wl2to1srcdst)
	cd("/JMSBridgeDestinations/%s" % wl2to1srcdst)
	set('AdapterJNDIName',"%s" % adptjndinm)
	set('InitialContextFactory',"%s" % initctxtfctry)
	set('ConnectionFactoryJNDIName',"%s" % connfctryjndinm)
	set('DestinationJNDIName',"%s" % wl2to1srcdstjndiname)
else:
    print("%s already created." % wl2to1srcdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl2to1tgtdst)
if(ref == None):
	cmo.createJMSBridgeDestination("%s" % wl2to1tgtdst)
	cd("/JMSBridgeDestinations/%s" % wl2to1tgtdst)
	set('AdapterJNDIName',"%s" % adptjndinm)
	set('InitialContextFactory',"%s" % initctxtfctry)
	set('ConnectionFactoryJNDIName',"%s" % connfctryjndinm)
	set('DestinationJNDIName',"%s" % wl2to1tgtdstjndiname)
else:
    print("%s already created." % wl2to1tgtdst)

activate()

print 'Exiting....'

disconnect()

exit()
