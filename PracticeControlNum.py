def proclist(num1, num2, num3):
    anslist = []
    str1 = "The sum is: " + str(num1 + num2 + num3)
    str2 = "The product is: " + str(num1 * num2 * num3)
    str3 = "The average is: " + str(int((num1 + num2 + num3)/3))
    anslist.append(str1)
    anslist.append(str2)
    anslist.append(str3)
    sizlist = []
    sizlist.append(num1)
    sizlist.append(num2)
    sizlist.append(num3)
    sizlist.sort()
    diff = int(sizlist[2] - sizlist[0])
    difhf = int(diff/2)
    mean = sizlist[0] + difhf
    str4 = "The mean is: " + str(mean)
    anslist.append(str4)
    return anslist

    ## THE GHOST OF THE SHADOW ##