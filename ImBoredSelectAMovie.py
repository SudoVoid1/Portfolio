import urllib3
from bs4 import BeautifulSoup
import random

#gets website data
url = "http://www.imdb.com/search/title?release_date=2020,2020&title_type=feature"
getUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(getUrl, "html.parser")
rnum = random.randint(0,50)
#print(rnum) test
#rnum=1 #just to test 
i = 0
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
for div_item in movieList:
    div = div_item.find('div',attrs={'class':'lister-item-content'})
    header = div.findChildren('h3',attrs={'class':'lister-item-header'})
    if i == rnum:
        print("Picking a movie from the Top 100")
        print ("I found number: " + str(i))
        print ('The Movie Is: ' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
        flink = str(header[0].findChildren('a'))
        s = list(flink)
        s.remove("/") #by doing this it allows for the for loop to find the end of the link
        s.remove("/") # ^^
        for j in s:
            if j == "/":
                #print(s.index(j))
                g = s.index(j)
                lk = []
                for x in range(10,g+1): #finds end of link
                    lk.append(s[x]) 
                
                lk.insert(5,"/") #inserts / back into link
                lk.insert(0,"/")
                print("\nClick this link to find where to watch")
                print("https://www.imdb.com", end ='') 
                print(*lk, sep='')
                break
        break
    i += 1
    
