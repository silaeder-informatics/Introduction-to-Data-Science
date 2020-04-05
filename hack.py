import requests
import random
import pandas
import datetime

filename = 'tested.csv'
try:
    data = pd.read_csv(filename)
    print(len(data['Raw_date']))
    ind = len(data['Raw_date'])
except:
    ind = 0
    print('remade')
    data = pd.DataFrame(columns=['Raw_date', 'Link'])

ind = -1
while (True):
    ind += 1
    gener = ''
    m_ind = [8, 13, 18, 23]
    arr = '0123456789abcdefghijklmnopqrstuvwxyz'

    for i in range(36):
        if i in m_ind:
            gener += '-'
        else:
            gener += arr[random.randint(0, 35)]


    path = f'https://storage.geekclass.ru/images/{gener}.ipynb'
    print(ind, path)
    answer = requests.get(path)

    if answer.status_code == 200:
        print(path)
        with open('file/' + path.lstrip('https://storage.geekclass.ru/images/'), 'wb') as file:
            file.write(answer.content)
    else:
	data.loc[ind] = {'Raw_time': datetime.datetime.now(), 'Link': path}
	ind += 1
