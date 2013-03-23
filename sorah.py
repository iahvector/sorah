#!/usr/bin/python

import os
import urllib
import hashlib
import xml.etree.ElementTree as et

user_name = os.getlogin()
sorah_dir = "/home/" + user_name + ".sorah"
sorah_config = "/home/" + user_name + ".sorah/config"

if os.path.isdir(sorah_dir):
    if os.path.isfile(sorah_config):
        tree = et.parse(sorah_config)
        user = tree.getroot()
        email = user.findall("email[1]")

        email_hash = hashlib.md5(email.lower()).hexdigest()
        params = urllib.urlencode({'d': '404'})
        url = "http://www.gravatar.com/avatar/" + email_hash + "?" + params
        image_path = "/var/lib/AccountsService/icons/" + user_name

        # Check connection success
        urllib.urlretrieve(url, image_path)
    else:
        # issue notification to update user settings
else:
    # issue notification to update user settings
