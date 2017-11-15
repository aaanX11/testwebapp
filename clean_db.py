import random
from django.db import connection
import time
from foodsharing.models import UserPerson, Supply, UserSuggestion, FoodInstance, FoodType

print 'print u r going to TRUNCATE tables'
print ' (1 to continue)'
s= int(raw_input())
if s==1:
    cursor=connection.cursor()
    cursor.execute("TRUNCATE TABLE foodsharing_UserPerson CASCADE")
    cursor.execute("TRUNCATE TABLE foodsharing_FoodType CASCADE") 
    cursor.execute("TRUNCATE TABLE foodsharing_Supply CASCADE")
    cursor.execute("TRUNCATE TABLE foodsharing_FoodInstance CASCADE") 
    cursor.execute("TRUNCATE TABLE foodsharing_Vote CASCADE")
    cursor.execute("TRUNCATE TABLE foodsharing_UserSuggestion CASCADE") 

#python manage.py flush
