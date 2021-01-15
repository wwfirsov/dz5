try:
    diapazon = int(input('Введите диапазон: '))
    sum = 0
    with open("zd5.txt", "a") as my_file:
        for i in range(diapazon):
            stroka = str(i)
            my_file.write(stroka + ' ')
    with open("zd5.txt", "r") as file:
        for line in file:
            s = line.split()
            for word in s:
                value = int(word)
                sum += value
            print('Сумма:', sum)

except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    my_file.close()