
from hotelapi import *
hotels={}
while True:
    print("I have",len(hotels),"favourite Hotels :)")
    print("1.- Search hotel by Name")
    print("2.- Quality by Id")
    print("3.- Import hotel by Id")
    print("4.- List hotels")
    print("5.- List hotels by Id")
    print("6.- List hotels by value")
    print("7.- Exit")
    option = int(input("Select option: "))
    if option ==7:
        print("Good bye!")
        break
    elif option ==1:
        name = input("Enter name hotel: ")
        dictHotel = getHotelsBy(name)
        for key, value in dictHotel.items():
            print(key)
            for key2, value2 in value.items():
                print("\t"+key2.capitalize()+" :",value2)
    elif option ==2:
        hotelId = int(input("Enter hotel Id: "))
        value =getValue(hotelId)
        print ("Quality:",value,"\n")
    elif option ==3:
        hotelId = int(input("Enter hotel Id: "))
        hotels[hotelId]=getHotelDetailById(hotelId)
        print("Importing...")
        if hotelId not in hotels.keys():
            print("Imported fail!")
        else:
            print("Imported successfully!")
    elif option ==4:
        print("Listing Hotels")
        for key, value in hotels.items():
            print(key)
            for key2, value2 in value.items():

                if key2 != "reviews":
                    print("\t"+key2.capitalize()+" :",value2)
                    
                else:
                    print("\t"+key2.capitalize()+" :(",str(len(value2))+")")
    elif option ==5:
        hotelId = int(input("Enter hotel Id: "))
        reviews = getReviewsByid(hotelId)
        hotel =getHotelDetailById(hotelId)
        print("Review for",hotel["name"])
        for i in reviews:
            print(i)
    elif option ==6:
        quality = float(input("Enter min quality [0-10]: "))
        for i in hotels:
            print(str(i["value"]))
            value =i["value"]

            if value.find(str(quality))>0:
                for key, value in i.items():
                    if key != "reviews":
                        print("\t"+key.capitalize()+" :",value)

    else:
        print("The option seleted it's not exist!")