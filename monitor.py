#! /usr/bin/env python

"""
file        :   monitor.py
date        :   2014-0201
module      :   monitor
classes     :   
desription  :   main monitor functions
"""
 
import sys, datetime
from sys import argv
from os import system
from urllib2 import urlopen
from socket import socket
from time import asctime
import smtplib, email.utils

from urlparse import urlparse

from sendmail import send_mail


"""
get time in format I like

"""
def get_timestamp():
    
    dt = datetime.datetime.now()
    timestamp = dt.strftime("%Y-%m%d, %X")
    return timestamp

"""
tcp test

:param server_info: server ipor hostname with port
"""
def tcp_test(server_info):
    
    try:
        cpos = server_info.find(':')
        
    except Exception, e:
        print('server info exception: ' + str(e))
    
    try:
        sock = socket()
        sock.connect((server_info[:cpos], int(server_info[cpos+1:])))
        sock.close
        print('tcp_test successful')
        return True
    
    except Exception, e:
        print('socket exception: ' + str(e))
 
"""
http test

:param server_info: server ip or hostname with port, including http:///https://
:returns: boolean value
"""
def http_test(server_info):
    
    try:
        data = urlopen(server_info).read()
        print('http_test successful')
        return True
    
    except Exception, e:
        print(str(e))
 
"""
run server test

:param test_type: test type, eg, tcp or http
:param server_info: server ipor hostname with port
:returns: result object
"""
def server_test(test_type, server_info):
    
    try:
        if test_type.lower() == 'tcp':
            result = tcp_test(server_info)
            return result
        
        elif test_type.lower() == 'http':
            result = http_test(server_info)
            return result
        
        else:
            raise ValueError('valid test types are "tcp" and "http"')
        
    except Exception, exception:
        print('caught exception: ' + str(exception))

# send result by email
# todo: set up sms for text alerts

"""
send result by email

:param test_type: test type, eg, tcp or http
:param server_info: server ipor hostname with port
:param recipient: recipient email address
"""
def send_result(test_type, server_info, recipient):
    
    timestamp = get_timestamp()
    test_result = server_test(test_type, server_info)
    
    try:
        if test_result != False:
            subject = '%s completed successfully: %s, %s' % (test_type.upper(), server_info, timestamp)
            message = '%s completed successfully: %s, %s' % (test_type.upper(), server_info, timestamp)
        
        else:
            subject = 'Error: %s test failed: %s, %s' % (test_type.upper(), server_info, asctime())
            message = 'There was an error while executing a %s test against %s.' % (test_type.upper(), server_info)
            
    except Exception, exception:
        print(str(exception))
        return False
    
    try:
       send_mail(subject, recipient, message)         
       print "Successfully sent email"
       
    except smtplib.SMTPException, smtp_exception:
        print str(smtp_exception)
        print "Error: unable to send email"

# for testing this script can be run at the terminal with args
if __name__ == '__main__':
    
    if 3 > len(argv) > 4:
        print('Wrong number of arguments.')
        
    elif len(argv) == 3:
        server_test(argv[1], argv[2])
        
    else:
        send_result(argv[1], argv[2], argv[3])
