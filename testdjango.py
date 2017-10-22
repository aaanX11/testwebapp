from django.db import connection
from foodsharing.models import UserPerson

#cur=connection.cursor()
#cur.execute("SELECT ALL FROM "

for i in range(10):
    print 'user'+str(i), 'usermail'+str(i)+'@mail.ru', i
    u=UserPerson(name='user'+str(i),email= 'usermail'+str(i)+'@mail.ru', rating=i)
    u.save()
