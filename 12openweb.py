#AIM: open a webpage using the urlib library.
#prerequisite: Install urllib in python
import urllib.request 
request_url = urllib.request.urlopen('https://cbse.nic.in/') 
print(request_url.read()) 
