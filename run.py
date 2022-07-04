#SEQUELS
import requests
import threading
import time


#ACT 1 
r = requests.get('https://steamunlocked.net/all-games-2/').content.decode("utf-8")
r = r.split('<li>')
r.remove(r[0])


c = []

paste = open('pas.txt','w')
paste.write('')
paste.close()

for i in range(len(r)):
    r[i] = r[i].split('</li>')
    r[i].remove(r[i][1])
    r[i] = r[i][0]

    r[i] = r[i].split('<a href="')
    r[i].remove(r[i][0])
    r[i] = r[i][0]

    r[i] = r[i].split('">')
    r[i].remove(r[i][1])
    r[i] = r[i][0]

    c.append(r[i] + '\n')



#ACT 2 
full = len(c)
v = []
ind = 0

def conn1():
    global ind
    for i in range(0,1000): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2] 
        fd = R.count('Torrent') + R.count('torrent')  
        if fd >= 1:
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1   



def conn2():
    global ind
    for i in range(1000,2000): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2]
        fd = R.count('Torrent') + R.count('torrent')  

        if fd >= 1:
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1  

def conn3():
    global ind
    for i in range(2000,3000): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2]
        fd = R.count('Torrent') + R.count('torrent')  

        if fd >= 1:
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1  


def conn4():
    global ind
    for i in range(3000,4000): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2]
        fd = R.count('Torrent') + R.count('torrent')  

        if fd >= 1:
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1  


def conn5():
    global ind
    for i in range(4000,5000): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2]
        fd = R.count('Torrent') + R.count('torrent')  

        if fd >= 1:
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1  


def conn6():
    global ind
    for i in range(5000,6000): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2]
        fd = R.count('Torrent') + R.count('torrent')  

        if fd >= 1:
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1  


def conn7():
    global ind
    for i in range(6000,7000): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2]
        fd = R.count('Torrent') + R.count('torrent')  

        if fd >= 1:
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1  


def conn8():
    global ind
    for i in range(7000,8000): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2]
        fd = R.count('Torrent') + R.count('torrent')  

        if fd >= 1:
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1  


def conn9():
    global ind
    for i in range(8000,9000): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2]
        fd = R.count('Torrent') + R.count('torrent')  

        if fd >= 1:
            c[i] =c[i] + '\n'
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1  


def conn10():
    global ind
    for i in range(9000,len(c)): 
        c[i] = c[i].split('\n')[0]
        R = requests.get(c[i]).content.decode("utf-8").split('<img')[2]
        fd = R.count('Torrent') + R.count('torrent')  

        if fd >= 1:
            c[i] =c[i] + '\n'
            print(c[i])
            v.append(str(c[i]))
        ind = ind + 1  




#ACT 3


t1 = threading.Thread(target=conn1)
t2 = threading.Thread(target=conn2)
t3 = threading.Thread(target=conn3)
t4 = threading.Thread(target=conn4)
t5 = threading.Thread(target=conn5)
t6 = threading.Thread(target=conn6)
t7 = threading.Thread(target=conn7)
t8 = threading.Thread(target=conn8)
t9 = threading.Thread(target=conn9)
t10 = threading.Thread(target=conn10)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start() 
t8.start()
t9.start()
t10.start()




while True:
    paste = open('pas.txt','w')
    for i in range(len(v)):
        a = v[i] + '\n'
        paste.write(a)
    paste.close()
    p = round((ind*100)/full,1)
    o = round(p / 10)
    f = '*' * o * 2
    e = '-' * (10 - o) *2
    b = '[' + f + e + ']'
    k = '(' + str(ind) + '/' + str(full) +')'

    print(p,'%',b.center(40), k.center(10),end='\r' )
    time.sleep(2)

    if ind == full:
        break

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

f.close()

#Sorry i could not find how to multithread while loops xd
