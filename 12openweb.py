#AIM: open a webpage using the urllib library.
#prerequisite: Install urllib in python
import urllib.request 
request_url = urllib.request.urlopen('http://cbse.nic.in/') 
print(request_url.read()) 
