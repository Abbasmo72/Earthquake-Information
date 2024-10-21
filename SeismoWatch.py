
import json
import urllib.request 

def printResults(data):
   
    theJSON = json.loads(data)
    
    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])
    
    count = theJSON['metadata']['count']
    print(count, 'events recorded')
    
    for i in theJSON['features']:
        print(i['properties']['place'])
    print('---------------------')

    for i in theJSON['features']:
        if i ['properties']['mag'] >= 4.0:
            print(i['properties']['place'])
    print('---------------------')

    print('\n Events that were felt:')
    for i in theJSON['features']:
        feltReports = i['properties']['felt']
        if feltReports != None:
            if feltReports > 0:
                print(i['properties']['place'], feltReports, 'times')
def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
    if(webUrl.getcode()) == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print('Received an error from the server, cannot print results', webUrl.getcode())
if __name__ == "__main__":
    main()
