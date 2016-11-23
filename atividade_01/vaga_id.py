"""
Nov 11 2016 11:15PM

@author: Pedro Garcia
"""


import json
import requests


url = "http://ec2-35-164-139-210.us-west-2.compute.amazonaws.com"
response = requests.get(url)
print(response.json())