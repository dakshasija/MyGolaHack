import requests
import sys
import json

def get_searched_places(place):    
    base_url = "https://api.foursquare.com/v2/venues/explore?client_id=MDREIXWEKU15QLSRJAH12CAWB4S4MTJEGDM3JYZPIALRJ5WJ&client_secret=PHQLBL3QSZMATWV30XN0H54V35N0U02TH53GB0T54AEFS1TA&v=20130815&near={place}&radius=5000&limit=30"
    req = requests.get(base_url.format(place=place))
    return req.text

        
            
if __name__ == '__main__':
    places = get_searched_places("Pune")#str(sys.argv[1]))

places=json.loads(places)
print places
place_list = []

for i in places["response"]["groups"][0]["items"]:
        try:
            d = {"id":i["venue"]["id"],"lat":i["venue"]["location"]["lat"],"lng":i["venue"]["location"]["lng"],"name":i["venue"]["name"],"checkins":i["venue"]["stats"]["checkinsCount"],"userscount":i["venue"]["stats"]["usersCount"],"tip_count":i["venue"]["stats"]["tipCount"],"rating":i["venue"]["rating"],"tips":i["tips"]}
            d = json.dumps(d)
            place_list.append(d)
        except KeyError:
            pass

print place_list
sys.stdout.flush()
