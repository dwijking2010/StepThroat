def find_prob(a,b):
    if a==1:
        prob_a = 0.2
        if b ==1:
            prob_bga = 0.85
        elif b==2:
            prob_bga = 0.15
        else:
            print("You don't exist")
        prob_a_and_b = prob_a * prob_bga
        print("Prob of b given a: ", prob_bga)
        print("Prob of both the events occuring: ", prob_a_and_b)
    elif a==2:
        prob_a = 0.8
        if b ==1:
            prob_bga = 0.02
        elif b==2:
            prob_bga = 0.98
        else:
            print("You don't exist")
        prob_a_and_b = prob_a * prob_bga
        print("Prob of b given a: ", prob_bga)
        print("Prob of both the events occuring: ", prob_a_and_b)  
    else:
        print("Get OUT!!")
print("Let's calculate prob. Please enter choices for the events ...")
print("Person has step throat \n 1. Ha \n 2.Na")
a =int(input("Enter your choices (1/2): "))

print("Person has step throat \n 1. Ha \n 2.Na")
b =int(input("Enter your choices (1/2): ")) 

print("Prob for event a & b: ")
find_prob(a,b)