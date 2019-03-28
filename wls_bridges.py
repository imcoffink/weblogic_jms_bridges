# Configure OMS <> AUA JMS Bridges

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

print 'Creating JMS Bridge Destinations in WL Server 1'
connect(wl1user,wl1pass,wl1conn)
edit()
startEdit()

cd('/')
ref = getMBean("/Deployments/%s" % wl1to2bridge)
if(ref == None):
    cmo.createMessagingBridge("%s" % wl1to2bridge)
    cd("/Deployments/%s" % wl1to2bridge)
    set('Targets',jarray.array([ObjectName("com.bea:Name=%s,Type=Server" % beasrvtp)],
    ObjectName))
    cmo.setSourceDestination(getMBean("/JMSBridgeDestinations/%s" % wl1to2srcdst))
    cmo.setTargetDestination(getMBean("/JMSBridgeDestinations/%s" % wl1to2tgtdst))
    set('Selector','')
    set('QualityOfService','Exactly-once')
    set('QOSDegradationAllowed','true')
    set('IdleTimeMaximum','60')
    set('AsyncEnabled','true')
    set('DurabilityEnabled','true')
    set('PreserveMsgProperty','false')
    set('Started','true')
    set('BatchInterval','100')
else:
    print("%s bridge already created." % wl1to2bridge)

cd('/')
ref = getMBean("/Deployments/%s" % wl2to1bridge)
if(ref == None):
    cmo.createMessagingBridge("%s" % wl2to1bridge)
    cd("/Deployments/%s" % wl2to1bridge)
    set('Targets',jarray.array([ObjectName("com.bea:Name=%s,Type=Server" % beasrvtp)],
    ObjectName))
    cmo.setSourceDestination(getMBean("/JMSBridgeDestinations/%s" % wl2to1srcdst))
    cmo.setTargetDestination(getMBean("/JMSBridgeDestinations/%s" % wl2to1tgtdst))
    set('Selector','')
    set('QualityOfService','Exactly-once')
    set('QOSDegradationAllowed','true')
    set('IdleTimeMaximum','60')
    set('AsyncEnabled','true')
    set('DurabilityEnabled','true')
    set('PreserveMsgProperty','false')
    set('Started','true')
    set('BatchInterval','100')
else:
    print("%s bridge already created." % wl2to1bridge)

activate()

print 'Exiting....'

disconnect()

print 'Creating JMS Bridge Destinations in WL Server 2'
connect(wl2user,wl2pass,wl2conn)
edit()
startEdit()

cd('/')
ref = getMBean("/Deployments/%s" % wl1to2bridge)
if(ref == None):
    cmo.createMessagingBridge("%s" % wl1to2bridge)
    cd("/Deployments/%s" % wl1to2bridge)
    set('Targets',jarray.array([ObjectName("com.bea:Name=%s,Type=Server" % beasrvtp)],
    ObjectName))
    cmo.setSourceDestination(getMBean("/JMSBridgeDestinations/%s" % wl1to2srcdst))
    cmo.setTargetDestination(getMBean("/JMSBridgeDestinations/%s" % wl1to2tgtdst))
    set('Selector','')
    set('QualityOfService','Exactly-once')
    set('QOSDegradationAllowed','true')
    set('IdleTimeMaximum','60')
    set('AsyncEnabled','true')
    set('DurabilityEnabled','true')
    set('PreserveMsgProperty','false')
    set('Started','true')
    set('BatchInterval','100')
else:
    print("%s bridge already created." % wl1to2bridge)

cd('/')
ref = getMBean("/Deployments/%s" % wl2to1bridge)
if(ref == None):
    cmo.createMessagingBridge("%s" % wl2to1bridge)
    cd("/Deployments/%s" % wl2to1bridge)
    set('Targets',jarray.array([ObjectName("com.bea:Name=%s,Type=Server" % beasrvtp)],
    ObjectName))
    cmo.setSourceDestination(getMBean("/JMSBridgeDestinations/%s" % wl2to1srcdst))
    cmo.setTargetDestination(getMBean("/JMSBridgeDestinations/%s" % wl2to1tgtdst))
    set('Selector','')
    set('QualityOfService','Exactly-once')
    set('QOSDegradationAllowed','true')
    set('IdleTimeMaximum','60')
    set('AsyncEnabled','true')
    set('DurabilityEnabled','true')
    set('PreserveMsgProperty','false')
    set('Started','true')
    set('BatchInterval','100')
else:
    print("%s bridge already created." % wl2to1bridge)

activate()

print 'Exiting....'

disconnect()

exit()
