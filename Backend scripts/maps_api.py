import requests

#########GOOOGLE##########
def search_by_address(address):
    base_url="https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=AIzaSyCfTGctBT1nsQjoVJ0tELQi00cGzujscg8"
    req = requests.get(base_url.format(address=address))
    result = req.json()
    print result
    lat , langi = result["results"][0]["geometry"]["location"]["lat"],result["results"][0]["geometry"]["location"]["lng"]
    place_id = result["results"][0]["place_id"]
    l =[]
    l = [lat,langi,place_id]
    return l

########GOOGLE############
def get_point_of_interests(place_id):
    base_url = "https://maps.googleapis.com/maps/api/place/details/json?placeid={place}&key=AIzaSyCfTGctBT1nsQjoVJ0tELQi00cGzujscg8"
    req = requests.get(base_url.format(place=place_id))
    print req.text

#get_point_of_interests(search_by_address("Kfc Pimple Saudagar Pune")[2])
