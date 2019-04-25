
'''
import googlemaps
#from googlemaps import Client as GoogleMaps

gmaps = googlemaps.Client(key='')

nearby_places = gmaps.places_nearby((22.281033, 114.155556))
print(nearby_places)
'''

import requests
import json
import time

def getCountFromAPI(latitude, longitude, radius, feature):

    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(latitude) + ',' + str(longitude) + '&radius=' + \
        str(radius) + '&type=' + feature + '&key='
    #print(url)

    response = requests.get(url)
    count = 0

    if (response.ok):
        #jsonResponse = json.loads(response.content)
        jsonResponse = response.json()
        '''
        if 'next_page_token' not in jsonResponse:
            print("next_page_token not found")
        else:
        '''
        nextPageToken = jsonResponse['next_page_token'] 
        results = jsonResponse['results']

        for i in range(len(results)):
            #print(results[i]['place_id'])
            count += 1
        
        while nextPageToken is not None:
            time.sleep(5)
            newUrl = url + '&pagetoken=' + str(nextPageToken)
            response = requests.get(newUrl)
            jsonResponse = response.json()
            #print(jsonResponse)
            if (response.ok):
                results = jsonResponse['results']
                for i in range(len(results)):
                    count += 1
                
                try:
                    nextPageToken = jsonResponse['next_page_token']
                except:
                    print('Next page token not found')
                    break
                #if 'next_page_token' not in jsonResponse:
                #    break
                #if 'data' not in data['to']:
                #    raise ValueError("No data for target")
                print(nextPageToken)
                print(count)
            else:
                print("Invalid response")
                break
    else:
        print(response.status_code)

    print(count)
    return count


'''
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=22.281033,114.155556&radius=2000&type=restaurant&key='
response = requests.get(url)

if (response.ok):
    jData = json.loads(response.content)
    #print(jData)
    results = response.json()['results']
    print(response.json()['next_page_token'])
    count = 0
    #placeIds = jData['results']['place_id']
    for i in range(len(results)):
        #print(results[i]['place_id'])
        count += 1
    print(count)
'''


if __name__ == "__main__":
    getCountFromAPI(22.281033, 114.155556, 2000, 'restaurant')