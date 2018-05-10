'''Global API'''
'''author Cloud '''
import time
import subprocess
import os
import codecs
import re
import struct
import base64
import telnetlib
import subprocess,traceback, platform
from selenium import webdriver
from ftplib import FTP
import ftplib
from API._FormatCheckLib import *
from API._logging import *
from API._Console import *
import urllib,urllib2
import requests
import logging
import sys
import warnings
import pytest
import allure
from allure.constants import AttachmentType
from PIL import Image
import math
import operator
from functools import reduce
com = 'com1'
user='admin'
passwd='Password!'
TimeLoad = 160
GenieWaitTime = 38
log = logging.getLogger(__name__)
cmd = '"taskkill.exe" /F /IM firefox.exe '
p = os.popen(cmd)
hostip = '192.168.1.1'

def ping(host):
    if platform.system()=='Windows':
        cmd = 'ping -n %d %s'%(1,host)
    else:
        cmd = 'ping -c %d %s'%(1,host)
    try:
        p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (stdoutput,erroutput) = p.communicate()
    # print stdoutput
    except Exception, e:
        traceback.print_exc()
    if platform.system()=='Windows':
        str1 = stdoutput.find('Destination host unreachable')
        str2 = stdoutput.find('nRequest timed out')
        str3 = stdoutput.find('100% loss')
        if str1 != -1 or str2 != -1 or str3 != -1:
            pingresult = 'false'
        else:
            pingresult = 'true'
    else:
        str1 = stdoutput.find('Destination host unreachable')
        str2 = stdoutput.find('nRequest timed out')
        str3 = stdoutput.find('1 packets received')
        if str1 != -1 or str2 != -1 or str3 != -1:
            pingresult = 'false'
        else:
            pingresult = 'true'
    return pingresult

#======================Get DUT ip-=============
def getHostip():
    trace('\n========= Get dut ip')
    str1 = sendCommandAndGetReturn(com,'nvram get wla_ssid')
    print str1
    if str1.find('Unknown command') != -1:
        str1 = ping('192.168.0.1')
        if str1 == 'true':
            host_ip = '192.168.0.1'
        else:
            str2 = ping('192.168.100.1')
            if str2 == 'true':
                host_ip = '192.168.100.1'    
    else:
        if str1.find('#') == -1:
            try:
                driver = webdriver.Firefox()
                httpurl = "http://admin:password@192.168.0.1/setup.cgi?todo=uartenable123"
                driver.get(httpurl)
                time.sleep(15)
                driver.quit()
                driver = webdriver.Firefox()
                httpurl = "http://admin:Password!@192.168.0.1/setup.cgi?todo=uartenable123"
                driver.get(httpurl)
                time.sleep(15)
                driver.quit()
            except:
                time.sleep(1)
        else:
            print 'Console enable'
        host_ip = getIpByConsole(com, 'ifconfig')
        # try:
            # if host_ip.find('127.0.0.1') != -1:
                # host_ip = '192.168.1.1'
        # except:
            # time.sleep(1)
    return host_ip

#======================Get DUT ip-=============
#======================Get DUT console type-=============
def getConsoletype():
    trace('\n========= get console prop info')
    sendCommandAndGetReturn(com,'cd /')
    sendCommandAndGetReturn(com,'/doc/scan_stop')
    console_index = ''
    str1 = sendCommandAndGetReturn(com,'nvram get wla_ssid')
    if str1.find('Unknown command') != -1:
        console_index = 'cable'
    elif str1.find('#') == -1:
        try:
            driver = webdriver.Firefox()
            httpurl = "http://admin:password@192.168.0.1/setup.cgi?todo=uartenable123"
            driver.get(httpurl)
            time.sleep(15)
            driver.quit()
            driver = webdriver.Firefox()
            httpurl = "http://admin:Password!@192.168.0.1/setup.cgi?todo=uartenable123"
            driver.get(httpurl)
            time.sleep(15)
            driver.quit()
        except:
            time.sleep(1)
    elif str1 == '':
        sendCommandAndGetReturn('com3','c0')
        sendCommandAndGetReturn('com3','c0')
        sendCommandAndGetReturn('com3','o0')
        sendCommandAndGetReturn('com3','o0')
        time.sleep(160)
    else:
        print 'Console enable'
    if console_index != 'cable':
        str = sendCommandAndGetReturn(com,'nvram get wla_ssid')
        if str.find('nvram: not found') == -1:
            console_index = 'nvram'
        else:
            str1 = sendCommandAndGetReturn(com,'param get wla_ssid')
            if str1.find('param: not found') == -1:
                console_index = 'param'
    return console_index

console_type = getConsoletype()
print 'DUT console type:',console_type
#======================Get DUT console type-=============
def aploaddefault():
    trace('\n========= dut loaddefault and reboot')
    if console_type != 'cable':
        str = sendCommandAndGetReturn(com,console_type + ' loaddefault')
        if str.find('done') != -1 or str.find('finished') != -1 or str.find('RST button') != -1:
            sendCommandAndGetReturn(com,'reboot')
        else:
            sendCommandAndGetReturn('com3','c0')
            sendCommandAndGetReturn('com3','c0')
            sendCommandAndGetReturn('com3','o0')
            sendCommandAndGetReturn('com3','o0')
        print 'DUT loaddefault' 
        time.sleep(160)
    else:
        sendCommandAndGetReturn(com,'reset')
        print 'DUT reset' 
        time.sleep(80)
        sendCommandAndGetReturn(com,'cd /')
        sendCommandAndGetReturn(com,'/doc/scan_stop')
log.info( 'step-0-0 dut loaddrfault wait 160s')
aploaddefault()
hostip = getHostip()
print 'dut host ip:',hostip

#======================Get DUT name-=============
def curlGetProjectname(username,password,ipaddress):
    trace('\n========= curl Get Projectname') 
    driver = webdriver.Firefox()
    httpurl = "http://" + username + ':' + password + "@" + hostip
    if console_type == 'cable':
        httpurl = "http://" + username + ':' + password + "@" + hostip
    driver.get(httpurl)
    str = driver.page_source
    time.sleep(15)
    driver.quit()
    if console_type == 'cable': 
        projectstr = re.findall(r'<title>NETGEAR Gateway (.+?)</title>',str)
        if projectstr == []:
            projectstr = re.findall(r'name="description" content=(.+?)>',str)
            a = projectstr[0].split('"', )
            Projectid = [a[1]]
        else: 
            Projectid = projectstr
    else:
        url = 'http://' + ipaddress + '/FW_log.htm'
        cmd = 'curl.exe -u ' + username + ':' + password + ' ' + url
        print cmd
        trace(cmd)
        p = os.popen(cmd)
        str = p.read()
        p = os.popen(cmd)
        str = p.read()
        if str == '':
            Projectid = 'dut offline'
        else:
            if str.find('401 Unauthorized') != '-1':
                print "401,loginin fail---login again"
                sendCommandAndGetReturn('com1',console_type + ' set circle_no_remind=1')	
                sendCommandAndGetReturn('com1',console_type + ' save')
                print "login again"
                p = os.popen(cmd)
                str = p.read()
                projectstr = re.findall(r'<title>NETGEAR Router (.+?)</title>',str)
                if projectstr[0] == 'Nighthawk X6 R8000':
                    Projectid = ['R8000']
                elif projectstr[0] == 'Nighthawk R7000':
                    Projectid = ['R7000']
                elif projectstr[0] == 'Nighthawk X6 R7900':
                    Projectid = ['R7900']
                elif projectstr[0] == 'Nighthawk R6700':
                    Projectid = ['R6700']
                elif projectstr[0] == 'Orbi Index':
                    Projectid = ['Orbi']
                else:
                    Projectid = projectstr
            else:
                print 'login as http://hostip/fw_log|Logs.htm'
                projectstr = re.findall(r'<title>NETGEAR Router (.+?)</title>',str)
                if projectstr[0] == 'Nighthawk X6 R8000':
                    Projectid = ['R8000']
                elif projectstr[0] == 'Nighthawk R7000':
                    Projectid = ['R7000']
                elif projectstr[0] == 'Nighthawk X6 R7900':
                    Projectid = ['R7900']
                elif projectstr[0] == 'Nighthawk R6700':
                    Projectid = ['R6700']
                elif projectstr[0] == 'Orbi Index':
                    Projectid = ['Orbi']
                else:
                    Projectid = projectstr 
    return Projectid

def Genie_overleap():
    trace('\n========= dut genie overleap')
    if console_type == 'cable':
        print 'Cable no Genie_overleap'
    else:
        str1 = sendCommandAndGetReturn(com,'nvram get wla_ssid')
        print str1
        if str1.find('#') == -1:
            try:
                driver = webdriver.Firefox()
                httpurl = "http://admin:password@192.168.0.1/setup.cgi?todo=uartenable123"
                driver.get(httpurl)
                time.sleep(15)
                driver.quit()
                driver = webdriver.Firefox()
                httpurl = "http://admin:Password!@192.168.0.1/setup.cgi?todo=uartenable123"
                driver.get(httpurl)
                time.sleep(15)
                driver.quit()
            except:
                time.sleep(1)
        else:
            print 'Console enable'
        str2 = sendCommandAndGetReturn(com,'version')
        print str2
        if str2.find('Orbi') != -1:
            get_url = 'http://192.168.1.1/Orbi_admin_account_settings.htm'
            r = requests.get(get_url,auth=(user,passwd))
            token = re.findall('\?id=[0-9a-z]+',r.text)
            cmd1 = 'curl.exe -u admin:Password! -d "sysNewPasswd=Password%%21&sysConfirmPasswd=Password%%21&question1=1&answer1=1&question2=1&answer2=1" http://192.168.1.1/wizsetpassword.cgi' + token[0]
            p = os.popen(cmd1)
            cmd2 = 'curl.exe -u admin:Password! -d "ssid=ORBI85&passphrase=festiveonion830" http://192.168.1.1/wizsetwifi.cgi' + token[0]
            p = os.popen(cmd2)
            cmd3 = 'curl.exe -u admin:Password! -d "Check=Check&OrbiCheck=OrbiCheck" http://192.168.1.1/ver_check_upgrade.cgi' + token[0]
            p = os.popen(cmd3)
            cmd4 = 'curl.exe -u admin:Password! -d "" http://192.168.1.1/upgrade_status.cgi' + token[0]
            p = os.popen(cmd4)
            print "Orbi genie done"
        else:
            if console_type == 'nvram' or console_type == 'param':
                sendCommandAndGetReturn(com,'burnsku 9')
                str3 = sendCommandAndGetReturnUntil(com,'nvram show | grep https ','#')
                if str3.find('httpsEnable') != -1:
                    sendCommandAndGetReturn(com,console_type + ' set httpsEnable=0')  
                if hostip == '192.168.1.1':
                    sendCommandAndGetReturn(com,console_type + ' set as_genie=0')
                    sendCommandAndGetReturn(com,console_type + ' set auto_update_enable=1')
                else:
                    sendCommandAndGetReturn(com,console_type + ' set as_genie=1')
                    sendCommandAndGetReturn(com,console_type + ' set auto_update_enable=0')  
                sendCommandAndGetReturn(com,console_type + ' set gui_Internet_state=1')
                sendCommandAndGetReturn(com,console_type + ' set brs_lang_check_enable=0')
                sendCommandAndGetReturn(com,console_type + ' set gui_Wireless_Radio_state=both')
                sendCommandAndGetReturn(com,console_type + ' set gui_Wireless_Security_state=both')
                sendCommandAndGetReturn(com,console_type + ' set http_passwd=Password!')
                sendCommandAndGetReturn(com,console_type + ' set genie_admin_password=1')
                sendCommandAndGetReturn(com,console_type + ' set need_to_load_basic=1')
                sendCommandAndGetReturn(com,console_type + ' set password_question1=1')
                sendCommandAndGetReturn(com,console_type + ' set password_question2=1')
                sendCommandAndGetReturn(com,console_type + ' set password_answer1=1')
                sendCommandAndGetReturn(com,console_type + ' set password_answer2=1')
                sendCommandAndGetReturn(com,console_type + ' set blank_state=0')
                sendCommandAndGetReturn(com,console_type + ' set weak_passwd_neverRemind=1')
                sendCommandAndGetReturn(com,console_type + ' set enable_password_recovery=0')
                sendCommandAndGetReturn(com,console_type + ' set circle_no_remind=1')
                sendCommandAndGetReturn(com,console_type + ' set call_by_genie=0')
                sendCommandAndGetReturn(com,console_type + ' set router_TC_enable=1')
                sendCommandAndGetReturn(com,console_type + ' set RA_enable=1')
                sendCommandAndGetReturn(com,console_type + ' set auto_enable=0')
                sendCommandAndGetReturn(com,console_type + ' set http_passwd_digest=06fdbf93a794fa04a93d1eaca4d75740d3e936af50fbcfe46e7f49bac34eb06d')
                sendCommandAndGetReturn(com,console_type + ' save')
                if str3.find('httpsEnable') != -1:
                    sendCommandAndGetReturn(com,console_type + ' set http_passwd_digest=01cb92dfff4091c2bee0f343b2af049fb39b45c08a1e5132b834e12e037d919d')
                    ser = serial.Serial('com1', '115200', timeout=1)
                    ser.write('cd /' + "\n")
                    line = ser.read(256)
                    print line
                    ser.write('cd /media/nand' + "\n")
                    line = ser.read(256)
                    print line
                    ser.write('./dap proxy web --delete' + "\n")
                    line = ser.read(256)
                    print line
                    ser.write('./dap proxy web http://192.168.1.1:80 http://127.0.0.1:8080 --protect=off' + "\n")
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
                if hostip == '192.168.1.1':
                    sendCommandAndGetReturn(com,console_type + ' set bd_no_remind=1')
                    sendCommandAndGetReturn(com,console_type + ' set as_genie=0')
                    sendCommandAndGetReturn(com,console_type + ' set auto_update_enable=1')
                    sendCommandAndGetReturn(com,console_type + ' save')
                    sendCommandAndGetReturn(com,'')
                print "AP Genie over leap done"
            else:
                print "cable genie"
        cmd = '"taskkill.exe" /F /IM firefox.exe '
        p = os.popen(cmd)

log.info( "step-0-1 AP Genie over leap done")
Genie_overleap()

ProjectName = ' '
try:
    if console_type == 'cable':
        ProjectName = curlGetProjectname('admin','password',hostip)
    else:
        ProjectName = curlGetProjectname('admin','Password!',hostip)
except:
    time.sleep(1)
ProjectName = ProjectName[0]
print 'DUT projectname is:',ProjectName
if console_type == 'cable':
    user='admin'
    passwd='password'
#print ProjectName
#======================Get DUT name-=============
# DUT url info
############# setup ###################
start = 'start.htm'
urlWirelessSetup = 'WLG_wireless_dual_band_r10.htm' 
urlLANSetup = 'LAN_lan.htm'
# urlAddress_Reservation "LAN_reserv_add.htm"
urlDeviceName = 'DEV_name.htm'
urlGuestNetwork = "WLG_wireless_dual_band_2.htm"
urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
urlGuestNetwork2G_passphrase = "WLG_2g_wireless2_2.htm"
urlGuestNetwork5G = "WLG_5g_wireless3_2.htm"
urlGuestNetwork5G_1 = "WLG_5g_wireless3_2.htm"
urlGuestNetwork5G_2 = "WLG_5g_wireless3_3.htm"
#=============setup =========================
#===============USB Storage==================
#===============USB Storage==================
#===============Security=====================
#===============Security=====================
#===============Administration===============
urlRouterStatus = "ADV_home.htm"
urlAttachedDevices = "DEV_redirect.htm"
urlDevicecontrol = "DEV_control.htm"
urlLogs = "FW_log.htm"
#===============Administration===============
#===============Advanced Setup===============
urlWirelessSettings = "WLG_adv_dual_band2.htm"
urlStaticRoutes = "STR_routes.htm"
multilginurl = "MNU_access_multiLogin2.htm"

if ProjectName == 'WNDR4500v2':
    urlWirelessSetup = "WLG_wireless_dual_band.htm"	
elif ProjectName == 'WNDR3400v3':
    urlWirelessSetup = "WLG_wireless_dual_band.htm"	
elif ProjectName == 'R6200v2':
    urlRouterStatus = "ADV_home.htm"
elif ProjectName == 'R6400v2':
    urlRouterStatus = "ADV_home2.htm"
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    urlGuestNetwork5G = "WLG_5g_wireless2_2.htm"
elif ProjectName == 'R6400':
    urlRouterStatus = "ADV_home2.htm"
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    urlGuestNetwork5G = "WLG_5g_wireless2_2.htm"
elif ProjectName == 'R6300v2':
    urlRouterStatus = "ADV_home.htm"
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    urlGuestNetwork5G = "WLG_5g_wireless2_2.htm"
elif ProjectName == 'R6250':
    urlRouterStatus = "ADV_home2.htm"		
elif ProjectName == 'R6700':
    urlRouterStatus = "ADVANCED_home.htm"
    urlGuestNetwork5G = "WLG_5g_wireless2_2.htm"
elif ProjectName == 'R6900':	
    urlAttachedDevices = "DEV_device_R7000.htm"
    urlGuestNetwork5G = "WLG_5g_wireless2_2.htm"
    urlDeviceName = "DEV_name.htm"
    urlRouterStatus = "ADVANCED_home2.htm"
elif ProjectName == 'R7000':	
    urlDeviceName = "DEV_name.htm"
    urlRouterStatus = "ADVANCED_home2.htm"
elif ProjectName == 'R7000P':	
    urlRouterStatus = "ADVANCED_home2.htm"
    urlWirelessSetup = "WLG_wireless_dual_band_r10.htm"
    urlGuestNetwork5G = "WLG_5g_wireless2_2.htm"
    GenieWaitTime = 38
elif ProjectName == 'R7100LG':	
    urlRouterStatus = "ADVANCED_home2.htm" 
    urlWirelessSettings = "WLG_wireless_dual_band_r10.htm"
    urlGuestNetwork = "WLG_wireless_dual_band_2.htm"
elif ProjectName == 'R7300':		 
    urlRouterStatus = "ADVANCED_home2.htm"
elif ProjectName == 'R7900':		
    urlWirelessSetup = "WLG_wireless_dual_band_r7900.htm"
    urlGuestNetwork = "WLG_wireless_dual_band_2_r7900.htm"
    urlWirelessSettings = "WLG_adv_dual_band2_r7900.htm"
    urlGuestNetwork5G = "WLG_5g_wireless3_2.htm"
elif ProjectName == 'R8000':	
    urlGuestNetwork5G = "WLG_5g_wireless2_2.htm"
    urlWirelessSetup = "WLG_wireless_dual_band_r8000.htm"
    urlRouterStatus = "ADV_home2_r8000.htm"
    urlWirelessSettings = "WLG_adv_dual_band2_r8000.htm"
elif ProjectName == 'R8300':	
    urlRouterStatus = "ADVANCED_home2_tri_band.htm"
    urlGuestNetwork = "WLG_wireless_tri_band_2.htm"
    urlWirelessSetup = "WLG_wireless_tri_band.htm"
elif ProjectName == 'D6220':
    urlRouterStatus = "ADVANCED_home.htm"
elif ProjectName == 'D6400':
    urlRouterStatus = "ADVANCED_home.htm"
elif ProjectName == 'D8500':
    urlWirelessSetup = "WLG_home.htm"
    urlRouterStatus = "ADVANCED_home.htm"
elif ProjectName == 'CBR40':
    urlWirelessSetup = "WLG_wireless2.htm"
elif ProjectName == 'D7000v2':
    urlRouterStatus = "ADVANCED_home2.htm"
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    urlGuestNetwork5G = "WLG_5g_wireless2_2.htm"
elif ProjectName == 'DGN2200v4':
    urlWirelessSetup = "WLG_wireless.htm" 
elif ProjectName == 'DGN2200Bv4':
    urlInternetSetup = "BAS_basic.htm" 
    urlWirelessSetup = "WLG_wireless.htm" 
elif ProjectName == 'R8500':
    GenieWaitTime = 38
    urlInternetSetup = "BAS_basic.htm"	
    urlWirelessSetup = "WLG_home.htm" 
    urlRouterStatus = "ADVANCED_home.htm"
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    urlGuestNetwork5G = "WLG_5g_wireless3_2.htm"
    urlGuestNetwork = "WLG_wireless_tri_band_2.htm"
elif ProjectName == 'R8000P':
    urlRouterStatus = "ADVANCED_home.htm"
    urlWirelessSetup = "WLG_home.htm" 
elif ProjectName == 'WNR3500Lv2':
    urlWirelessSetup = "WLG_wireless.htm" 
elif ProjectName == 'C3700-100NAS' or ProjectName == 'C7000-100NAS' or ProjectName == 'C7000v2' or ProjectName == 'C6250-100NAS':
    start = "index.htm"
    urlLogs = "Logs.htm"
    urlInternetSetup = "BasicSettingsBottom.htm" 
    urlWirelessSetup = "WirelessSettings.htm" 
    urlDevicecontrol = "AccessControl.htm"
    urlRouterStatus = "RouterStatus.htm"
    multilginurl = "MultiLogin.htm"
    urlLANSetup = 'LANSetup.htm'
elif ProjectName == 'Extender':
    urlLogs = "wifiSettings.html"
    start = "start.htm"
    urlWirelessSetup = "wifiSettings.html" 
    multilginurl = "MNU_access_multiLogin2.htm"
else:
    if console_type == 'cable':
        if ProjectName == 'CM500V-1STAUS':
            urlLogs = "eventLog.htm"
            urlDevicecontrol = "MtaStatus.htm"
        else:
            urlLogs = "Logs.htm"
        start = "index.htm"
        urlWirelessSetup = "WirelessSettings.htm" 
        urlRouterStatus = "RouterStatus.htm"
        urlLANSetup = 'LANSetup.htm'

print 'log-url=',urlLogs
  
host = 'http://' + hostip + '/'
print 'host=',host
