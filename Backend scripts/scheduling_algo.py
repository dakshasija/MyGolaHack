import requests
import four_square
from operator import itemgetter, attrgetter, methodcaller
import itertools
import math
import json

class Place:
    def __init__(self,d):
        self.dic = d
        self.name = d["name"]
        self.type = d["type"]
        self.lat = d["lat"]
        self.lng = d["lng"]
        self.checkins=d["checkins"]
        self.userscount=d["userscount"]
        self.tip_count= d["tip_count"]
        self.rating = d["rating"]
        self.tips = d["tips"]
        self.contact = d["contact"]
        self.open_hours = d["open_hours"]
    def __repr__(self):
             return repr(self.name)
import math
 
def length(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.
         
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    if(cos<=-1):
        cos = -1
    elif(cos>=1):
        cos = 1
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    rho = 6373 ###Radius of earth
    ################################TENTATIVE DISTANCE FOR ESTIMATION#####################################
    return arc*rho





def solve_tsp_dynamic(all_distances):
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(all_distances)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[1]#######<------------------- ORDER FOR TRAVELING WHERE 0 is starting point


def plan_my_day(places,lat,lng,hours):
    ######################################################
    places_list =[]
    for i in places["response"]["groups"][0]["items"]:
        try:
            d = {"id":i["venue"]["id"],"lat":i["venue"]["location"]["lat"],"lng":i["venue"]["location"]["lng"],"name":i["venue"]["name"],"checkins":i["venue"]["stats"]["checkinsCount"],"userscount":i["venue"]["stats"]["usersCount"],"tip_count":i["venue"]["stats"]["tipCount"],"rating":i["venue"]["rating"],"tips":i["tips"]}

            try:
                d["open_hours"]=i["venue"]["hours"]["status"]
            except KeyError:
                d["open_hours"] = "10 am"
            try:
                d["contact"]=i["venue"]["contact"]
            except KeyError:
                d["contact"]=""
            try:
                d["type"] = i["venue"]["categories"][0]["name"]
            except KeyError:
                pass
            places_list.append(Place(d))
        except KeyError:
            pass

    sorted(places_list, key=attrgetter('rating'),reverse=True)
    start_time = raw_input("Start time for today In 24 hrs format")
    end_time = raw_input("End time for today In 24 hrs format")
    n =  int(end_time) - int(start_time)
    final_list = places_list[hours:hours+n]
    hours = hours + n
     #####by hour #####
    matrix = [[length(X.lat,X.lng,Y.lat,Y.lng) for Y in final_list] for X in final_list]
    #matrix.append([length(Y.lat,Y.lng,lat,lng) for Y in places_list])
    order = solve_tsp_dynamic(matrix)
    res = []
    time_now = int(start_time)
    print order
    for i in order:
        if(time_now<5):
            print "Its Probably your nap time"
            break
        res.append([final_list[i].dic,time_now])
        time_now  = time_now +1
    return res,hours
hours=0
#plan_my_day(four_square.get_topPicks("12.912248","77.642369"),12.912248,77.642369,hours)

def plan_multiple_days(places,lat,lng):
    days = raw_input("Enter days?\n")
    days = int(days)
    hours =0
    for i in range(1,days+1):
        print "Day: ",i
        res , hours = plan_my_day(places,lat,lng,hours)
        for place in res:
            print "|"
            print place[0]["name"]," : ",place[1],"Hrs"
            
        print "Day :",i," scheduled above","\n"
    print "trip planning concluded"

    
plan_multiple_days(four_square.get_topPicks("18.520262", "73.856035"),18.520262,73.856035)
