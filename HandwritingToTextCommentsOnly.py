import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, time, json

import sys

# This is based heaily on the tutorial on https://nordicapis.com/digitize-your-notes-with-microsoft-vision-api/

#####Comment Version#####
#---Setting up the connection---
# Keys
endpoint = 

#Replace this with your API key!!!
api_key = 

# HTTP request to send to the API
# Look at the RecognizeText function from Microsoft
headers = {
    # Request headers.
}

#Gets the first argument as the url of the picture to process
body = {}

#If you set the handwriting param to be false, it will use OCR on the text instead (NOT good for handwritten text). 
params = {}

#---Handwriting analysis---
#Try sending the image to the CV API
try:
    #Make a request to the API
    response = requests.request()

    #202 is the success status code
    if response.status_code != 202:
        # Display JSON data and exit if the REST API call was not successful.


    # grab the 'Operation-Location' from the response
    operationLocation = response.headers['Operation-Location']

    #It will take a little bit of time to load so just make the user wait


    # GET the response.
    response = requests.request()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(response.text)

    # Get the transcribed lines of text
    lines = parsed['recognitionResult']['lines']

    #parsed['recognitionResult']['lines'] contains an array of all the lines of processed text. We can print those out now:

#Catch any exceptions that might happen
except Exception as e:


# This opens the file specified by the second argument for writing
with open(sys.argv[2], "w") as f:
    for line in lines:
        # write the value to the file
        