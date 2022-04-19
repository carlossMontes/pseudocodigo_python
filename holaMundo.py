num = 120

for i in range(2, num+1):
    if num%i != 0:
        print('NINGUNO')
        quit()

    num = num/i
    if num==1:
        print(format(exp,'0.0f'),'!')
        quit()
    exp = num