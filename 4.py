try:
    d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    with open("zd4.txt", 'r', encoding='utf-8') as file:
        for line in file:
            s = line.split()
            chislo_en = s[0]
            for key in d:
                if chislo_en == key:
                    with open("new_zd4.txt", 'a', encoding='utf-8') as new_file:
                        new_file.writelines(d[key] + ' ' + s[1] + ' ' + s[2] + '\n')
    with open("new_zd4.txt", 'r', encoding='utf-8') as file:
        print('Новый файл')
        for i in file:
            print(i)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file.close()