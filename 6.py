try:
    dictionary = dict()
    with open('zd6.txt', 'r', encoding='utf-8') as my_file:
        for line in my_file:
            s = line.split()
            predmet = s[0]

            l = len(line)
            integ = []
            i = 0
            while i < l:
                s_int = ''
                a = line[i]
                while '0' <= a <= '9':
                    s_int += a
                    i += 1
                    if i < l:
                        a = line[i]
                    else:
                        break
                i += 1
                if s_int != '':
                    integ.append(int(s_int))

            dictionary[predmet] = sum(integ)
        print(dictionary)

except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    my_file.close()