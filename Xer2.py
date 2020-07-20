name= input('Ваше имя: ')
height = float(input('Ваш рddост: '))
weight = float(input('Ваш вес: '))

bmi = weight / (height ** 2)
print(name,',''индекс вашего тела составляет:', f"{bmi:.1f}")

if 1>bmi<24:
    print('Вы Дрищ')
elif 25>bmi<30:
    print('Это Норма')
else:
    print('Ну и жирдяй')

