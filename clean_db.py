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

#python manage.py flush
