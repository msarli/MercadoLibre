from django.test import TestCase
from .classes import Person

class PersonTestCase(TestCase):
    def setUp(self):
        pass
        #Person.objects.create()

    def test_isMutant(self):
        personTest = Person()
        #Failed test 1
        data=["AAAA","AAAA"]
        self.assertEqual(personTest.isMutant(data), False)
        #Failed test 2
        data2=["AAAA","AAAA"]
        self.assertEqual(personTest.isMutant(data2), False)
        #Correct test 1
        data3=["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
        self.assertEqual(personTest.isMutant(data3), True)
        #Failed test 3
        data4=['ATGCGA','CAGTGC','TTATTT','AGACGG','GCGTCA','TCACTG']
        self.assertEqual(personTest.isMutant(data4), False)
        #Correct test 2
        data5=['AACC','CACC','CCAC','CAAA']
        self.assertEqual(personTest.isMutant(data5), True)
        #Failed test 4
        data6=[]
        self.assertEqual(personTest.isMutant(data6), False)

        