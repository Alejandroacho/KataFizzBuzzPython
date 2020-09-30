import unittest
from FizzBuzz import FizzBuzz

class MyTestCase(unittest.TestCase):

    def test_fizz_letra(self):
        conversor = FizzBuzz()
        result = conversor.calculadora('a')
        self.assertEqual('Introduce sólo números!', result)

    def test_fizz_una_cifra(self):
        conversor = FizzBuzz()
        result = conversor.calculadora(3)
        self.assertEqual('Fizz', result)

    def test_fizz_dos_cifra(self):
        conversor = FizzBuzz()
        result = conversor.calculadora(12)
        self.assertEqual('Fizz', result)
    
    def test_buzz_una_cifra(self):
        conversor = FizzBuzz()
        result = conversor.calculadora(5)
        self.assertEqual('Buzz', result)

    def test_buzz_dos_cifra(self):
        conversor = FizzBuzz()
        result = conversor.calculadora(10)
        self.assertEqual('Buzz', result)
    
    def test_fizzbuz_dos_cifra(self):
        conversor = FizzBuzz()
        result = conversor.calculadora(15)
        self.assertEqual('FizzBuzz', result)

    def test_fizzbuz_tres_cifra(self):
        conversor = FizzBuzz()
        result = conversor.calculadora(150)
        self.assertEqual('FizzBuzz', result)