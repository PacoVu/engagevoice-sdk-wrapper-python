import sys
from engagevoice.sdk_wrapper import *

RC_CLIENT_ID=""
RC_CLIENT_SECRET=""

RC_USERNAME=""
RC_PASSWORD=""
RC_EXTENSION=""

def list_account_agent_groups():
    try:
        endpoint = 'admin/accounts/~/agentGroups'
        response = ev.get(endpoint, None, None)
        print (response)
    except Exception as e:
        print (e)

ev = RestClient(RC_CLIENT_ID, RC_CLIENT_SECRET)
try:
    resp = ev.login(RC_USERNAME, RC_PASSWORD, RC_EXTENSION)
    if resp:
        list_account_agent_groups()
except Exception as e:
    print (e)
