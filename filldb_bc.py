import random
from django.db import connection
import time
import datetime
from foodsharing.models import UserPerson, Supply, UserSuggestion, FoodInstance, FoodType, Vote
from django.utils import timezone


def fillFoodType(nn, nnn, ftypes):    

    names=['potato', 'tomato', 'lamb', 'sushi', 'pizza', 'milk', 'bread']
    types=['VE','VG', 'NO']

    for j in range(nn):
        u=[]
        uu=[]
        for i in range(nnn):
            u.append(FoodType(
                name=names[random.randint(0,len(names)-1)]+str(j+nnn*10*i), 
                type=types[random.randint(0,len(types)-1)], 
                pretamanger=bool(random.randint(0,2))
            ))
	uu=FoodType.objects.bulk_create(u)
        ftypes += [x.id for x in uu]


def fillUserPerson(nn, nnn, users):    
    u=[]
    for j in range(nn):
        u=[]
        uu=[]
        for i in range(nnn):
            u.append(UserPerson(
                name='0000User'+str(i)+str(j), 
                email='emailaddr'+str(j)+str(i)+'@mail.ru',
                rating= 20*random.random(),
            ))
        uu=UserPerson.objects.bulk_create(u)
        users += [x.id for x in uu]

def fillSupply(nn, nnn, supplies, users):    
    for j in range(nn):
        u=[]
        uu=[]
        for i in range(nnn):
            u.append(Supply(
                source_id= users[random.randint(0,len(users)-1)],
                date=timezone.now(),
                longitude=37.618423+0.2*random.random()-0.1,#55.970211, 37.475328
                latitude=55.751244+0.2*random.random()-0.1#55.539769, 37.491808
            ))
        uu=Supply.objects.bulk_create(u)
        supplies += [x.id for x in uu]

def fillFoodInstance(nn, nnn, finsts, ftypes, supplies):    
    for j in range(nn):
        uu=[]
        u=[]
        for i in range(nnn):
            u.append(FoodInstance(
                ftype_id= ftypes[random.randint(0,len(ftypes)-1)],
                supply_id=supplies[random.randint(0,len(supplies)-1)],
                manufacturer="manufacturer"+str(random.randint(0,10)),
                expire_date=datetime.datetime(2017, random.randint(1,12),random.randint(1,28), 18),
            ))
        uu=FoodInstance.objects.bulk_create(u)
        finsts += [x.id for x in uu]

def fillUserSuggestion(nn, nnn, sugests, users, supplies):    
    for j in range(nn):
        uu=[]
        u=[]
        for i in range(nnn):
            u.append(UserSuggestion(
                user_id_id=users[random.randint(0,len(users)-1)],
                supply_id=supplies[random.randint(0,len(supplies)-1)],
                date=datetime.datetime(2017, random.randint(1,12),random.randint(1,28), 17),
                longitude=37.618423+0.2*random.random()-0.1,
                latitude=55.751244+0.2*random.random()-0.1
            ))
        uu = UserSuggestion.objects.bulk_create(u)
        sugests  += [x.id for x in uu]

def fillVote(nn, nnn, users, supplies, sugests):    
    content_t=ContentType.objects.get_for_models(Supply, UserSuggestions)
    arr=[supplies,sugests]
    for j in range(nn):
        u=[]
        for i in range(nnn):
            k=random.randint(0,1)
            u.append(Vote(
                user_id=users[random.randint(0,len(users)-1)],
                rating=10*random.random()-5,
                content_type=content_t[k],
                object_id=arr[random.randint(0,len(arr[k])-1)]
            ))
        Vote.objects.bulk_create(u)
        
total=start_time=time.time()

users=list(UserPerson.objects.only('id').values_list('id',flat= True))
print 'counting UserPerson objects', ' time = ', time.time()-start_time 
start_time=time.time()
nn=100
nnn=1000
fillUserPerson(nn,nnn, users)    
print 'filling model UserPerson (pieces =', nn, ')*(piece_size = ', nnn, ') time = ', time.time()-start_time 
start_time=time.time()

ftypes=list(FoodType.objects.only('id').values_list('id',flat= True))
print 'counting FoodType objects', ' time = ', time.time()-start_time 
start_time=time.time()
nn=50
nnn=2000
fillFoodType(nn,nnn, ftypes)    
print 'filling model FoodType (pieces =', nn, ')*(piece_size = ', nnn, ') time = ', time.time()-start_time 
start_time=time.time()

supplies=list(Supply.objects.only('id').values_list('id',flat= True))
print 'counting Supply objects', ' time = ', time.time()-start_time 
start_time=time.time()
nn=50
nnn=2000
fillSupply(nn,nnn, supplies, users)    
print 'filling model Supply (pieces =', nn, ')*(piece_size = ', nnn, ') time = ', time.time()-start_time 
start_time=time.time()

finsts=list(FoodInstance.objects.only('id').values_list('id',flat= True))
print 'counting FoodInstance objects', ' time = ', time.time()-start_time 
start_time=time.time()
nn=200
nnn=500
fillFoodInstance(nn,nnn, finsts, ftypes, supplies)    
print 'filling model FoodInstance (pieces =', nn, ')*(piece_size = ', nnn, ') time = ', time.time()-start_time 
start_time=time.time()

sugests=list(UserSuggestion.objects.only('id').values_list('id',flat= True))
print 'counting UserSuggestion objects', ' time = ', time.time()-start_time 
start_time=time.time()
nn=25
nnn=4000
fillUserSuggestion(nn, nnn, sugests, users, supplies)    
print 'filling model UserSuggestion (pieces =', nn, ')*(piece_size = ', nnn, ') time = ', time.time()-start_time 
start_time=time.time()

start_time=time.time()
nn=20
nnn=1000
fillVote(nn,nnn, users, supplies, sugests)    
print 'filling model Vote (pieces =', nn, ')*(piece_size = ', nnn, ') time = ', time.time()-start_time 

print 'total = ', time.time()-total
