import requests
import threading
import time

st = time.time()
browse = requests.get('https://steamunlocked.net/all-games-2/',timeout=None).text.split('<li>')
browse.remove(browse[0])
browse[-1] = browse[-1].split('</ul>')[0]

allLinks = []
badLinks = []
Wlinks = []
progress = 0

f = open('output.txt','w')
f.write('')
f.close()

for i in range(len(browse)):
    allLinks.append(browse[i].split('</a>')[0].split('href="')[1].split('"')[0])
print(len(allLinks))

def default(role,start,finish,fin2):
    print(f' {role} | {start} to {finish} | started') 
    for i in range(start,finish):
        global progress
        progress = progress + 1
        print(f'({progress}/{fin2})', end='\r')
        try:
            l = requests.get(allLinks[i],timeout=None).content.decode("utf-8")
            l = l.split('<img')[2]
            Z = l.upper().count('TORRENT')  
            if Z > 0:
                link = allLinks[i]
                dat = ''
                try :
                    dat = l.split('class="btn-download"')[1].split('</a>')[0].split('<br>')
                    name = dat[1]
                    size = dat[2].split('<em>Size:')[1].split('</em>')[0]
                    print(f'{link} | {name} | {size}')
                    Wlinks.append(f'{link} | {name} | {size}')
                except:
                    dat = l.split('class="btn-download"')[1].split('</a>')[0].split('<br />')
                    name = dat[1]
                    size = dat[2].split('<em>Size:')[1].split('</em>')[0]
                    print(f'{link} | {name} | {size}') 
                    Wlinks.append(f'{link} | {name} | {size}')
        except:
            print(badLinks.append(allLinks[i]))
    print(f'\n\n {role} over\n\n')

#Tnum = int(input('number of threads    ')) -1
Tnum = 10
portion = round(len(allLinks)/Tnum)

index = 0
threads = []
Tcount = 1
while True :
    time.sleep(0.1)
    if index+portion > len(allLinks):
        t = threading.Thread(target=default,args=(Tcount,index,len(allLinks),len(allLinks),))
        threads.append(t)
        break
    else:
        t = threading.Thread(target=default,args=(Tcount,index,index+portion,len(allLinks),))
        index = index + portion 
        threads.append(t)
    Tcount = Tcount+ 1

for i in range(len(threads)) :
    threads[i].start()
for i in range(len(threads)) :
    threads[i].join()

 

while True :
    print(f'{progress}/{len(allLinks)}',end='\r')
    if progress >= len(allLinks):
        break


progress = 0
default('retrying timeout links',0,len(badLinks),len(badLinks))
et = time.time()


elapsed_time = et - st
f = open('output.txt','w+')
for i in Wlinks:
    f.write(f'{i}\n')

f.write(f'Execution time:  {elapsed_time}s')
f.close()
