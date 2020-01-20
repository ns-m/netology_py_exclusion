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
        if self.operand1 == '0' or self.operand2 == '0':
            self.operand1, self.operand2 = int(0), int(0)
        if self.operand1 == '' or self.operand2 == '':
            try:
                self.operand1, self.operand2 = int(self.operand1), int(self.operand2)
            except ValueError:
                print('введены не все операнды')
        try:
            self.operand1 / self.operand2
        except ArithmeticError:
            print('арифметическая ошибка')
        except TypeError:
            print('вводить только числа')

    def operation(self):
        result = 0
        try:
            if self.operators == '/':
                result = int(self.operand1) / int(self.operand2)
            elif self.operators == '+':
                result = int(self.operand1) + int(self.operand2)
            elif self.operators == '*':
                result = int(self.operand1) * int(self.operand2)
            elif self.operators == '-':
                result = int(self.operand1) - int(self.operand2)
        except:
            result = ''
        return result