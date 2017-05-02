from bs4 import BeautifulSoup
from urllib import request
from time import sleep

# Phone Numbers go into this dictionary
phoneNumberList = {}

while True:
    for key, value in phoneNumberList.items():
        pNumber = str(value)
        pNumberName = str(key)
        url = "https://order.dominos.com/orderstorage/GetTrackerData?Phone=" + pNumber
        thepage = request.urlopen(url)
        soup = BeautifulSoup(thepage, "xml")
        print("Checking " + pNumberName + "...")

        # Gatekeeper XML tag stored in a variable
        orderStatuses = str(soup.find('OrderStatuses').text)

        # Gatekeeper
        if orderStatuses != "":

            # Pertinent XML tags stored in variables
            startTime = str(soup.find('StartTime').text)
            orderDescription = str(soup.find('OrderDescription').text)
            print(orderDescription)
            # vvv Put additional XML tags code in between these comments vvv

            # ^^^ Put additional XML tags code in between these comments ^^^


        else:
            pass
            print("No order for " + pNumberName)

        # Be cautious if you edit this sleep statement.
        # Do not reduce the wait time too much.
        # We don't want to accidentally DDoS Dominos :)
        sleep(60)
