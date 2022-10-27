import requests



def getHotelsBy(name):

    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    querystring = {"q":name,"locale":"en_US","langid":"1033","siteid":"300000001"}

    headers = {
        "X-RapidAPI-Key": "807febe8a3mshb19f3d0ca58469ap1226bfjsnfdfb91199e22",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonResp =response.json()
    hotels ={}
    for i in jsonResp["sr"]:
        hotels[i["hotelId"]]={"name":i["regionNames"]["shortName"],"address":i["hotelAddress"]["street"], "city":i["hotelAddress"]["city"], "province":i["hotelAddress"]["province"]}
    return hotels
    
def getReviewsByid(hotelId):
    url = "https://hotels4.p.rapidapi.com/reviews/v3/list"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": str(hotelId),
        "size": 10,
        "startingIndex": 0
        }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "807febe8a3mshb19f3d0ca58469ap1226bfjsnfdfb91199e22",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    jsonResp =response.json()
    reviews=[]
    for i in jsonResp["data"]["propertyInfo"]["reviewInfo"]["reviews"]:
        if(len(i)>0):
            reviews.append(i["text"])
    return reviews

def getHotelDetailById(hotelId):
    url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": str(hotelId)
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "807febe8a3mshb19f3d0ca58469ap1226bfjsnfdfb91199e22",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if response.status_code==200:
        jsonResp =response.json()
        
        hotel = {"name":jsonResp["data"]["propertyInfo"]["summary"]["name"],"address":jsonResp["data"]["propertyInfo"]["summary"]["location"]["address"]["addressLine"],"city":jsonResp["data"]["propertyInfo"]["summary"]["location"]["address"]["city"],"province":jsonResp["data"]["propertyInfo"]["summary"]["location"]["address"]["province"],"value":getValue(hotelId),"reviews":getReviewsByid(hotelId)}
        return hotel
    return None
def getValue(hotelId):
    url = "https://hotels4.p.rapidapi.com/reviews/v3/get-summary"

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": str(hotelId)
        }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "807febe8a3mshb19f3d0ca58469ap1226bfjsnfdfb91199e22",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    jsonResp =response.json()
    value = jsonResp["data"]["propertyReviewSummaries"][0]["overallScoreWithDescriptionA11y"]["value"]
    return value