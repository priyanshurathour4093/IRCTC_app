import requests
class IRCTC:

    def __init__(self):
        user_input = input("""How would you like to proceed?
              1. Enter 1 to check live train status
              2. Enter 2 to check PNR
              3. Enter 3 to check train schedule""")
        
        if user_input == "1":
            print("live tarin status")
        elif user_input == "2":
            print("PNR")
        else: 
            self.train_schedule()

    def train_schedule(self):
        train_no =input("Enter the Train no")
        self.fetch_data(train_no)

    def fetch_data(self,train_no):
        data = requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/<key>/TrainNumber/{}".format(train_no))
        #<key> paste your indianrailapi key
        #for different APIs go to Indian Rail Api website (https://indianrailapi.com/) and simply sign in and paste it over in get request

        data = data.json()

        #print(data)  #for whole data fetch like station code,station name, Arr_time, Depart_time, Dis etc.
        print(data['Route'])

        for i in data['Route']:
            print(i['StationName'])   # add more things as per our need like i["ArrivalTime"] and much more

obj = IRCTC()
