from bs4 import BeautifulSoup
import requests
import time
from csv import writer


def find_car():
 url ='https://www.olx.pl/d/motoryzacja/samochody/' 
 page = requests.get(url)
 soup = BeautifulSoup(page.content, 'html.parser')
 lists = soup.find_all('a',class_='css-rc5s2u')
 

 with open('Carreport.csv','w', encoding='utf-8') as f:
  thewriter = writer(f)
  header = ['title', 'car']
  thewriter.writerow(header)

  for list in  lists:
    title = list.find('div', class_='css-1venxj6').text.replace('\n', '')
    car = list.find('div', class_='css-1ut25fa').text.replace('\n', '')
    info = [title,car]
    

     
    base_url = 'https://api.telegram.org/bot5381340367:AAFRaalGsLUVyCYTVKE3yYdLw12kE9p6Ow8/sendMessage?chat_id=-877307780&text="{}"'.format(list)
    requests.get(base_url)
    time.sleep(1)

    thewriter.writerow(info)

   
   

if __name__ == '__main__':
    while True:
        find_car()
        time_wait = 10
        print(f'Waiting for{time_wait} seconds to complete.')
       