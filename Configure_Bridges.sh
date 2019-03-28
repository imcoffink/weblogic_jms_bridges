#! /bin/ksh

#===============================================================
# Name    :  Configure_Bridges.sh
# Author  :  Iago Misko
# Date    :  November 24th, 2017
# Purpose :  Configure JMS Bridges between two WebLogic Server instances
# Usage   :  Configure_Bridges.sh <config_file>
#
# Changes history:
#  Date     |     By        | Changes/New features
# ----------+---------------+-----------------------------------
# 11-24-17    Iago Misko      Initial version
#===============================================================

Usage()
{
	echo "Usage:"
	echo "         $0 <config_file>"
	echo "Example:"
	echo "         $0 bridges_conf.py"
	echo ""
	exit 1
}

if [ $# -ne 1 ]
then
	Usage
fi

CONF_FILE=$1
. ${CONF_FILE}

echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

echo "Creating WL1 <> WL2 JMS Bridge Destinations"

echo "WL1 Host: ${WL1_HOST}"
echo "WL1 Port: ${WL1_PORT}"
echo "WL1 User: ${WL1_USER}"
echo "WL1 Pasword: ${WL1_PASS}"
echo "WL1 Connection: ${WL1_CONN}"

echo "WL2 Host: ${WL2_HOST}"
echo "WL2 Port: ${WL2_PORT}"
echo "WL2 User: ${WL2_USER}"
echo "WL2 Pasword: ${WL2_PASS}"
echo "WL2 Connection: ${WL2_CONN}"

${WLST_PATH}${WLST} wls_destinations.py -u ${WL1_USER} -p ${WL1_PASS} -c ${WL1_CONN} -j ${WL2_USER} -k ${WL2_PASS} -l ${WL2_CONN}

echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

echo "Creating WL1 <> WL2 Bridges"

echo "WL1 Host: ${WL1_HOST}"
echo "WL1 Port: ${WL1_PORT}"
echo "WL1 User: ${WL1_USER}"
echo "WL1 Pasword: ${WL1_PASS}"
echo "WL1 Connection: ${WL1_CONN}"

echo "WL2 Host: ${WL2_HOST}"
echo "WL2 Port: ${WL2_PORT}"
echo "WL2 User: ${WL2_USER}"
echo "WL2 Pasword: ${WL2_PASS}"
echo "WL2 Connection: ${WL2_CONN}"
	
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
	
${WLST_PATH}${WLST} wls_bridges.py -u ${WL1_USER} -p ${WL1_PASS} -c ${WL1_CONN} -j ${WL2_USER} -k ${WL2_PASS} -l ${WL2_CONN}
${WLST_PATH}${WLST} wls_integration.py -u ${OMS_USER} -p ${OMS_PASS} -c ${OMS_CONN} -j ${AUA_USER} -k ${AUA_PASS} -l ${AUA_CONN}
	
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
