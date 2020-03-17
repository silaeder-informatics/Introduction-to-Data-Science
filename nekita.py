import datetime
import pandas as pd
import vk
import time
import os

from my_token import token

session = vk.Session(access_token=token)
vk_session = vk.API(session)

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
subjects = [['9:00', '9:40'], ['9:45', '10:25'], ['10:35', '11:15'], ['11:20', '12:00'], ['12:20', '13:00'], ['13:05', '13:45'], ['14:35', '15:15'], ['15:20', '16:00'], ['16:10', '16:50'], ['16:55', '17:35']]
filename = 'friends_data.csv' 
ind = 0


try:
    data = pd.read_csv(filename)
    print(len(data['Date']))
    ind = len(data['Date'])
except:
    ind = 0
    print('remade')
    data = pd.DataFrame(columns=['Date', 'User_first_name', 'User_last_name', 'User_id', 'Is_closed', 'User_sex', 'User_age', 'User_status'])

while (True):
    online_friends = vk_session.friends.getOnline(v=5.103)

    for user_id in online_friends:
        status = vk_session.status.get(v=5.103, user_id=user_id)
        time.sleep(0.6)
        user = vk_session.users.get(v=5.103, user_id=user_id)[0]
        time.sleep(0.6)
        
        now = datetime.datetime.now()
        data.loc[ind] = {'Date':now, 'User_first_name':user['first_name'], 'User_last_name':user['last_name'], 'User_id':user_id, 'Is_closed':user['is_closed'], 'User_sex':'Nan', 'User_age':'Nan', 'User_status':status['text']}

        ind += 1
    
    data.to_csv(filename, index=False)
    time.sleep(30)
