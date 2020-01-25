import sys
class PolishCalculator:

    def __init__(self, polish_input):
        self.polish_input = polish_input
        try:
            if self.polish_input[1] == ' ' and self.polish_input[3] == ' ':
                split_data = self.polish_input.split()
            elif self.polish_input[1] != ' ' and self.polish_input[2] == ' ':
                split_data = (self.polish_input.replace(self.polish_input[1], ' '+self.polish_input[1])).split()
            elif self.polish_input[1] == ' ' and self.polish_input[3] != ' ':
                split_data = (self.polish_input.replace(self.polish_input[3], ' '+self.polish_input[3])).split()
            else:
                split_data = list(self.polish_input)
        except IndexError:
            print('введены не все операнды')
            sys.exit()
        self.split_data = split_data

    def validate_operators(self):
        operators_list = ['+', '-', '*', '/']
        assert (self.split_data[0] in operators_list), 'Введите один из данных операторов: +, -, *, /'

    def validate_operands(self):
        try:
            if self.split_data[1] == '0' or self.split_data[2] == '0':
                self.split_data[1], self.split_data[2] = int(0), int(0)
            try:
                self.split_data[1] / self.split_data[2]
            except ArithmeticError:
                print('арифметическая ошибка')
            except TypeError:
                print('вводить только числа')
        except IndexError:
            print('введены не все операнды')
            sys.exit()

    def operation(self):
        result = 0
        self.result = result
        try:
            if self.split_data[0] == '/':
                self.result = int(self.split_data[1]) / int(self.split_data[2])
            elif self.split_data[0] == '+':
                self.result = int(self.split_data[1]) + int(self.split_data[2])
            elif self.split_data[0] == '*':
                self.result = int(self.split_data[1]) * int(self.split_data[2])
            elif self.split_data[0] == '-':
                self.result = int(self.split_data[1]) - int(self.split_data[2])
        except:
            self.result = ''
        return self.result