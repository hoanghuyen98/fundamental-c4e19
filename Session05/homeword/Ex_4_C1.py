month = int(input(" Enter the number month: "))
female = 0
male = 1
sum_rabbit = 0
for i in range(month):
    if i == 0 or i == 1 : 
        rabbit = 1
    else:
        rabbit = female + male
        female = male
        male = rabbit
    sum_rabbit += rabbit
    print(" Month {0} : {1} pair(s) of rabbit ".format(i, sum_rabbit))
