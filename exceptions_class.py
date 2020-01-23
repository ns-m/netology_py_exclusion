class PolishCalculator:

    def __init__(self, operators, operand1, operand2):
        self.operators = operators
        self.operand1 = operand1
        self.operand2 = operand2

    def validate_operators(self):
        operators_list = ['+', '-', '*', '/']
        assert (self.operators in operators_list), 'Введите один из данных операторов: +, -, *, /'

    def validate_operands(self):
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
        self.result = result
        try:
            if self.operators == '/':
                self.result = int(self.operand1) / int(self.operand2)
            elif self.operators == '+':
                self.result = int(self.operand1) + int(self.operand2)
            elif self.operators == '*':
                self.result = int(self.operand1) * int(self.operand2)
            elif self.operators == '-':
                self.result = int(self.operand1) - int(self.operand2)
        except:
            self.result = ''
        return self.result