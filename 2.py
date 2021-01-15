try:
    with open("zd2.txt") as my_file:
        stroki = 0
        for line in my_file:
            stroki += 1
            s = line.split()
            l = len(s)
            print('Количество слов в', stroki, 'строке:', l)
            print('Строка: ', line)

        print('Количество строк в файле: ', stroki)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    my_file.close()