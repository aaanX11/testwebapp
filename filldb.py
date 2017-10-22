#import random
#from django.db import connection

#from foodsharing.models import UserPerson


def fillUserPerson():    
    rr=random.random()
    u=[]
    r=[1 for _ in range(1000)]

    for i in range(100):
        u.append(('User'+str(i), 'emailaddr'+str(i)+'@mail.ru', r[i%1000]))
    print u
    cursor= connection.cursor()
 #   cursor.executemany("INSERT INTO UserPerson (name, email, rating) VALUES (%s, %s, %s)",u)

fillUserPerson()    
