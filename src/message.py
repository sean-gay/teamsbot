#!/usr/local/bin/python3
import pymsteams 
import sys
import os 

if __name__ == "__main__":
    print("here")
    #grab the connector card first, then perform action
    myTeamsMessage = pymsteams.connectorcard("<URL>")

    stream = os.popen(f"<MATLAB PATH> -nodesktop -nosplash -r 'cmds=\"{sys.argv[1]}\";disp(eval(cmds));exit;'")
    output = stream.read()

    myTeamsMessage.text(output)

    myTeamsMessage.send()

    last_status_code = myTeamsMessage.last_http_status.status_code
    print(last_status_code)
