from engagevoice.sdk_wrapper import *

RC_CLIENT_ID=""
RC_CLIENT_SECRET=""

RC_USERNAME=""
RC_PASSWORD=""
RC_EXTENSION=""

LEGACY_USERNAME= ""
LEGACY_PASSWORD= ""

MODE = "ENGAGE"

# Use call back
def callback(response):
    print (response._content)

def get_agent_states():
    endpoint = "admin/accounts/~/realTimeData/agent"
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
        get_agent_states()
except Exception as e:
    print (e)
