# WebLogic Bridge Configuration Tool - Configuration File

# WebLogic Server Hosts, Ports, Users and Passwords

# SAMPLE
#WL1_HOST="mywlsrva"
#WL1_PORT="27533"
#WL1_USER="Weblogic"
#WL1_PASS="Weblogic1"

#WL2_HOST="mywlsrvb"
#WL2_PORT="31927"
#WL2_USER="Weblogic"
#WL2_PASS="Weblogic1"

# CHANGE
WL1_HOST="%wl.server.1.host%"
WL1_PORT="%wl.server.1.port%"
WL1_USER="%wl.server.1.user%"
WL1_PASS="%wl.server.1.password%"

WL2_HOST="%wl.server.2.host%"
WL2_PORT="%wl.server.2.port%"
WL2_USER="%wl.server.2.user%"
WL2_PASS="%wl.server.2.password%"

# DEFAULT
WL1_CONN="t3://${WL1_HOST}:${WL1_PORT}"
WL2_CONN="t3://${WL2_HOST}:${WL2_PORT}"


# WebLogic Installation Info

# SAMPLE
#WL_HOME="/opt/weblogic1212"

# CHANGE
WL_HOME="%weblogic.installation.path%"

# DEFAULT
WLST_PATH="${WL_HOME}/common/bin/"
WLST="wlst.sh"


# Bridge Destinations

# SAMPLE
#adptjndinm="eis.jms.WLSConnectionFactoryJNDIXA"
#initctxtfctry="weblogic.jndi.WLInitialContextFactory"
#connfctryjndinm="weblogic.jms.XAConnectionFactory"

# CHANGE
adptjndinm="%adapter.jndi.name%"
initctxtfctry="%initial.context.factory%"
connfctryjndinm="%connection.factory.jndi.name%"


# WL1 to WL2 Source Destination

# SAMPLE
#wl1to2srcdst="Order2Bill-Source"
#wl1to2srcdstjndiname="javaBeans.OrderJMS.SourceQueue"

# CHANGE
wl1to2srcdst="%wl1.to.wl2.source.destination%"
wl1to2srcdstjndiname="%wl1.to.wl2.source.destination.jndi.name%"


# WL1 to WL2 Target Destination

# SAMPLE
#wl1to2tgtdst="Order2Bill-Target"
#wl1to2tgtdstjndiname="javaBeans.OrderJMS.TargetQueue"

# CHANGE
wl1to2tgtdst="%wl1.to.wl2.target.destination%"
wl1to2tgtdstjndiname="%wl1.to.wl2.target.destination.jndi.name%"


# WL2 to WL1 Source Destination

# SAMPLE
#wl2to1srcdst="Bill2Order-Source"
#wl2to1srcdstjndiname="javaBeans.NotifyOrderJMS.SourceQueue"

# CHANGE
wl2to1srcdst="%wl2.to.wl1.source.destination%"
wl2to1srcdstjndiname="%wl2.to.wl1.source.destination.jndi.name%"


# WL2 to WL1 Target Destination

# SAMPLE
#wl2to1tgtdst="Bill2Order-Target"
#wl2to1tgtdstjndiname="javaBeans.NotifyOrderJMS.TargetQueue"

# CHANGE
wl2to1tgtdst="%wl2.to.wl1.target.destination%"
wl2to1tgtdstjndiname="%wl2.to.wl1.target.destination.jndi.name%"


# Bridge Names

# SAMPLE
#wl1to2bridge="Order2Bill"
#wl2to1bridge="Bill2Order"

# CHANGE
wl1to2bridge="%wl1.to.wl2.bridge.name%"
wl2to1bridge="%wl2.to.wl1.bridge.name%"


# BEA Variables

# SAMPLE
#beasrvtp="AppServer"

# CHANGE
beasrvtp="%bea.server.type%"
