import sys
from engagevoice.sdk_wrapper import *

RC_CLIENT_ID=""
RC_CLIENT_SECRET=""

RC_USERNAME=""
RC_PASSWORD=""
RC_EXTENSION=""

LEGACY_USERNAME= ""
LEGACY_PASSWORD= ""

MODE = "ENGAGE"

def list_account_agent_groups():
    try:
        endpoint = 'admin/accounts/~/agentGroups'
        response = ev.get(endpoint, None, None)
        print (response)
    except Exception as e:
        print (e)

if (MODE == "ENGAGE"):
    ev = RestClient(RC_CLIENT_ID, RC_CLIENT_SECRET)
    username= RC_USERNAME
    password = RC_PASSWORD
    extensionNum = RC_EXTENSION
else:
    ev = RestClient();
    username= LEGACY_USERNAME
    password = LEGACY_PASSWORD
    extensionNum = ""

try:
    resp = ev.login(username, password, extensionNum)
    if resp:
        list_account_agent_groups()
except Exception as e:
    print (e)
