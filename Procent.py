perc = 0
i = 0
for i in range(0, 100):
    perc = i + 1
    perc = str(perc)
    if perc[-1] == '1' and perc != '11':
        print(perc, 'процент')
    elif perc[-1] == '2' and perc != '12':
        print(perc,'процента')
    elif perc[-1] == '3' and perc != '13':
        print(perc, 'процента')
    elif perc[-1] == '4' and perc != '14':
        print(perc, 'процента')
    else:
        print(perc, 'процентов')
