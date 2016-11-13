import httplib, urllib, base64
import json

def get_strongest_emotion(raw_result):
    """
        Returns:
            The strongest emotion in image or if there's multiple faces a list representing
                strongest emotion in each face is returned.
        MIT liscence for this function from https://github.com/zooba/projectoxford
    """

    num_faces, res = len(raw_result), raw_result
    if num_faces < 1:
        return None
    elif num_faces == 1:
        return max(res[0]['scores'], key=(lambda s: res[0]['scores'][s]))
    else:
        return [max(face['scores'], key=(lambda s: face['scores'][s])) for face in res]

def processRequest( json, data, headers, params ):

    """
    Helper function to process the request to Project Oxford

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """

    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429: 

            print( "Message: %s" % ( response.json()['error']['message'] ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['error']['message'] ) )

        break
        
    return result

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9d317db38ed24d859240f407b2e02867',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    link = "https://reactonfly.blob.core.windows.net/images/filename4.jpg"
    d = json.dumps({"url": link})
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, d, headers)
    response = conn.getresponse()
    data = response.read()
    print data
    print get_strongest_emotion(json.loads(data))
    conn.close()
except Exception as e:
    print e
