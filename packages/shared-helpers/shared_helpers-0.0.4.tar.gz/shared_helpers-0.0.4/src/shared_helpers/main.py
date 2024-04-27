import variables
from yandex.organization.organization_helper import CloudHelper
from yandex.tracker.tracker_helper import TrackerHelper
from lm.sbbid.sbbid_helper import SbbIdHelper
from functions import TokenHelper

token_helper = TokenHelper()

def fetch_current_iam_token() -> str:
    """Fetch a valid IAM token or return None."""
    token = None
    if (
        variables.SA01_IAM_TOKEN and
        variables.SA01_IAM_TOKEN_EXPIRY and
        int(variables.SA01_IAM_TOKEN_EXPIRY) <300
    ):
        token = variables.SA01_IAM_TOKEN
    elif (variables.SA01_API_KEY and variables.SA01_CF_ENDPOINT_URL):
        token = token_helper.get_iam_token_from_endpoint(api_key=variables.SA01_API_KEY, endpoint_url=variables.SA01_CF_ENDPOINT_URL)
    elif token_helper.file_exists(json_file_path=variables.SA01_JSON_FILE_PATH):
        token = token_helper.get_iam_token_from_file(json_file_path=variables.SA01_JSON_FILE_PATH)
    return token

if token := fetch_current_iam_token():
    cloud_client = CloudHelper(token)
    tracker_client = TrackerHelper(token)
sbbid_client = SbbIdHelper(x_api_key=variables.SBBID_X_API_KEY, environment = variables.SBBID_ENVIRONMENT)

#print(cloud_client.cloud_get_all_groups())
#print(tracker_client.queues_get_queues())
#print(sbbid_client.get_domains())