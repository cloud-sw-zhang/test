import requests
import time
import re
import base64
from requests.packages import urllib3
urllib3.disable_warnings()
import os
import telnetlib
import subprocess,traceback, platform
from API._FormatCheckLib import *
from API._logging import *
from API._Console import *
import logging
import sys
import warnings

ip = '192.168.1.1'
user='admin'
passwd='A0dsp33d*'
host='https://192.168.1.1/'

log = logging.getLogger(__name__)

headers = {
    'Host' : ip,
    'Connection' : 'keep-alive',
    'Authorization': 'Basic ' + base64.b64encode(user+ ':' + passwd) ,
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT' : '1',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.8,ca;q=0.6,en;q=0.4,ja;q=0.2,zh-TW;q=0.2',
}

def getIDToken(url):
    log.info( 'Get id token from',url, 'page' )
    get_url = host + url
    log.info( get_url)
    tmpHTML = ''
    token = ''
    a = 1
    try:
        tmpHTML = requests.get(get_url,auth=(user,passwd),verify=False)
    except:
        time.sleep(1)
    while tmpHTML == '':
        a= a + 1
        log.info( 'try get token ',a,'times')
        try:
            tmpHTML = requests.get(get_url,auth=(user,passwd),verify=False)
        except:
            time.sleep(1)
        if a == 10:
            break
    log.info( tmpHTML)
    if tmpHTML == '':
        log.info( 'Get Token fail')
        return token
    else:
        if tmpHTML.status_code != 200:
            tmpHTML = requests.get(get_url,auth=(user,passwd),verify=False)
        else:
            log.info( tmpHTML.status_code)

        token = re.findall('\?id=[0-9a-z]+',tmpHTML.text)
        return token[0]

def aploaddefault():
    sendCommandAndGetReturn('com1',' ')
    log.info( 'send space')
    sendCommandAndGetReturn('com1','nvram loaddefault')
    log.info( 'dut loaddefault')
    sendCommandAndGetReturn('com1','reboot')
    time.sleep(200)
    log.info( 'dut reboot')

def Genie_overleap():
    sendCommandAndGetReturn('com1','nvram set as_genie=1')
    sendCommandAndGetReturn('com1','nvram set gui_Internet_state=1')
    sendCommandAndGetReturn('com1','nvram set gui_Wireless_Radio_state=both')
    sendCommandAndGetReturn('com1','nvram set http_passwd=password')
    sendCommandAndGetReturn('com1','nvram set genie_admin_password=1')
    sendCommandAndGetReturn('com1','nvram set need_to_load_basic=1')
    sendCommandAndGetReturn('com1','nvram set password_question1=1')
    sendCommandAndGetReturn('com1','nvram set password_question2=1')
    sendCommandAndGetReturn('com1','nvram set password_answer1=1')
    sendCommandAndGetReturn('com1','nvram set password_answer2=1')
    sendCommandAndGetReturn('com1','nvram set blank_state=0')
    sendCommandAndGetReturn('com1','nvram set weak_passwd_neverRemind=1')
    sendCommandAndGetReturn('com1','nvram set enable_password_recovery=0')
    sendCommandAndGetReturn('com1','nvram set circle_no_remind=1')
    sendCommandAndGetReturn('com1','nvram set call_by_genie=0')
    sendCommandAndGetReturn('com1','nvram set RA_enable=1')
    sendCommandAndGetReturn('com1','nvram set auto_update_enable=1')
    sendCommandAndGetReturn('com1','nvram set http_passwd_digest=06fdbf93a794fa04a93d1eaca4d75740d3e936af50fbcfe46e7f49bac34eb06d')
    sendCommandAndGetReturn('com1','nvram save')		
    log.info( "AP Genie over leap done")

def Disable_changedToken():	
    ser = serial.Serial('com1', '115200', timeout=1)
    ser.write('cd /' + "\n")
    line = ser.read(256)
    print line
    ser.write('cd /media/nand' + "\n")
    line = ser.read(256)
    print line
    ser.write('./dap proxy webs --delete' + "\n")
    line = ser.read(256)
    print line
    ser.write('./dap proxy webs https://192.168.1.1:443 https://127.0.0.1:8083 --protect=off' + "\n")
    line = ser.read(256)
    print line
    ser.write('fsaDmin7293' + "\n")
    line = ser.read(256)
    print line
    ser.write('./dap service restart' + "\n")
    line = ser.read(256)
    print line
    ser.write('cd /' + "\n")
    line = ser.read(256)
    print line
    ser.close()
    log.info( "AP Disable changedToken done")
