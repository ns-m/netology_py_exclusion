from exceptions_class import Exceptions

while True:
    Exceptions()
    Exceptions().exceptions_operators()
    #Exceptions().exceptions_operands()

    if Exceptions().operation():
        print(f'Выражение : {Exceptions().operators} {Exceptions().operand1} {Exceptions().operand2} = {Exceptions().operation()}')
    else:
        print(Exceptions().exceptions_operands())
    break

