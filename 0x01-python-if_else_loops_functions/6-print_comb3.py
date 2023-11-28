#!/usr/bin/python3
for i in range(100):
    # add "0" to single numbers
    if i < 10:
        i = "0" + str(i)
    i = str(i)
    if i[-1] == i[-2] or i[-2] > i[1]:
        continue

    if int(i) == 89:
        print('{}'.format(i))
    else:
        print('{}'.format(i), end=", ")
