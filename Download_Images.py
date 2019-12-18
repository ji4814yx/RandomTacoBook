import requests # to get the url
url = 'https://api.unsplash.com/photos/?client_id=YOUR_ACCESS_KEY' # get the url with access key as client id
auth_url = 'https://unsplash.com/oauth/token' # get the authorized url with a specific token
# access key
access_key = 'b82ee7fea9c0dd726586f928f79cdcde9032dcaa2da4fc2101ddf72d0a1b2a29' # define the access key parameter
secret_key = '5b8e2b3a8187b51e49525fb720ecfcc7eb281439c07ee12d4b79e315e8d6de67' # define the secret key parameter
query_params = {'client_id': access_key, 'client_secret': secret_key, 'grant_type': 'authorization_code'} # define the
# query parameter using access key, access key, secret key and the authorization code
auth_response = requests.post(auth_url, params=query_params).json() #
print(auth_response)

# we are missing the redirect