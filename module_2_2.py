first = int(input('Введите любое число:'))
second = int(input('ещё одно:'))
third = int(input('Ну и последнее:'))
if first == second and third == second:
    print(3, 'равных числа:)')
if first == second or third == first or second == third:
    print(2, 'равных числа:)')
else:
    print(0, 'совпадений:(')

