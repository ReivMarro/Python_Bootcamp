import requests

req = requests.get("https://kalob.io")
print(req.status_code) # The result will be 200, which shows that the website is running normally

# Above there is a very easy check on a website, but this command can be use to monitor or alert on the status of a website

import requests
import time
while True:
    req = requests.get("https://github.com/ReivMarro")
    print(req.status_code) # After this we can create an alert in case the site drops below 200
    if req.status_code != 200:
        # Here anything such 'Email me' or 'Text me' could be created to alert someone
        pass
    time.sleep(60) # This will constantly pull the site to make sure that it is up all the time

    # This is an uptime monitoring program
    