class FizzBuzz:
    def calculadora (self, input):

        if isinstance(input, str) == True:
            message='Introduce sólo números!'
            return message

        if input % 3 == 0 and input % 5 != 0:
            message='Fizz'
            return message

        if input % 5 == 0 and input % 3 != 0:
            message='Buzz'
            return message

        if input % 3 == 0 and input % 5 == 0:
            message= 'FizzBuzz'
            return message