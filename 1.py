try:
    with open("zd1.txt", "a") as my_file:
        flag = 1
        while flag == 1:
            str_list = input("Введите данные (для завершения введите пробел): ")
            if str_list == " ":
                my_file.close()
                flag = 0
                with open("zd1.txt") as file:
                    print("Готовый файл: ")
                    for line in file:
                        print(line)
            else:
                my_file.writelines(str_list + '\n')
                print("Данные записаны")

except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    my_file.close()
