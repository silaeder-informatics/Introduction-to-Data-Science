import requests
import random

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
            