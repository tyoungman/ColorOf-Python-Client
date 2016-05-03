import requests

API_KEY="<get api key from colorof>"
API_SECRET="<get api key from colorof>"
API_SERVER="http://api.colorof.com"

#Obtain an token from the server to make authenticated requests  
def getAuthToken():

	#Define Authentication request parameters and authentication token endpoint
	AUTH_PARAMS= { 
 		'api_key' : API_KEY, 
 		'api_secret' : API_SECRET, 
	}
	url = API_SERVER + "/auth/token"

	#Make authentication request and return token
	r = requests.post(url, AUTH_PARAMS)
	
	if(r.status_code == 200):
		token = r.json().get("token")
		if token is not None and len(token) > 0:
			return token

	#Either the return code or token was invalid		
	print "Unsuccessful authentication request"
	print(r.url)
	print(r.text)
	print(r.headers)

#Upload a Colorof swatch
def uploadSwatch(token):

	PARAMS= { 
	'name' : 'EHEIM Everyday Fish Feeder Programmable Automatic Food Dispenser', 
	'desc' : "EHEIM Everyday Fish Feeder Programmable Automatic Food Dispenser", 
	'link' : "http://www.amazon.com/Everyday-Feeder-Programmable-Automatic-Dispenser/dp/B001F2117I/", 
	'image_link' : "http://ecx.images-amazon.com/images/I/51RvfhaC92L.jpg",
	'image_link2' : "http://ecx.images-amazon.com/images/I/51RvfhaC92L.jpg", 
	'uid':"2498221",
	'gravity':"NorthWest"}

	url = API_SERVER + "/swatches"
	myheaders = {'Cookie': "at="+token}

	r = requests.post(url + "/format/json", PARAMS,None,headers=myheaders)

	print(r.url)
	print(r.text)
	print(r.headers)
	print(r.request.headers)
	print(r.history)

	#Detect if response was successful and return the swatch_id
	if (r.status_code == 200 and r.headers['Content-Type'] == 'application/json'):
		return r.json().get("swatch_id")
	else:
		print "Unexpected response from server"


#Make an update to the swatch name and description
def updateSwatch(token,swatch_id):

	PARAMS= { 
	'name' : 'UPDATED EHEIM Everyday Fish Feeder Programmable Automatic Food Dispenser', 
	'desc' : 'UPDATED EHEIM Everyday Fish Feeder Programmable Automatic Food Dispenser', 
	'link' : "http://www.amazon.com/Everyday-Feeder-Programmable-Automatic-Dispenser/dp/B001F2117I/"
	}

	url = API_SERVER + "/swatches/%d/format/json" % swatch_id	

	myheaders = {'Cookie': "at="+token}
	r = requests.put(url, PARAMS,headers=myheaders)

	print(r.url)
	print(r.text)
	print(r.headers)
	print(r.request.headers)

#Delete swatch by id
def deleteSwatch(token,swatch_id):
	url = API_SERVER + "/swatches/%d/format/json" % swatch_id

	myheaders = {'Cookie': "at="+token}
	r = requests.delete(url, headers=myheaders)

	print(r.url)
	print(r.text)
	print(r.headers)
	print(r.request.headers)


#Display some information about the swatch we just entered
def printSwatch(swatch_id):
	url = API_SERVER + "/swatches/%d/format/json" % swatch_id 
	r = requests.get(url)
	print(r.text)
	print(r.url)


token = getAuthToken()
print(token)
if token is not None:
	#test(token)
	swatch_id = uploadSwatch(token)

	if swatch_id is not None:
		#Display details about the swatch
		printSwatch(swatch_id)

		#Update the swatch description
		updateSwatch(token, swatch_id)	

		#Display details about the swatch - should reflect updates
		printSwatch(swatch_id)
		
		#Delete swatch
		deleteSwatch(token,swatch_id)
		
