import json
import urllib.request
import datetime
from collections import Counter

#This is a method that will return the most frequent element of a list
def mostFrequent(list):
    occurence_count = Counter(list)
    return occurence_count.most_common(1)[0][0]

#This is a method that gets our data from OPAP KINO api
def getDayData(url):
    with urllib.request.urlopen(url) as r:
        temp = r.read()
        temp = temp.decode()
        data = json.loads(temp)
        return data

#At this point I declare some useful variables, start is my starting date (For February, if I want to change the month or the year, all I have to do is change the numbers inside the parentheses)
#end is my current date
#delta is used to shift between days
#day is used to parse the day number inside the url
#DailyWinningNumbers is a list where I store the winning numbers
start = datetime.datetime(2021, 2, 1)
end = datetime.datetime.now()
delta = datetime.timedelta(days=1)
DailyWinningNumbers = []
day=1

#At this while loop, the condition makes sure I don't surpass the current date
#I empty the list everytime the loop runs
while start<=end:
    DailyWinningNumbers.clear()
    #This condition makes sure I dont get a bad request from the HTTP server while parsing the day value inside the URL
    if day<10:
        url ='https://api.opap.gr/draws/v3.0/1100/draw-date/2021-02-0{}/2021-02-0{}'.format(day, day)
    else:
        url ='https://api.opap.gr/draws/v3.0/1100/draw-date/2021-02-{}/2021-02-{}'.format(day, day)
    data = getDayData(url)
    #I fill my DailyWinningNumbers list with the winning numbers from the JSON file
    try:
        for x in range(0, 10):
            for y in range(0, 10 ):
                DailyWinningNumbers.append(data["content"][x]["winningNumbers"]["list"][y])
                #I declare the message that the user will receive when running the script
        Message = 'The most frequent winning number of the {}th of February is: '.format(day)
        print(Message,mostFrequent(DailyWinningNumbers))
    except:
        print("There's not any draws right now, come back between 9:00 AM and 23:55 PM")    
    start+=delta
    day+=1
