bacterias = int(input("=====> How many B bacterias are there? "))
time = int(input("=====> How much time in minutes will we wait? "))
total = bacterias * 2 ** (time // 2)
print ("After {0} minutes(s) we would have {1} B Bacterias".format(time, total))