import requests

#Examples of Unauthenticated request to Colorof API
#python colorof-client.py

#Search - GET /search

#Define parameter array. http://api.colorof.com has more details on search fields
PARAMS= { 
    'query' : "flower", 
    'hex' : "e29f11", 
    'accuracy' : "4", 
    'format' : "json",
    'user_id' : "", 
    'search_by':"swatch"}

URL="http://api.colorof.com/search"

#Send a request to server and print out results
r = requests.get(URL,PARAMS)
print(r.url)
print(r.text)


#Display swatch details GET /swatches
URL="http://api.colorof.com/swatches/69001/format/json"

#Send a request to server and print out results
r = requests.get(URL)
print(r.url)
print(r.text)


#Faceted Search Step 1, get bucket IDs (facets) - GET /search

#Define parameter array. http://api.colorof.com has more details on search fields
PARAMS= { 
    'query' : "flower", 
    'hex' : "e29f11", 
    'facet' : "True",
    'accuracy' : "4", 
    'format' : "json",
    'user_id' : "", 
    'search_by':"swatch"}

URL="http://api.colorof.com/search"

#Send a request to server and print out results
r = requests.get(URL,PARAMS)
print(r.url)
print(r.text)

#Faceted Search Step 2, search / display swatches in a bucket - GET /search

#Define parameter array. http://api.colorof.com has more details on search fields
PARAMS= { 
    'query' : "flower", 
    'hex' : "None", 
    'accuracy' : "4", 
    'format' : "json",
    'bucket_id' : "1065",
    'user_id' : "", 
    'search_by':"swatch"}

URL="http://api.colorof.com/search"

#Send a request to server and print out results
r = requests.get(URL,PARAMS)
print(r.url)
print(r.text)



