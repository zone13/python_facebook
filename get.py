#!/usr/bin/env python

###########################################################
### Python Script to get the latest post from Facebook Page
### Author: Sid
### https://zone13.io
### Version 1.0
###########################################################

import urllib2, json, base64

def getFacebookPageFeedData(page_id, access_token, num_statuses):
    # Construct the URL string
    base = "https://graph.facebook.com"
    node = "/" + page_id + "/feed" 
    parameters = "/?fields=message,link,created_time,type,name,id,likes.limit(1).summary(true),comments.limit(1).summary(true),shares&limit=%s&access_token=%s" % (num_statuses, access_token) # changed
    url = base + node + parameters

    # Retrieve data
    data = json.loads(request_until_succeed(url))
    return data


def request_until_succeed(url):
    req = urllib2.Request(url)
    success = False
    while success is False:
        try:
            response = urllib2.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception, e:
            print e
            time.sleep(5)
            print "Error for URL %s: %s" % (url, datetime.datetime.now())
    return response.read()

# Populate the Page Id and access token below
page_id = ""
access_token = ""

# Get the latest post
test_status = getFacebookPageFeedData(page_id, access_token, 1)["data"][0]["message"]
print json.dumps(test_status, indent=4, sort_keys=True)

encoded_string = json.dumps(test_status, indent=4, sort_keys=True)[12:-1]

decoded_string = base64.b64decode(encoded_string)

with open("secret_out.zip", "wb") as f:
	f.write(decoded_string)
