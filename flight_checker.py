import time
from sms import send
from urllib import response
import os
from h11 import Data
import requests
import emoji


def main(origin_code, destination_code, date_from, date_to, return_from, return_to, adults):
    TEQUILA_API_KEY = "YOURAPIKEY"
    headers = {"apikey": TEQUILA_API_KEY}

    date_from_day = date_from.split("/")[0]
    date_from_month = date_from.split("/")[1]
    date_from_year = date_from.split("/")[2]
    date_to_day = date_to.split("/")[0]
    date_to_month = date_to.split("/")[1]
    date_to_year = date_to.split("/")[2]
    return_from_day = return_from.split("/")[0]
    return_from_month = return_from.split("/")[1]
    return_from_year = return_from.split("/")[2]
    return_to_day = return_to.split("/")[0]
    return_to_month = return_to.split("/")[1]
    return_to_year = return_to.split("/")[2]

    # string_asd = "date_from=31%2F08%2F2022&date_to=31%2F08%2F2022&return_from=13%2F09%2F2022&return_to=13%2F09%2F202"
    url = f"https://tequila-api.kiwi.com/v2/search?fly_from={origin_code}&fly_to={destination_code}&date_from={date_from_day}%2F{date_from_month}%2F{date_from_year}&date_to={date_to_day}%2F{date_to_month}%2F{date_to_year}&return_from={return_from_day}%2F{return_from_month}%2F{return_from_year}&return_to={return_to_day}%2F{return_to_month}%2F{return_to_year}&flight_type=round&one_for_city=0&one_per_date=0&adults={adults}&selected_cabins=M&only_working_days=false&only_weekends=false&partner_market=us&curr=USD&max_stopovers=2&max_sector_stopovers=2&vehicle_type=aircraft&limit=500"

    data = requests.get(url, headers=headers)

    data = data.json()

    # if seats is None look for next flight
    # if seats are less than adults, look for next flight

    total_num_flights = len(data["data"])
    for i in range(total_num_flights):
        # check if there are seats available
        seats = data["data"][i]["availability"]["seats"]
        if seats is None:
            continue
        elif seats < adults:
            continue
        else:
            price = data["data"][i]["price"]
            print(f"Flight costs: ${price}")
            # print(f"Flight has {seats} seats available")
            # print(f"Flight index of {i}")
            send(f"Flight costs: ${price}")
            break


main(origin_code="LAX", destination_code="HND", date_from="19/04/2022",
     date_to="19/04/2022", return_from="05/05/2022", return_to="05/05/2022", adults=2)
