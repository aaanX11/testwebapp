from django.db import connection
from foodsharing.models import FoodType

#cur=connection.cursor()
#cur.execute("SELECT ALL FROM "

names=['lamb', 'sushi', 'potato', 'tomato']
types=['VE', 'VG','NO']
for i in range(10):
    
    u=FoodType(name=names[i%4]+str(i),type=types[i%3], pretamanger=(i%2==0))
    u.save()
