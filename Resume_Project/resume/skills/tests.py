from django.test import TestCase

# Create your tests here.

y = [ i for i in range(2019,0,-1) if i >= 1980 ]
years = [(val,str(val)) for val in y ]
print(years)
