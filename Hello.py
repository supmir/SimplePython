def Acid_Rain(the_pleasure, the_pain):
    while the_pleasure >= the_pain:
        the_pleasure = the_pleasure - the_pain
    return the_pleasure
the_storm = input()
The_Gods = 1
the_chaos = 2
a_pair = 2
your_willpower = 10
if the_storm <= (a_pair * a_pair):
    if the_storm <= The_Gods:
        print("This ain't allowed!")
    else:
        if your_willpower > the_storm:
            print("I am Prime!")
        else:
            print("I will divide!")
else:
    while the_storm > the_chaos:
        if Acid_Rain(the_storm, the_chaos) == False:
            print("I will divide")
            break
         #Break it down
        the_chaos += 1
if the_storm == the_chaos and the_storm > a_pair * a_pair:
    print("I am Prime!")
