import datetime
import pandas as pd
import vk
import time
import os

from token import token

session = vk.Session(access_token=token)
vk_session = vk.API(session)

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
subjects = [['9:00', '9:40'], ['9:45', '10:25'], ['10:35', '11:15'], ['11:20', '12:00'], ['12:20', '13:00'], ['13:05', '13:45'], ['14:35', '15:15'], ['15:20', '16:00'], ['16:10', '16:50'], ['16:55', '17:35']]
filename = 'data.csv' 

time_array = []
ind = 0

nikita_id = 429454563
friends = []

def test(subjects, now):
    for elem in subjects:
        t = elem[0].split(':')
        t2 = elem[1].split(':')
        if (int(t[0]) * 60 + int(t[1])) < now.hour * 60 + now.minute and (int(t2[0]) * 60 + int(t2[1])) > now.hour * 60 + now.minute:
            return True
    return False 


data = pd.DataFrame(columns=['Date', 'Hour', 'Minute', 'Second', 'Weekday', 'Weekday_number', 'Is_lesson' ,'Online_friends', 'Nikita_online'])
while (True):
    arr = vk_session.friends.getOnline(v=5.103)

    now = datetime.datetime.now()
    print(test(subjects, now))
    data.loc[ind] = {'Date':now.day, 'Hour':now.hour, 'Minute':now.minute, 'Second':now.second, 'Weekday':week[now.weekday()], 'Weekday_number':now.weekday(), 'Is_lesson':[0, 1][test(subjects, now)], 'Online_friends':len(arr), 'Nikita_online':nikita_id in arr}
    data.to_csv(filename, index=False)
    ind += 1

    time.sleep(10)
