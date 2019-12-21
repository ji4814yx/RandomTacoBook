import requests # to get the url
from PIL import Image, ImageDraw, ImageFont   # use of pillow to import and edit image
url = 'https://api.unsplash.com/photos/random' # get the url with access key as client id
auth_url = 'https://unsplash.com/oauth/token' # get the authorized url with a specific token
# access key
client_id = 'b82ee7fea9c0dd726586f928f79cdcde9032dcaa2da4fc2101ddf72d0a1b2a29' # define my client ID value
secret_key = '5b8e2b3a8187b51e49525fb720ecfcc7eb281439c07ee12d4b79e315e8d6de67' # define the secret key parameter
query_params = {'client_id': client_id, 'query':'taco', 'orientation':'squarish'} # define the
# query parameter using access key, access key, secret key and the authorization code
response = requests.get(url, params=query_params).json() # convert Json response to dictionary

print(response) # print response
img_url = 'https://api.unsplash.com/users/mnelson/photos'
#img_query_params = {'client_id': client_id, 'query':'BytesIO'}
img_response = requests.get(img_url, params=query_params).json()
print(img_response)

# def readBytes(filename, nBytes):
#     # 'rb' raed in binary mode
#     with open(filename, 'rb') as file:
#         while True:
#             byte = file.read(1)
#             if byte:
#                 yield byte
#             else:
#                 break
#
# for b in readBytes('photo.jpg', 5):
#     i = int.from_bytes(b, byteorder = 'big')
#
#     print(f"raw({b} - int({i} -binary({bin(i)}")
#





# auth_response = requests.get(auth_url, params=query_params).json()
# print(auth_response)

# we are missing the redirect
#auth_response = requests.post(auth_url, params=query_params).json() #
# query_params = {'client_id': access_key, 'client_secret': secret_key, 'grant_type': 'authorization_code'}
#url = 'https://api.unsplash.com/photos/?client_id=YOUR_ACCESS_KEY'