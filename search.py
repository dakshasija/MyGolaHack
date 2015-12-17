import requests
import sys

def get_searched_places(place):    
    base_url = "https://api.foursquare.com/v2/venues/explore?client_id=MDREIXWEKU15QLSRJAH12CAWB4S4MTJEGDM3JYZPIALRJ5WJ&client_secret=PHQLBL3QSZMATWV30XN0H54V35N0U02TH53GB0T54AEFS1TA&v=20130815&near={place}&section=topPicks&limit=10"
    req = requests.get(base_url.format(place=place))
    return req.json()


print get_searched_places(str(sys.argv[1]))
sys.stdout.flush()
