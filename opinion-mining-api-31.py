import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '3f7e7a5c8aaa4e5fa43ae374eb922ffb',
}

params = urllib.parse.urlencode({
    # Request parameters
    'showStats': '{boolean}',
    'model-version': '{string}',
})

try:
    conn = http.client.HTTPSConnection('southcentral.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v3.1-preview.1/sentiment?opinionMining=true%s" %params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))