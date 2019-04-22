import urllib.request, json

key = '' #Insert your API key here
apiURL = 'https://api.clashroyale.com/v1'

#Create the API request
request = urllib.request.Request(
    apiURL + '/cards', #In this example, we will request to view all Clash Royale cards available
    headers={'Authorization': 'Bearer %s' % key}
)

#Send the API request
response = urllib.request.urlopen(request).read()

#Load and pretty print the API response
data = json.loads(response)
print(json.dumps(data, indent=4))
