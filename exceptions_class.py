class Exceptions:

    def __init__(self, operators=input("Введите оператор : "), operand1=input("Введите операнд №1 : "),
                 operand2=input("Введите операнд №2 : ")):
        self.operators = operators
        self.operand1 = operand1
        self.operand2 = operand2

    def exceptions_operators(self):
        operators_list = ['+', '-', '*', '/']
        assert (self.operators in operators_list), 'Введите один из данных операторов: +, -, *, /'

    def exceptions_operands(self):
        try:
            int(self.operand1) / int(self.operand2)
        except ArithmeticError:
            print('арифметическая ошибка')
        except TypeError:
            print('вводить только числа')
        except ValueError:
            print('введены не все операнды')

    def operation(self):
        result = 0
        operand1, operand2 = int(self.operand1), int(self.operand2)
        try:
            if self.operators == '/':
                result = operand1 / operand2
            elif self.operators == '+':
                result = operand1 + operand2
            elif self.operators == '*':
                result = operand1 * operand2
            elif self.operators == '-':
                result = operand1 - operand2
        except:
            result = ''
        return result