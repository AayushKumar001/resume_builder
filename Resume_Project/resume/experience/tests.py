from django.test import TestCase
from datetime import datetime


datetime_str = '09/19/18'
#date_object = datetime.strptime(datetime_str, '%d-%b-%Y').date()
date_object1 = datetime.strptime('10/01/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object2= datetime.strptime('10/02/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object3 = datetime.strptime('10/03/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object4 = datetime.strptime('10/04/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object5 = datetime.strptime('10/05/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object6 = datetime.strptime('10/06/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object7 = datetime.strptime('10/07/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object8 = datetime.strptime('10/08/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object9 = datetime.strptime('10/09/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object10 = datetime.strptime('10/10/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object11 = datetime.strptime('10/11/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
date_object12 = datetime.strptime('10/12/2012', '%d/%m/%Y').strftime('%d-%b-%Y')
#print(type(date_object))
print(date_object1)
print(date_object2)
print(date_object3)
print(date_object4)
print(date_object5)
print(date_object6)
print(date_object7)
print(date_object8)
print(date_object9)
print(date_object10)
print(date_object11)
print(date_object12)