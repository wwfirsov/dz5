try:
    with open("zd3.txt", 'r', encoding='utf-8') as my_file:
        sum_zp = 0
        col_sotrudnikov = 0
        for line in my_file:
            s = line.split()
            col_sotrudnikov += 1
            sum_zp += float(s[1])
            zp = float(s[1])
            if zp < 20000:
                print('Сотрудник:', s[0], 'имеет зарплату менее 20000')
        print("Общее количество сотрудников:", col_sotrudnikov)
        sum = float("{0:.2f}".format(sum_zp / col_sotrudnikov))
        print("Средняя величина дохода всех сотрудников:", sum)
    with open("zd3.txt", 'r', encoding='utf-8') as file:
        print('Список сотрудников')
        for i in file:
            print(i)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    my_file.close()
    file.close()