def love_calculator():
    name1= input("What's your name? \n").lower()
    name2 = input("What's their name? \n").lower()
    print(name1)
    count1= 0
    count2= 0
    love_text = "love"
    true_text = "true"
    for x in love_text:
        count1+= name1.count(x)
        count1+= name2.count(x)
    for x in true_text:
        count2+= name1.count(x)
        count2+= name2.count(x)
    print("count 1 is: ", count1)
    #print("count2 is: ", count2)
    love_score = str(count2)+str(count1)
    love_score = int(love_score)
    if love_score < 10 or love_score > 90:
        print("Your score is ",love_score, " you go together like coke and mentos.")
    elif love_score > 40 and love_score < 90:
        print("Your score is " ,love_score , "you are alright together.")
    else :
        print("your love score is " + str(love_score))
love_calculator()