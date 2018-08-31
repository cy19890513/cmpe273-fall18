# https://webhook.site/#/33879aac-dfa3-43d8-acb0-ae23bf9e847a/2055f03b-0bc8-4e66-9b99-921e629ad80b/0

import requests



r1 = requests.get('https://webhook.site/33879aac-dfa3-43d8-acb0-ae23bf9e847a')


print ('First Call Date '+ r1.headers['Date'])


r2 = requests.get('https://webhook.site/33879aac-dfa3-43d8-acb0-ae23bf9e847a')

print ('Second Call Date '+ r2.headers['Date'])

r3 = requests.get('https://webhook.site/33879aac-dfa3-43d8-acb0-ae23bf9e847a')


print ('Third Call Date '+ r3.headers['Date'])
