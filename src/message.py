#!/usr/local/bin/python3
import pymsteams 
import sys
import os 

if __name__ == "__main__":
    print("here")
    #grab the connector card first, then perform action
    myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/f1440fea-6baa-450b-b733-72ea9e3bcd1b@99dd3a11-4348-4468-9bdd-e5072b1dc1e6/IncomingWebhook/f58e83d790c04bde8a88ca17e08a8ad3/cd3f2add-89d4-4d63-bc4c-c0eca66f4cc0")

    stream = os.popen(f"/Applications/MATLAB_R2017b.app/bin/matlab -nodesktop -nosplash -r 'cmds=\"{sys.argv[1]}\";disp(eval(cmds));exit;'")
    output = stream.read()

    myTeamsMessage.text(output)

    myTeamsMessage.send()

    last_status_code = myTeamsMessage.last_http_status.status_code
    print(last_status_code)
