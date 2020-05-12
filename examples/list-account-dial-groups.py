from engagevoice.sdk_wrapper import *

RC_CLIENT_ID=""
RC_CLIENT_SECRET=""

RC_USERNAME=""
RC_PASSWORD=""
RC_EXTENSION=""

LEGACY_USERNAME= ""
LEGACY_PASSWORD= ""

MODE = "ENGAGE"

def get_account_dial_groups():
    print ("get_account_dial_groups()")
    try:
        endpoint = "admin/accounts/~/dialGroups"
        response = ev.get(endpoint, None, None)
        print (response)
    except Exception as e:
        print (e)

#Returns a dial group for an account
def get_account_dial_group(groupId):
    endpoint = "admin/accounts/~/dialGroups/" + groupId
    try:
        ev.get(endpoint, None, callback)
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
        get_account_dial_groups()
except Exception as e:
    print (e)
