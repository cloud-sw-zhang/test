#encoding=utf8
'''
Created on 2017.08.10
this lib is used to update FW by curl
@author: Jim Chen
'''
import subprocess
import os
import time
import serial
import pyping
from API._FormatCheckLib import *
from API._logging import *
def sendCommandAndGetReturnUntil(strComPort, strCommand, finish,band = '115200'):
    trace('\n========= Send Command, com={0}'.format(strComPort))
    import re
    time.sleep(0.1)
    ser = serial.Serial(strComPort, band, timeout=1)
    ser.write("\n")
    ser.close()
    time.sleep(0.1)
    ser = serial.Serial(strComPort, band, timeout=1)
    time.sleep(0.1)
    ser.write(strCommand + "\n")
    matcher = re.compile(finish)    #gives you the ability to search for anything
    tic     = time.time()
    buff    = ser.read(256)
    # you can use if not ('\n' in buff) too if you don't like re
    while ((time.time() - tic) < 5) and (not matcher.search(buff)):
        buff += ser.read(256)
    
    trace(buff)
    ser.close()
    return buff

def sendCommandListAndGetReturnUntil(strComPort, strCommandList, finish,band = '115200'):
    trace('\n========= Send Command, com={0}'.format(strComPort))
    import re
    res = ''
    time.sleep(0.1)
    ser = serial.Serial(strComPort, band, timeout=1)
    ser.write("\n")
    ser.close()
    time.sleep(0.1)
    ser = serial.Serial(strComPort, band, timeout=1)
    time.sleep(0.1)
    for cmd in strCommandList:
        print cmd
        ser.write(cmd + "\n")
        matcher = re.compile(finish)    #gives you the ability to search for anything
        tic     = time.time()
        buff    = ser.read(256)
        # you can use if not ('\n' in buff) too if you don't like re
        while ((time.time() - tic) < 5) and (not matcher.search(buff)):
            buff += ser.read(256)
        
        trace(buff)
        res = res + buff
        trace(res)
        print res
    ser.close()
    return res


def sendCommandAndGetReturn(strComPort, strCommand,band = '115200'):
	trace('\n========= Send Command, com={0}'.format(strComPort))
	cmd = strCommand
	time.sleep(1)
	ser = serial.Serial(strComPort, band, timeout=1)
	ser.write("\n")
	ser.close()
	time.sleep(0.2)
	ser = serial.Serial(strComPort, band, timeout=1)
	ser.write(cmd + "\n")
	line = ser.read(256)
	trace(line)
	ser.close()
	return line

    
def getIpByConsole(com, cmd,band = '115200'):
    for i in range(0, 5, 1):
        log = sendCommandAndGetReturnUntil(com, cmd, '#',band = '115200')
        strIp = log[log.find('inet addr:')+len('inet addr:'):log.find(' ', log.find('inet addr:')+len('inet addr:'))]
    if checkIpv4AddressFormat(strIp) == True:
        return strIp
    time.sleep(1)

def isIpBack(strIp):
    trace('\n[PcCtrl] --- try to ping ip: ' + strIp + '.')
    response = pyping.ping(strIp)
    if response.ret_code == 0:
        trace('\n[PcCtrl] --- ping result: pass.')
        return True
    else:
        trace('\n[PcCtrl] --- ping result: fail.')
        return False

def waitIpBack(strIp, intTimeout):
    trace('\n[PcCtrl] --- try to ping ip: ' + strIp + '.')
    response = pyping.ping(strIp)
    tStart = time.time()
    while(response.ret_code != 0):
        trace('\n[PcCtrl] --- ping result: fail, keep trying...')
        response = pyping.ping(strIp)
        tEnd = time.time()
        if (tEnd-tStart) > intTimeout:
            return False
    trace('\n[PcCtrl] --- ping result: pass.')
    time.sleep(3)
    return True
    