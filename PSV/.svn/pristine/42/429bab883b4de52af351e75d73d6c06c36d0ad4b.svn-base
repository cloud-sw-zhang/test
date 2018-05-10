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
com = 'com1'
user='admin'
passwd='Password!'
TimeLoad = 160
port = 21
telnetport = 23
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

def check_DUTnocrash(url):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(15)
    AclStatus = ''
    try:
        AclStatus = driver.find_element_by_name("enable_acl").is_selected()
        driver.quit()
    except:
        time.sleep(1)
    if AclStatus == True or AclStatus == False:
        return 'pass'
    else:
        return 'fail'

def judjeduttelnet(host=hostip,username='admin',password='Password!',telnetport ='23',prompt='#'):
    print 'telnet DUT ip = ', hostip
    tn = ''
    try:
        tn = telnetlib.Telnet(host,telnetport,3)
        str = tn.read_some()
    except:
        time.sleep(1)
    if tn != '':
        print str
        if str.find('BusyBox') != -1 or str.find('#') != -1:
            tn.write('exit' + b"rn")
            case = 'fail'
        elif str.find('login:') != -1:
            str = tn.read_some()
            if str.find('Password') != -1:
                tn.write('password' + b"rn")
                str = tn.read_some()
                if str.find('login:') != -1:
                    case = 'pass'
                else:
                    case = 'fail'
            elif str.find('BusyBox') != -1 or str.find('#') != -1:
                case = 'fail'
            else:
                case = 'pass'
    else:
        case = 'pass'
    return case

#======================Get DUT ip-=============
def getHostip():
    trace('\n========= Get dut ip')
    str1 = sendCommandAndGetReturn(com,'nvram get wla_ssid')
    print str1
    if str1.find('Unknown command') != -1:
        str1 = ping('192.168.0.1')
        if str1 == 'true':
            host_ip = '192.168.0.1'
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
        if host_ip.find('127.0.0.1') != -1:
            host_ip = '192.168.1.1'
    return host_ip

#======================Get DUT ip-=============
def getIDToken(url):
    log.info( "Get id token from %s page",url)
    print console_type
    get_url = url
    driver = webdriver.Firefox()
    httpurl = "http://" + user + ':' + passwd + "@" + hostip
    if console_type == 'cable':
        str = get_url.split('/',)
        httpurl = "http://" + user + ':' + passwd + "@" + hostip + '/' + str[3]
    driver.get(httpurl)
    time.sleep(15)
    str = driver.page_source
    driver.quit()
    log.info(get_url) 
    if console_type == 'cable':
        token = re.findall('\?id=[0-9a-z]+',str)
    else:
        tmpHTML = requests.get(get_url,auth=(user,passwd))
        if tmpHTML.status_code == 400:
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
            log.info( "AP Disable changedToken done")
            tmpHTML = requests.get(get_url,auth=(user,passwd))
            token = re.findall('\?id=[0-9a-z]+',tmpHTML.text)
        else:
            token = re.findall('\?id=[0-9a-z]+',tmpHTML.text)
    return token[0]

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
        print str
        if str.find('nvram: not found') == -1:
            console_index = 'nvram'
        else:
            str1 = sendCommandAndGetReturn(com,'param get wla_ssid')
            print str1
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
        print str
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

def curldownloadpage(username,password,url):
    trace('\n========= curl get page source')
    cmd = '"curl.exe" -u ' + username + ':' + password + ' ' + url
    trace(cmd)
    p = os.popen(cmd)
    str = p.read()
    return str

def tsharkCapture(interface='WAN',packetsize='',packetcount='',duration='',protocol='',file=''):
    trace('\n========= tshark capture')
    print interface
    print packetsize
    print packetcount
    print duration
    print protocol
    print file
    if packetsize != "":
        if interface == 'LAN':
            cmd = '"c:/Program Files/Wireshark/tshark.exe" -i 2 -a filesize:' + packetsize + ' -f ' + protocol + ' -w ' + file
        elif interface == 'WAN':
            cmd = '"c:/Program Files/Wireshark/tshark.exe" -i 1 -a filesize:' + packetsize + ' -f ' + protocol + ' -w ' + file
    elif packetcount != "":
        if interface == 'LAN':
            cmd = '"c:/Program Files/Wireshark/tshark.exe" -i 2 -c ' + packetcount + ' -f ' + protocol + ' -w ' + file
        elif interface == 'WAN':
            cmd = '"c:/Program Files/Wireshark/tshark.exe" -i 1 -c ' + packetcount + ' -f ' + protocol + ' -w ' + file
    else:
        if interface == 'LAN':
            cmd = '"c:/Program Files/Wireshark/tshark.exe" -i 2 -a duration:' + duration + ' -f ' + protocol + ' -w'  + file
        elif interface == 'WAN':
            cmd = '"c:/Program Files/Wireshark/tshark.exe" -i 1 -a duration:' + duration + ' -f ' + protocol + ' -w ' + file	
    trace(cmd)
    p = os.popen(cmd)
    str = p.read()

def tsharkRead(optionV='YES',filter='',packetfile=''):
    trace('\n========= tshark pcap out txt')
    print optionV
    print filter
    print packetfile
    if optionV == 'YES':
        cmd = '"c:/Program Files/Wireshark/tshark.exe" -2 -R ' + filter + ' -V -r ' + packetfile
    else:
        cmd = '"c:/Program Files/Wireshark/tshark.exe" -2 -R ' + filter + ' -r ' + packetfile
    trace(cmd)
    p = os.popen(cmd)
    str = p.read()
    return str

def judje_dutReboot(txt):
    if txt.find('updateProgress') != '-1':
        log.info( "Action Successful, sleep 70s")
        time.sleep(70)
    elif txt.find('The router is rebooting') != '-1':
        log.info( "Action Successful, sleep 160s")
        time.sleep(160)
    else:
        log.info('This step no need reboot')

#======================Get DUT name-=============
def curlGetProjectname(username,password,ipaddress):
    trace('\n========= curl Get Projectname') 
    driver = webdriver.Firefox()
    httpurl = "http://" + username + ':' + password + "@" + hostip
    if console_type == 'cable':
        httpurl = "http://" + username + ':' + password + "@" + hostip + '/Logs.htm'
    driver.get(httpurl)
    str = driver.page_source
    time.sleep(15)
    driver.quit()
    if console_type == 'cable':
        projectstr = re.findall(r'name="description" content=(.+?)>',str)
        a = projectstr[0].split('"', )
        Projectid = [a[1]]
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
                elif projectstr[0] == 'Nighthawk R6700':
                    Projectid = ['R6700']
                elif projectstr[0] == 'Orbi Index':
                    Projectid = ['Orbi']
                else:
                    Projectid = projectstr
            # elif str.find('404 Not Found') != '-1':
                # print '404 not found,login as http://hostip/Logs.htm'
                # url = 'http://' + ipaddress + '/Logs.htm'
                # cmd = '"curl.exe" -u ' + username + ':' + password + ' ' + url
                # print cmd
                # trace(cmd)
                # p = os.popen(cmd)
                # str = p.read()
                # projectstr = re.findall(r'<title>NETGEAR Router (.+?)</title>',str)
                # if projectstr[0] == 'Nighthawk X6 R8000':
                    # Projectid = ['R8000']
                # elif projectstr[0] == 'Nighthawk R7000':
                    # Projectid = ['R7000']
                # elif projectstr[0] == 'Nighthawk R6700':
                    # Projectid = ['R6700']
                # elif projectstr[0] == 'Orbi Index':
                    # Projectid = ['Orbi']
                # else:
                    # Projectid = projectstr
            else:
                print 'login as http://hostip/fw_log|Logs.htm'
                projectstr = re.findall(r'<title>NETGEAR Router (.+?)</title>',str)
                if projectstr[0] == 'Nighthawk X6 R8000':
                    Projectid = ['R8000']
                elif projectstr[0] == 'Nighthawk R7000':
                    Projectid = ['R7000']
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
                str = sendCommandAndGetReturn(com,'version')
                if str.find('R7000P') != -1:
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
                    ser.write('./dap service start' + "\n")
                    line = ser.read(256)
                    print line
                    ser.write('cd /' + "\n")
                    line = ser.read(256)
                    print line
                    ser.close()
                if hostip == '192.168.1.1':
                    sendCommandAndGetReturn(com,console_type + ' set as_genie=0')
                    sendCommandAndGetReturn(com,console_type + ' set auto_update_enable=1')
                else:
                    sendCommandAndGetReturn(com,console_type + ' set as_genie=1')
                    sendCommandAndGetReturn(com,console_type + ' set auto_update_enable=0')
                sendCommandAndGetReturn(com,console_type + ' set gui_Internet_state=1')
                sendCommandAndGetReturn(com,console_type + ' set brs_lang_check_enable=0')
                sendCommandAndGetReturn(com,console_type + ' set gui_Wireless_Radio_state=both')
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
                if hostip == '192.168.1.1':
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
urlInternetSetup = 'BAS_ether.htm'
DHCP = "DHCP"
AccountName = 'system_name'
DomainName = "domain_name"
MACAdress = '//tr[20]/td[2]/input'
urlInternetpptp = 'BAS_pptp.htm'
PPTP = 'PPTP'
PPTPLogin = 'pptp_username'
PPTPpassword = 'pptp_passwd'
ConnectionId = 'pptp_conn_id'
urlInternetpppoe = 'BAS_pppoe.htm'
PPPoE = 'PPPoE'
PPPoELogin = 'pppoe_username'
PPPoEpassword = 'pppoe_passwd'
serviceName = 'pppoe_servicename'
urlWirelessSetup = 'WLG_wireless_dual_band_r10.htm' 
SSID = 'ssid'
Password = 'passphrase'
TKIPPassword = "xpath=(//input[@name='security_type'])[3]"
AESPassword = "xpath=(//input[@name='security_type'])[4]"	
MixPassword = "xpath=(//input[@name='security_type'])[5]"
urlWANSetup = 'WAN_wan.htm'
NATMode	= "//tr[12]/td[2]/input"
urlWANSetupHelp = 'WAN_wan_h.htm'
urlLANSetup = 'LAN_lan.htm'
# urlAddress_Reservation "LAN_reserv_add.htm"
DeviceName = 'device_name'
urlDeviceName = 'DEV_name.htm'
Rst_DeviceName = "//tr[2]/td[4]/span"
urlQoSSetup = 'QOS_main.htm'
urlQoSdown = "QOS_down_streaming.htm"
Qosdown = "highestserviceList"
urlQOSRuleTable = "QOS_ruletab.htm"
Qos = '//tr[2]/td[3]/span'
QosMacdev = 'dev_name'
urlGuestNetwork = "WLG_wireless_dual_band_2.htm"
urlGuestNetwork2G = "WLG_2g_wireless3_2.htm"
urlGuestNetwork2G_passphrase = "WLG_2g_wireless2_2.htm"
urlGuestNetwork5G_1 = "WLG_5g_wireless3_2.htm"
urlGuestNetwork5G_2 = "WLG_5g_wireless3_3.htm"
#=============setup =========================
#===============USB Storage==================
urlUSBBasicSetting = "USB_basic_main.htm"
urlUSBReadyshareStorage = "Readyshare_Storage.htm"
enableUSBHTTPS = "enable_wan_http"
enableUSBFTPInternet = "enable_wan_ftp"

urlUSBAdvancedSetting = "USB_adv_main.htm"
urlUSBMediaServer = "UPNP_media.htm"
urlUSBSettings = "USB_settings.htm"
urlUSBAdvance = "USB_adv.htm"
urlUSBEditStorage = "USB_adv_edit.htm"
#===============USB Storage==================
#===============Security=====================
urlBlockSites = "BKS_keyword.htm"
BlockSite = "cfKeyWord_DomainList"
urlBlockServices = "BKS_service.htm"
BlockServices = '//tr[2]/td[3]/span'
urlSchedule = "FW_schedule.htm"
urlEmail = "FW_email.htm"
Email = "auth_user"
#===============Security=====================
#===============Administration===============
urlRouterStatus = "ADV_home.htm"
urlConnectionStatus = "RST_st_dhcp.htm"
urlLogs = "FW_log.htm"
clearLogButton = "action_Clear"
urlAttachedDevices = "DEV_device.htm"
urlDevicecontrol = "DEV_control.htm"
urlBackupSettings = "BAK_backup.htm"
urlSetPassword = "PWD_password.htm"
urlRouterUpdate = "UPG_upgrade.htm"
#===============Administration===============
#===============Advanced Setup===============
urlWirelessSettings = "WLG_adv_dual_band2.htm"
urlWirelessAP = "WLG_ap_dual_band.htm"
urlPortForwardingTriggering = "FW_forward2.htm"
editPortForwardingTriggering = "Edit"
deletePortForwardingTriggering = "Delete"
portForwardName = '//tr[2]/td[3]/span'
portForwardExtPort = '//tr[2]/td[4]/span'
portForwardIntPort = '//tr[2]/td[5]/span'
portForwardIntIP = '//tr[2]/td[6]/span'

urlPortTriggering = "FW_pt.htm"
portTriggerTimeOut = "fwpt_timeout"
portTriggerName = '//tr[2]/td[4]/span'
portTriggerSrvType = '//tr[2]/td[5]/span'
portTriggerInboundConn = '//tr[2]/td[6]/span'
portTriggerSrvUser = '//tr[2]/td[7]/span'
urlDynamicDNS = "DNS_ddns.htm"
DNSHostName = "sysDNSHost"
DNSUserName = "sysDNSUser"
DNSPassWord = "sysDNSPassword"
urlVPNService = "OPENVPN.htm"
urlStaticRoutes = "STR_routes.htm"
RouteName = '//tr[2]/td[4]/span'
urlRemoteManagement = "FW_remote.htm"
turnRomoteManagementOn = "remote_mg_enable"
urlUPnP = "UPNP_upnp.htm"
urlIPv6 = "IPV6_basic.htm"
urlTrafficMeter = "traffic_meter.htm"
urlTrafficStatus = "traffic_status.htm"
urlTrafficImportantUpdate = "traffic_important_update.htm"
urlWlanACL = "WLG_acl.htm"
WlanACL = '//tr[2]/td[2]/span'
multilginurl = "MNU_access_multiLogin2.htm"

if ProjectName == 'WNDR3400v2':
    portForwardIntPort = '//tr[2]/td[7]/span'
    portForwardIntIP = '//tr[2]/td[8]/span'
elif ProjectName == 'WNDR4500v2':
    urlWirelessSetup = "WLG_wireless_dual_band.htm"	
    urlUSBReadyshareStorage = "USB_adv_main.htm"
elif ProjectName == 'WNDR3400v3':
    urlWirelessSetup = "WLG_wireless_dual_band.htm"	
    urlUSBReadyshareStorage = "USB_adv_main.htm"
    urlUSBAdvancedSetting = "USB_adv_main.htm"
elif ProjectName == 'R6200v2':
    urlRouterStatus = "ADV_home.htm"
    urlPortForwardingTriggering = "FW_forward3.htm"
    Qos = '//tr[30]/td[3]/span}'
    urlUSBReadyshareStorage = "USB_adv_main.htm"
elif ProjectName == 'R6300v2':
    urlRouterStatus = "ADV_home.htm"
    urlPortForwardingTriggering = "FW_forward3.htm"
    Qos = '//tr[30]/td[3]/span'
    urlUSBReadyshareStorage = "USB_adv_main.htm"
elif ProjectName == 'R6300v2':
    urlRouterStatus = "ADV_home.htm"
    urlPortForwardingTriggering = "FW_forward3.htm"
    Qos = '//tr[30]/td[3]/span'
    urlUSBReadyshareStorage = "USB_adv_main.htm"
elif ProjectName == 'R6250':
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    urlRouterStatus = "ADV_home2.htm"		
    urlUSBReadyshareStorage = "USB_adv_main.htm"
elif ProjectName == 'R6400':
    portForwardIntPort = '//tr[2]/td[7]/span'
    portForwardIntIP = '//tr[2]/td[8]/span'
elif ProjectName == 'R6700':
    urlRouterStatus = "ADVANCED_home.htm"
    urlPortForwardingTriggering = "FW_forward3.htm"
    portForwardIntPort = '//tr[2]/td[7]/span'
    portForwardIntIP = '//tr[2]/td[8]/span'
elif ProjectName == 'R6900':	
    urlDeviceName = "DEV_name.htm"
    urlRouterStatus = "ADVANCED_home2.htm"
    TKIPPassword  = 'NOT SUPPORT'		
    AESPassword = "xpath=(//input[@name='security_type'])[3]"	
    MixPassword = "xpath=(//input[@name='security_type'])[4]"
    urlPortForwardingTriggering = "FW_forward3.htm"
elif ProjectName == 'R7000':	
    urlDeviceName = "DEV_name.htm"
    urlRouterStatus = "ADVANCED_home2.htm"
    urlQoSdown = "QOS_down_streaming.htm"
    urlPortForwardingTriggering = "FW_forward3.htm"
    TKIPPassword = 'NOT SUPPORT'		
    AESPassword = "xpath=(//input[@name='security_type'])[3]"	
    MixPassword = "xpath=(//input[@name='security_type'])[4]"
elif ProjectName == 'R7000P':	
    urlRouterStatus = "ADVANCED_home2.htm"
    urlWirelessSetup = "WLG_wireless_dual_band_r10.htm"
    urlGuestNetwork = "WLG_wireless_dual_band_2_r7900.htm"
    urlWirelessSettings = "WLG_adv_dual_band2_r7900.htm"
    turnRomoteManagementOn = "FW_remote.htm"
elif ProjectName == 'R7100LG':	
    urlRouterStatus = "ADVANCED_home2.htm" 
    urlWirelessSettings = "WLG_wireless_dual_band_r10.htm"
    urlGuestNetwork = "WLG_wireless_dual_band_2.htm"
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    AESPassword = "xpath=(//input[@name='security_type'])[3]"	
    MixPassword = "xpath=(//input[@name='security_type'])[4]"
    TKIPPassword = "NOT SUPPORT"	
    portForwardIntPort = "//tr[2]/td[7]/span"
    portForwardIntIP = '//tr[2]/td[8]/span'
elif ProjectName == 'R7300':		 
    urlRouterStatus = "ADVANCED_home2.htm"
    TKIPPassword = 'NOT SUPPORT'	
    AESPassword = "xpath=(//input[@name='security_type'])[3]"	
    MixPassword = "xpath=(//input[@name='security_type'])[4]"
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    urlPortForwardingTriggering = "FW_forward3.htm"
elif ProjectName == 'R7900':		
    urlWirelessSetup = "WLG_wireless_dual_band_r7900.htm"
    urlGuestNetwork = "WLG_wireless_dual_band_2_r7900.htm"
    urlWirelessSettings = "WLG_adv_dual_band2_r7900.htm"
elif ProjectName == 'R8000':	
    urlWirelessSetup = "WLG_wireless_dual_band_r8000.htm"
    TKIPPassword ='NOT SUPPORT}'
    AESPassword = "xpath=(//input[@name='security_type'])[3]}"
    MixPassword = "xpath=(//input[@name='security_type'])[4]"
    urlGuestNetwork = "WLG_wireless_dual_band_2_r8000.htm"
    urlRouterStatus = "ADV_home2_r8000.htm"
    urlWirelessSettings = "WLG_adv_dual_band2_r8000.htm"
    urlPortForwardingTriggering = "FW_forward3.htm"
elif ProjectName == 'R8300':	
    urlRouterStatus = "ADVANCED_home2_tri_band.htm"
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    urlGuestNetwork = "WLG_wireless_tri_band_2.htm"
    urlWirelessSetup = "WLG_wireless_tri_band.htm"
    AESPassword = "xpath=(//input[@name='security_type'])[3]}"
    MixPassword = "xpath=(//input[@name='security_type'])[4]"
elif ProjectName == 'D6220':
    urlRouterStatus = "ADVANCED_home.htm"
    urlInternetSetup = "BAS_basic.htm" 
elif ProjectName == 'D6400':
    urlRouterStatus = "ADVANCED_home.htm"
    urlInternetSetup = "BAS_basic.htm" 
elif ProjectName == 'D8500':
    urlWirelessSetup = "WLG_home.htm"
    urlRouterStatus = "ADVANCED_home.htm"
    urlInternetSetup = "BAS_basic.htm" 
elif ProjectName == 'CBR40':
    urlWirelessSetup = "WLG_wireless2.htm"
    urlRouterStatus = "ADVANCED_home.htm"
    urlInternetSetup = "BAS_basic.htm" 
elif ProjectName == 'VEGN2610':
    urlUSBReadyshareStorage = "USB_adv_main.htm"
    urlInternetSetup = "BAS_basic.htm" 
    urlUSBAdvancedSetting = "USB_adv_main.htm"
elif ProjectName == 'V6510':
    urlUSBReadyshareStorage = "USB_adv_main.htm"
    urlInternetSetup = "BAS_basic.htm" 
elif ProjectName == 'D7000v2':
    urlRouterStatus = "ADVANCED_home.htm"
    urlInternetSetup = "BAS_basic.htm" 
    urlUSBAdvancedSetting = "USB_adv_main.htm"
elif ProjectName == 'DGN2200v4':
    urlWirelessSetup = "WLG_wireless.htm" 
    urlInternetSetup = "BAS_pppoa.htm" 
    urlUSBReadyshareStorage = "USB_adv_main.htm"
    urlUSBAdvancedSetting = "USB_adv_main.htm"
elif ProjectName == 'DGN2200Bv4':
    urlInternetSetup = "BAS_basic.htm" 
    urlWirelessSetup = "WLG_wireless.htm" 
    urlUSBReadyshareStorage = "USB_adv_main.htm"
    urlUSBAdvancedSetting = "USB_adv_main.htm"
elif ProjectName == 'DC112A':
    urlUSBReadyshareStorage = "USB_adv_main.htm"
    urlUSBAdvancedSetting = "USB_adv_main.htm"
elif ProjectName == 'R8500':
    urlInternetSetup = "BAS_basic.htm"	
    urlWirelessSetup = "WLG_home.htm" 
    urlRouterStatus = "ADVANCED_home2_tri_band.htm"
    urlGuestNetwork2G = "WLG_2g_wireless2_2.htm"
    urlGuestNetwork = "WLG_wireless_tri_band_2.htm"
    urlUSBAdvancedSetting = "Readyshare_Storage.htm"
    urlUSBReadyshareStorage = "Readyshare_Storage.htm"
    AESPassword = "xpath=(//input[@name='security_type'])[3]}"
    MixPassword = "xpath=(//input[@name='security_type'])[4]"
elif ProjectName == 'R8000P':
    urlRouterStatus = "ADVANCED_home.htm"
    urlWirelessSetup = "WLG_home.htm" 
elif ProjectName == 'WNR3500Lv2':
    urlWirelessSetup = "WLG_wireless.htm" 
    urlUSBReadyshareStorage = "USB_adv_main.htm"
elif ProjectName == 'C3700-100NAS' or ProjectName == 'C7000-100NAS' or ProjectName == 'C7000v2' or ProjectName == 'C6250-100NAS':
    start = "index.htm"
    urlLogs = "Logs.htm"
    urlInternetSetup = "BasicSettingsBottom.htm" 
    urlWirelessSetup = "WirelessSettings.htm" 
    urlRemoteManagement = "RemoteManagementRetail.htm"
    urlDevicecontrol = "AccessControl.htm"
    urlUSBReadyshareStorage = "USBAdvRetail.htm"
    urlUSBEditStorage = "USBAdvEdit.htm"
    urlRouterStatus = "RouterStatus.htm"
    multilginurl = "MultiLogin.htm"
    urlLANSetup = 'LANSetup.htm'
    urlBlockSites = "BlockSites.htm"
    urlBlockServices = "BlockServices.htm"
elif ProjectName == 'Extender':
    urlLogs = "wifiSettings.html"
    start = "start.htm"
    urlWirelessSetup = "wifiSettings.html" 
    urlUSBReadyshareStorage = "USB_adv_main.htm"
    urlUSBEditStorage = "USBAdvEdit.htm"
    multilginurl = "MNU_access_multiLogin2.htm"
else:
    if console_type == 'cable':
        start = "index.htm"
        urlLogs = "Logs.htm"
        urlInternetSetup = "BasicSettingsBottom.htm" 
        urlWirelessSetup = "WirelessSettings.htm" 
        urlRemoteManagement = "RemoteManagementRetail.htm"
        urlDevicecontrol = "AccessControl.htm"
        urlUSBReadyshareStorage = "USBAdvRetail.htm"
        urlUSBEditStorage = "USBAdvEdit.htm"
        urlRouterStatus = "RouterStatus.htm"
        multilginurl = "MultiLogin.htm"
        urlLANSetup = 'LANSetup.htm'
        urlBlockSites = "BlockSites.htm"
        urlBlockServices = "BlockServices.htm"
    print 'log-url=',urlLogs


host = 'http://' + hostip + '/'
print 'host=',host
