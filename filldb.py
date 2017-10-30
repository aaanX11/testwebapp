import random
from django.db import connection
import time
from foodsharing.models import UserPerson, Supply, UserSuggestion, FoodInstance, FoodType


def fillUserPerson(nn, nnn):    

    u=[]
    r=[int((nnn/10)*random.random()) for _ in xrange(int(nnn/3))]

    for j in range(nn):
        for i in range(nnn):
            u.append((
                'User'+str(i)+str(j), 'emailaddr'+str(j)+str(i)+'@mail.ru', r[i%int(nnn/3)]
            ))
#       print u
        cursor= connection.cursor()
        cursor.executemany("INSERT INTO foodsharing_UserPerson (name, email, rating) VALUES (%s, %s, %s )", u)

start_time=time.time()
nn=20
nnn=10000
fillUserPerson(nn,nnn)    
print 'UserPerson', nn, '*', nnn, ' time = ', time.time()-start_time



def FoodType(nn, nnn):    
    u=[]
    r=[int((nnn/10)*random.random()) for _ in xrange(int(nnn/3))]
    names=['potato', 'tomato', 'lamb', 'sushi']
    types==['Vegeterian','Vegan', 'Ordinary']

    for j in range(nn):
        for i in range(nnn):
            u.append((names[i%4]+str(j+nnn*10*i), types[i%3]))
#       print u
        cursor= connection.cursor()
        cursor.executemany("INSERT INTO foodsharing_FoodType (name, type) VALUES (%s, %s)", u)

start_time=time.time()
nn=30
nnn=8000
fillFoodType(nn,nnn)    
print 'FoodType', nn, '*', nnn, ' time = ', time.time()-start_time

