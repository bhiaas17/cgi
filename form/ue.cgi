#!/usr/bin/python 
import cgi 
import cgitb 
cgitb.enable()

print "content-type:text/html"
print ""

d=cgi.FieldStorage()
d1=d.getvalue('user')
d2=d.getvalue('email')
print d1
print d2
