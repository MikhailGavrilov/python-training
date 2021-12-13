lis_n = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
len_list = len(lis_n)
i = 0
while i < len_list:
    i = i + 1
    l_part = lis_n.pop(0)
    #print(l_part)
    l_part2 = l_part.split(' ')
    # print(l_part2)
    part3 = l_part2[-1]
    # print(part3)
    part4 = part3.title()
    # print(part4)
    print("'Привет,", part4, "!'")



# # list_names = (list_names.title())
# # print(list_names)
#
