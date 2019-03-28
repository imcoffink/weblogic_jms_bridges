# Activate WL1 <> WL2 Bridges

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

print 'Configuring JMS Bridges Integration in WL Server 1'
connect(wl1user,wl1pass,wl1conn)
edit()
startEdit()

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl1to2srcdst)
if(ref != None):
    cd("/JMSBridgeDestinations/%s" % wl1to2srcdst)
    set('ConnectionURL','')
    set('UserName','')
    set('UserPassword','')
    print("%s has been configured." % wl1to2srcdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl1to2tgtdst)
if(ref != None):
    cd("/JMSBridgeDestinations/%s" % wl1to2tgtdst)
    set('ConnectionURL', wl2conn)
    set('UserName', wl2user)
    set('UserPassword', wl2pass)
	set('InitialContextFactory',initctxtfctry)
	set('ConnectionFactoryJNDIName',connfctryjndinm)
	set('DestinationJNDIName',wl1to2tgtdstjndiname)
    print("%s has been configured." % wl1to2tgtdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl2to1srcdst)
if(ref != None):
    cd("/JMSBridgeDestinations/%s" % wl2to1srcdst)
    set('ConnectionURL', wl2conn)
    set('UserName', wl2user)
    set('UserPassword', wl2pass)
	set('InitialContextFactory',initctxtfctry)
	set('ConnectionFactoryJNDIName',connfctryjndinm)
	set('DestinationJNDIName',wl2to1srcdstjndiname)
    print("%s has been configured." % wl2to1srcdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl2to1tgtdst)
if(ref != None):
    cd("/JMSBridgeDestinations/%s" % wl2to1tgtdst)
    set('ConnectionURL', '')
    set('UserName','')
    set('UserPassword','')
    print("%s has been configured." % wl2to1tgtdst)

cd('/')
cd("/MessagingBridges/%s" % wl1to2bridge)
set('Started', true)
cd("/MessagingBridges/%s" % wl2to1bridge)
set('Started', true)

activate()

print 'Exiting....'

disconnect()

print 'Configuring JMS Bridges Integration in WL Server 2'
connect(wl2user,wl2pass,wl2conn)
edit()
startEdit()

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl2to1srcdst)
if(ref != None):
    cd("/JMSBridgeDestinations/%s" % wl2to1srcdst)
    set('ConnectionURL','')
    set('UserName','')
    set('UserPassword','')
    print("%s has been configured." % wl2to1srcdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl2to1tgtdst)
if(ref != None):
    cd("/JMSBridgeDestinations/%s" % wl2to1tgtdst)
    set('ConnectionURL', wl1conn)
    set('UserName', wl1user)
    set('UserPassword', wl1pass)
	set('InitialContextFactory',initctxtfctry)
	set('ConnectionFactoryJNDIName',connfctryjndinm)
	set('DestinationJNDIName',wl2to1tgtdstjndiname)
    print("%s has been configured." % wl2to1tgtdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl1to2srcdst)
if(ref != None):
    cd("/JMSBridgeDestinations/%s" % wl1to2srcdst)
    set('ConnectionURL', wl1conn)
    set('UserName', wl1user)
    set('UserPassword', wl1pass)
	set('InitialContextFactory',initctxtfctry)
	set('ConnectionFactoryJNDIName',connfctryjndinm)
	set('DestinationJNDIName',wl1to2srcdstjndiname)
    print("%s has been configured." % wl1to2srcdst)

cd('/')
ref = getMBean("/JMSBridgeDestinations/%s" % wl1to2tgtdst)
if(ref != None):
    cd("/JMSBridgeDestinations/%s" % wl1to2tgtdst)
    set('ConnectionURL', '')
    set('UserName','')
    set('UserPassword','')
    print("%s has been configured." % wl1to2tgtdst)

cd('/')
cd("/MessagingBridges/%s" % wl1to2bridge)
set('Started', true)
cd("/MessagingBridges/%s" % wl2to1bridge)
set('Started', true)

activate()

print 'Exiting....'

disconnect()

exit()
