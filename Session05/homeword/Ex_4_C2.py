
def rabbit(month):
    if month <= 1 :
        return month
    else:
        return(rabbit(month-1) + rabbit(month-2))
month = 5 
sum_rabbit = 1
if month < 0:
    print(" Please enter a position integer ")
else:
    for i in range(month):
        t = rabbit(i)
        sum_rabbit += t
        print(" Month {0} : {1} pair(s) of rabbit ".format(i, sum_rabbit))

