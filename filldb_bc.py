import random
from django.db import connection
import time
from foodsharing.models import UserPerson, Supply, UserSuggestion, FoodInstance, FoodType
from django.utils import timezone


def fillUserPerson(nn, nnn):    

    u=[]
    r=[int((nnn/10)*random.random()) for _ in xrange(int(nnn/3))]

    for j in range(nn):
        for i in range(nnn):
            u.append(UserPerson(
                name='0000User'+str(i)+str(j), 
                email='emailaddr'+str(j)+str(i)+'@mail.ru',
                rating= r[i%int(nnn/3)]
            ))
#       print u
        UserPerson.objects.bulk_create(u)

start_time=time.time()
nn=20
nnn=1000
fillUserPerson(nn,nnn)    
print 'UserPerson', nn, '*', nnn, ' time = ', time.time()-start_time



def fillFoodType(nn, nnn):    
    u=[]
    r=[int((nnn/10)*random.random()) for _ in xrange(int(nnn/3))]
    names=['potato', 'tomato', 'lamb', 'sushi']
    types=['VE','VG', 'NO']

    for j in range(nn):
        for i in range(nnn):
            u.append(FoodType(name=names[i%4]+str(j+nnn*10*i), type=types[i%3], pretamanger=True))
#       print u
    FoodType.objects.bulk_create(u)

start_time=time.time()
nn=300
nnn=1000
fillFoodType(nn,nnn)    
print 'FoodType', nn, '*', nnn, ' time = ', time.time()-start_time


def fillSupply(nn, nnn):    
    u=[]
    r=[int((nnn/10)*random.random()) for _ in xrange(int(nnn/3))]

    for j in range(nn):
        for i in range(nnn):
            u.append(Supply(
                items=r[i%int(nnn/3-5):i%int(nnn/3)],
                source= r[i%int(nnn/3)],
                date=timezone.now(),
                longitude=random.random(),
                latitude=random.random()
            ))
#       print u
        Supply.objects.bulk_create(u)

start_time=time.time()
nn=20
nnn=1000
fillSupply(nn,nnn)    
print 'Supply', nn, '*', nnn, ' time = ', time.time()-start_time

def fillFoodInstance(nn, nnn):    
    u=[]
    r=[int((nnn/10)*random.random()) for _ in xrange(int(nnn/3))]

    for j in range(nn):
        for i in range(nnn):
            u.append(Supply(
                type= r[i%int(nnn/3)],
                manufacturer="manufacturer"+str(type+10),
                expire_date=timezone.now()
            ))
#       print u
        FoodInstance.objects.bulk_create(u)

start_time=time.time()
nn=20
nnn=1000
fillFoodInstance(nn,nnn)    
print 'FoodInstance', nn, '*', nnn, ' time = ', time.time()-start_time


