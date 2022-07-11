import unittest

from testlang import frenchToEnglish, englishToFrench

class TestSquare(unittest.TestCase): 
    def test1(self): 
   
        self.assertEqual(add('Hello'), 'Bonjour') 
        self.assertNotEqual(add('Hello'), 'Namaste') 
        self.assertEqual(add(None), "")   

class TestSquare(unittest.TestCase): 
    def test1(self): 
        
        self.assertEqual(add('Bonjour'), 'Hello') 
        self.assertNotEqual(add('Bonjour'), 'Namaste')  
        self.assertEqual(add(None), "")          

unittest.main()
