# 118945b975e51def3231f6d0e770589833

import requests
import time
import sys

job_name = sys.argv[1]
API_TOKEN = sys.argv[2]
USER = "telware"

JENKINS_URL = "https://jenkins.telware.tech/job/" + job_name

while True:
    response = requests.get(f"{JENKINS_URL}/lastBuild/api/json", auth=(USER, API_TOKEN))
    data = response.json()

    if data.get('building'):
        print("Build is still running...")
    elif data.get('result') == 'FAILURE':
        print("Build failed!")
        exit(1)
    elif data.get('result') == 'SUCCESS':
        print("Build succeeded!")
        exit(0)

    time.sleep(10)  
