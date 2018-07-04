import sys
import requests
import json

movie_title = sys.argv[1]
plot = 'full'

# credentials
api_base_url = 'http://www.omdbapi.com/?apikey=ec5d517a'
url = api_base_url + '&t=' + movie_title + '&plot=' + plot

response = requests.get(url)

if response.status_code is 200:
    movie_data = response.json()

    # print('Plot :')
    # print(movie_data['Plot'])
    for (key, value) in movie_data.items():
        print(key + ' : '+ str(value))
else:
    print('Error : ' + str(response.status_code))
