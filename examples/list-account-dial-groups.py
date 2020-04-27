from engagevoice.sdk_wrapper import *

RC_CLIENT_ID=""
RC_CLIENT_SECRET=""

RC_USERNAME=""
RC_PASSWORD=""
RC_EXTENSION=""

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
    print ("get_account_dial_group()")
    endpoint = "admin/accounts/~/dialGroups/" + groupId
    try:
        ev.get(endpoint, None, callback)
    except Exception as e:
        print (e)

ev = RestClient(RC_CLIENT_ID, RC_CLIENT_SECRET)
try:
    resp = ev.login(RC_USERNAME, RC_PASSWORD, RC_EXTENSION)
    if resp:
        get_account_dial_groups()
except Exception as e:
    print (e)
