from exceptions_class import PolishCalculator

polish_input = input("Введите данные: ")

calculations  = PolishCalculator(polish_input)

while True:

    calculations.validate_operators()

    if calculations.operation():
        print(f'Выражение:  {calculations.split_data[0]} {calculations.split_data[1]} {calculations.split_data[2]} = {calculations.operation()}')
    else:
        print(calculations.validate_operands())
    break

