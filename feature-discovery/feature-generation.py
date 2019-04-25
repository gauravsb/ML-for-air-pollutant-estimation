import csv
from collections import defaultdict
import time

columns = defaultdict(list)

with open('HKLURDataset.csv') as f:
    reader = csv.DictReader(f) 
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v) 

a = columns['SiteID']
b = columns['Lat']
c = columns['Long']

for i in range(len(a)):
    Site_id = a[i]
    Lat = b[i]
    Long = c[i]

from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = ''
google_places = GooglePlaces(YOUR_API_KEY)

def writeToCSVFile(rowList):
    with open('output.csv', mode='w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Lat', 'Long','Rest.1000'])
        for string in rowList:
            writer.writerow(string)

def restaurant_count(latitude,longitude,feature,rad):
    # 22.30871
    # 114.183472
    #print(latitude, longitude)
    if feature == 'restaurant':
        query_result = google_places.nearby_search(
            lat_lng={'lat': latitude, 'lng': longitude}, 
            radius=rad, 
            types=[types.TYPE_RESTAURANT])
        
        #if query_result.has_attributions:
        #print(query_result.html_attributions)
        count = 0
        for place in query_result.places:
            #print(place.place_id)    
            count += 1    
            
        #print(count)
        while query_result.has_next_page_token:
            time.sleep(5)
            query_result = google_places.nearby_search(
                lat_lng={'lat': latitude, 'lng': longitude}, 
                radius=rad, types=[types.TYPE_RESTAURANT], 
                pagetoken=query_result.next_page_token)
            
            for place in query_result.places:
                #print(place.place_id) 
                count += 1
            #print(count)
    #print(latitude, longitude, count)
    return count

resultList = []
for i in range(len(b)):
    count = restaurant_count(b[i],c[i],'restaurant',1000)
    #print(count)
    res = str(b[i]) + "," + str(c[i]) + "," + str(count)
    print(res)
    resultList.append(res)
    
writeToCSVFile(resultList)