from exceptions_class import PolishCalculator

calculations  = PolishCalculator(input("Введите оператор : "), input("Введите операнд №1 : "), input("Введите операнд №2 : "))

while True:

    calculations.validate_operators()

    if calculations.operation():
        print(f'Выражение:  {calculations.operators} {calculations.operand1} {calculations.operand2} = {calculations.operation()}')
    else:
        print(calculations.validate_operands())
    break

