import requests
import sys

def get_topPicks(lat,longi):    
    base_url = "https://api.foursquare.com/v2/venues/explore?client_id=MDREIXWEKU15QLSRJAH12CAWB4S4MTJEGDM3JYZPIALRJ5WJ&client_secret=PHQLBL3QSZMATWV30XN0H54V35N0U02TH53GB0T54AEFS1TA&v=20130815&ll={lati},{longi}&limit=30"
    req = requests.get(base_url.format(lati=lat,longi=longi))
    return req.json()

if __name__ == '__main__':
    print get_topPicks("12.912248","77.642369")#str(sys.argv[1]),str(sys.argv[2])


sys.stdout.flush()
