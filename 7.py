import json

with open("zd7.txt", 'r', encoding='utf-8') as file:
    firm_list = []
    firm_dict = {}
    sr_pr_dict = {}

    all_profit = 0
    col_comp = 0
    ubitok_com = 0
    for line in file:
        s = line.split()
        viruchka = s[2]
        izdergki = s[3]
        profit = float(viruchka) - float(izdergki)
        if profit >= 0:
            all_profit += profit
            col_comp += 1
            print('Прибыль ' + s[1] + ' ' + s[0] + ':', profit)
        else:
            ubitok_com += 1
            print('Убыток ' + s[1] + ' ' + s[0] + ':', profit)

        firm_dict[s[0]] = profit

    pribil_itog = all_profit / col_comp
    sr_pr_dict['average_profit'] = pribil_itog

    print('Средняя прибыль', col_comp,  'компаний: ', pribil_itog)
    print('Компаний с убытком: ', ubitok_com)

    firm_list =[firm_dict, sr_pr_dict]

    print('Готовый список: ', firm_list)

    with open("zd7.json", "w") as write_f:
        json.dump(firm_list, write_f)