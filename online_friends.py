import datetime
import pandas as pd
import vk
from tqdm import tqdm
import time

session = vk.Session(access_token="38479e4a81d854219057927293934ed4d12b1c91afb966101385de82fc3d24310c0d5a039d4a907764504")
vk_session = vk.API(session)
filename = 'online_friends.csv' 
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
time_array = []
ind = 0

data = pd.DataFrame(columns=['Date', 'Hour', 'Minute', 'Second', 'Weekday', 'Weekday_number' ,'Online_friends'])
while (True):
    arr = vk_session.friends.getOnline(v=5.103)
    print(len(arr))

    now = datetime.datetime.now()
    data.loc[ind] = {'Date':now.day, 'Hour':now.hour, 'Minute':now.minute, 'Second':now.second, 'Weekday':week[now.weekday()], 'Weekday_number':now.weekday(), 'Online_friends':len(arr)}
    data.to_csv(filename, index=False)
    ind += 1

    time.sleep(30)
