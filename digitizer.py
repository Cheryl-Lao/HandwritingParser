import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, time, json

import sys.argv

# This is based heaily on the tutorial on https://nordicapis.com/digitize-your-notes-with-microsoft-vision-api/


#---Setting up the connection---
# Keys
endpoint = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0'
api_key = 'cf70bc8dedd748edb657e9ad81555a73'

# HTTP request to send to the API
# Look at the RecognizeText function from Microsoft
headers = {
    # Request headers.
    # Another valid content type is "application/octet-stream".
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': api_key,
}

body = {'url' : 'https://www.gratefulleadership.com/wp-content/uploads/2013/01/Micahel-Case-Thank-You-2-e1359407348712.jpg'}
#body = {'url':'http://i.imgur.com/W2fF6uC.jpg'}

#If you set the handwriting param to be false, it will OCR the text instead
params = {'handwriting' : 'true'}


#---Handwriting analysis---
#try sending the image to the CV API
try:
    response = requests.request('POST', endpoint + '/RecognizeText', json=body, data=None, headers=headers, params=params)

    #error checking
    if response.status_code != 202:
        # Display JSON data and exit if the REST API call was not successful.
        parsed = json.loads(response.text)
        print ("Error:")
        print (json.dumps(parsed, sort_keys=True, indent=2))
        exit()

    # grab the 'Operation-Location' from the response
    operationLocation = response.headers['Operation-Location']

    #It will take a little bit to load
    print('\nHandwritten text submitted. Waiting 10 seconds to retrieve the recognized text.\n')
    time.sleep(10)


    # Execute the second REST API call and get the response.
    response = requests.request('GET', operationLocation, json=None, data=None, headers=headers, params=None)

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(response.text)

    # Get the transcribed lines of text
    lines = parsed['recognitionResult']['lines']

    #parsed['recognitionResult']['lines'] contains an array of all the lines of processed text. We can print those out now:
    for line in lines:
        print (line['text'])

except Exception as e:
    print('Error:')
    print(e)

# this opens the file for writing
with open("mynote.txt", "w") as f:
    for line in lines:
        print(line['text'])
        # write the value to the file
        f.write(line['text'])
