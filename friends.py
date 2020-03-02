import datetime
import pandas as pd
import vk
import time
import os


session = vk.Session(access_token="38479e4a81d854219057927293934ed4d12b1c91afb966101385de82fc3d24310c0d5a039d4a907764504")
vk_session = vk.API(session)
filename = 'online_friends.csv' 
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
time_array = []
subjects = [['9:00', '9:40'], ['9:45', '10:25'], ['10:35', '11:15'], ['11:20', '12:00'], ['12:20', '13:00'], ['13:05', '13:45'], ['14:35', '15:15'], ['15:20', '16:00'], ['16:10', '16:50'], ['16:55', '17:35']]
ind = 0

def test(subjects, now):
    for elem in subjects:
        t = elem[0].split(':')
        t2 = elem[1].split(':')
        if (int(t[0]) * 60 + int(t[1])) < now.hour * 60 + now.minute and (int(t2[0]) * 60 + int(t2[1])) > now.hour * 60 + now.minute:
            return True
    return False



try:
    data = pd.read_csv("online_friends.csv")
    print(len(data['Date']))
    ind = len(data['Date'])
except:
    ind = 0
    print('remade')
    data = pd.DataFrame(columns=['Date', 'Hour', 'Minute', 'Weekday', 'Weekday_number', 'Is_lesson' ,'Online_friends'])



while (True):
    arr = vk_session.friends.getOnline(v=5.103)

    now = datetime.datetime.now()
    data.loc[ind] = {'Date':now.day, 'Hour':now.hour, 'Minute':now.minute, 'Weekday':week[now.weekday()], 'Weekday_number':now.weekday(), 'Is_lesson':[0, 1][test(subjects, now)], 'Online_friends':len(arr)}

    data.to_csv(filename, index=False)
    ind += 1

    time.sleep(60)
