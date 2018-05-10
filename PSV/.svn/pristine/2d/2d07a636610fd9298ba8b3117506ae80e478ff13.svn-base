'''Validation test'''
'''[PSV-2017-2018] RCE:stack overflow in /usb_umount.cgi through "select1" parameter'''

from API._API import *

def test_Step_1():
    token = getIDToken('USB_umount.htm')
    log.info( 'Step-1: Set select1(Type:NUM, MaxLen:2) = 1')
    post_url = host  + 'usb_umount.cgi' + token
    post_data = 'Apply=Apply&choice=yes&num=0&umountsucc=3&select1=0&select2=-1&select3=-1&select4=-1'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    
    assert tmpHTML.status_code == 200, "This action should work." 
    
def test_Step_2():
    token = getIDToken('USB_umount.htm')
    log.info( 'Step-2: Set select1(Type:NUM, MaxLen:2) = 99')
    post_url = host  + 'usb_umount.cgi' + token
    post_data = 'Apply=Apply&choice=yes&num=0&umountsucc=3&select1=99&select2=-1&select3=-1&select4=-1'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_3():
    token = getIDToken('USB_umount.htm')
    log.info( 'Step-3: Set select1(Type:NUM, MaxLen:2) = -1')
    post_url = host  + 'usb_umount.cgi' + token
    post_data = 'Apply=Apply&choice=yes&num=0&umountsucc=3&select1=-1&select2=-1&select3=-1&select4=-1'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 200:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    
    assert tmpHTML.status_code == 200, "This action should work." 

def test_Step_4():
    token = getIDToken('USB_umount.htm')
    log.info( 'Step-4: Set select1(Type:NUM, MaxLen:2) = 100')
    post_url = host  + 'usb_umount.cgi' + token
    post_data = 'Apply=Apply&choice=yes&num=0&umountsucc=3&select1=100&select2=-1&select3=-1&select4=-1'
    tmpHTML = requests.post(post_url, data=post_data, headers=headers, verify=False)
    if tmpHTML.status_code == 400:
        log.info(tmpHTML)
        log.info( "Action Successful, sleep 3s")
    
    assert tmpHTML.status_code == 400, "This action should work." 

