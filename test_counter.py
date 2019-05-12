fruit = 1
abc = dir(fruit)
print(abc)


Result = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
Counter = 1
str_1 = ''
for a in Result:
    if Counter < 3:
        # print(a)
        str_1 += str(a)
        # print(str_1)
        # print("Counter : " + str(Counter))
        Counter += 1
    else:
        str_1 += str(a)
        print(str_1)
        # print("Counter : " + str(Counter))
        Counter = 1
        str_1 = ""
print(str_1)


