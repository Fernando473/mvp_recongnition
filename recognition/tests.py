from django.test import TestCase

from recognition.convert_to_number import to_number

# Create your tests here.
arr = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'siete']

numb = to_number(arr)

print(numb)
