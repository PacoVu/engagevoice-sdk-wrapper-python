from engagevoice.sdk_wrapper import *

RC_CLIENT_ID=""
RC_CLIENT_SECRET=""

RC_USERNAME=""
RC_PASSWORD=""
RC_EXTENSION=""

# Use call back
def callback(response):
    print (response._content)

def get_agent_states():
    endpoint = "admin/accounts/~/realTimeData/agent"
    try:
        ev.get(endpoint, None, callback)
    except Exception as e:
        print (e)


ev = RestClient(RC_CLIENT_ID, RC_CLIENT_SECRET)
try:
    resp = ev.login(RC_USERNAME, RC_PASSWORD, RC_EXTENSION)
    if resp:
        get_agent_states()
except Exception as e:
    print (e)
