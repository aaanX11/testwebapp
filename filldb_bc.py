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
                rating= r[i%int(nnn/3)],
            ))
        UserPerson.objects.bulk_create(u)

def fillFoodType(nn, nnn):    
    r=[int((nnn/10)*random.random()) for _ in xrange(int(nnn/3))]
    names=['potato', 'tomato', 'lamb', 'sushi']
    types=['VE','VG', 'NO']

    for j in range(nn):
        u=[]
        for i in range(nnn):
            u.append(FoodType(name=names[i%4]+str(j+nnn*10*i), type=types[i%3], pretamanger=(i%2==0)))
    FoodType.objects.bulk_create(u)

def fillSupply(nn, nnn):    
    users=list(UserPerson.objects.all().values_list('id', flat =True))
    r=[int((len(users))*random.random()) for _ in xrange(len(users))]

    for j in range(nn):
        u=[]
        for i in range(nnn):
            u.append(Supply(
                source= r[i%len(users)],
                date=timezone.now(),
                longitude=random.random(),
                latitude=random.random()
            ))
        Supply.objects.bulk_create(u)

def fillFoodInstance(nn, nnn):    

    ftypes=list(FoodType.objects.all().values_list('id', flat =True))
    r1=[int((len(ftypes))*random.random()) for _ in xrange(len(ftypes))]
    supplies=list(Supply.objects.all().values_list('id', flat =True))
    r2=[int((len(supplies))*random.random()) for _ in xrange(len(supplies))]
    for j in range(nn):
        u=[]
        for i in range(nnn):
            u.append(Supply(
                type= ftypes[r1[i%len(ftypes)]],
                supply=supplies[r2[i%len(supplies)]]
                manufacturer="manufacturer"+str(type+10),
                expire_date=timezone.now()
            ))
        FoodInstance.objects.bulk_create(u)
def fillUserSuggestion(nn, nnn):    
    users=list(UserPerson.objects.all().values_list('id', flat =True))
    r1=[int((len(users))*random.random()) for _ in xrange(len(users))]

    supplies=list(Supply.objects.all().values_list('id', flat =True))
    r2=[int((len(supplies))*random.random()) for _ in xrange(len(supplies))]
    for j in range(nn):
        u=[]
        for i in range(nnn):
            u.append(Supply(
                user=r1[i%len(users)],
                supply=supplies[r2[i%len(supplies)]],
                manufacturer="manufacturer"+str(type+10),
                expire_date=timezone.now()
            ))
        FoodInstance.objects.bulk_create(u)



total=start_time=time.time()
nn=20
nnn=1000
fillUserPerson(nn,nnn)    
print 'UserPerson', nn, '*', nnn, ' time = ', time.time()-start_time

start_time=time.time()
nn=30
nnn=1000
fillFoodType(nn,nnn)    
print 'FoodType', nn, '*', nnn, ' time = ', time.time()-start_time


start_time=time.time()
nn=20
nnn=1000
fillSupply(nn,nnn)    
print 'Supply', nn, '*', nnn, ' time = ', time.time()-start_time

start_time=time.time()
nn=20
nnn=1000
fillFoodInstance(nn,nnn)    
print 'FoodInstance', nn, '*', nnn, ' time = ', time.time()-start_time

start_time=time.time()
nn=20
nnn=1000
fillUserSuggestion(nn,nnn)    
print 'UserSuggestion', nn, '*', nnn, ' time = ', time.time()-start_time

start_time=time.time()
nn=20
nnn=1000
#fillVote(nn,nnn)    
#print 'Vote', nn, '*', nnn, ' time = ', time.time()-start_time

print 'total = ', time.time()-total
