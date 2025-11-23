# SAVINGS AND INTEREST CALCULATOR
print ("Please enter your Name , Age , Amount ,interest rate ,Time period of investement")
name = input("Enter your name :-")
age = int(input("enter your age:-"))
tuple = ('Colgate-Palmoliv','P & G Hygiene','Nestle India','tcs','Glaxosmi Pharma','Billionbrains',	'Hindustan Zinc',	'Page Industries','LG Electronics',	'Anand Rathi Wea','Gillette India',	'GE Vernova T&D',	'Hyundai Motor I','Life Insurance',	'Britannia Inds',	'I R C T C',	'Coal India' ,'BSE','Abbott India','Marico')
tuple_two=(2.34,0.86,1.05,1.90,1.68	,0.00,6.33,2.31,0.00,0.37,1.35,0.17,0.90,1.33,1.29,1.16,7.01,0.21,1.61,1.42)
t=len(tuple)
print("    THE LIST OF STOCKS :- ")
print("-------------------------------------------------------------------------------------------")
for i in range (0,t):
    print(f"{i+1} . {tuple[i]} and interest for each is---> {tuple_two[i]}") 
    print("-------------------------------------------------------------------------------------------")
q=input("for custum investement calculater enter (1)/ for calculating from the given stocks enter (2):- ")
if age >17:
    if q=='2':
        amt=int(input("Enter the desired amount you want to invest:-"))
        yr=int(input("Enter number of years for whic you want to invest:-"))
        e=int(input("enter the serial number of the stock you want to invest in:-"))
        p=int(input("For interest calculate by [compund interest input (1) / simple interest input (2) / if you want both enter (3)] :-"))
        if p==2:
            interest=(amt*yr*tuple_two[e-1])/100
            print (f"interest after {yr} is {interest}and the amount is {amt+interest}")
        elif p==1:
            interest=amt*[(1+tuple_two[e-1]/100)]**yr
            print (f"interest after {yr} is {interest}and the amount is {amt+interest}")
        elif p==3:
            interest1=(amt*yr*tuple_two[e-1])/100
            f=(1+tuple_two[e-1]/100)**yr
            interest2=amt*f
            print (f"when calculated using (simple interest) interest after {yr} is {interest1} and the amount is {amt+interest1}")
            print (f"when calculated using (simple interest) interest after {yr} is {interest2} and the amount is {amt+interest2}")
        else:
            print ("Please enter a valid number")
    if q=='1':
        amt=int(input("Enter the desired amount you want to invest:-"))
        ir=float(input("Enter the interest rate of your savings:- "))
        yr=int(input("Enter number of years you are going to invest:- "))
        p=int(input("For interest calculate by [compund interest input (1) / simple interest input (2) / if you want both enter (3)] :-"))
        if p==2:
            f=amt*ir*yr
            interest=(f)/100
            print (f"interest after {yr} is {interest}and the amount is {amt+interest}")
        elif p==1:
            interest=amt*[(1+ir/100)]**yr
            print (f"interest after {yr} is {interest}and the amount is {amt+interest}")
        elif p==3: 
            f=amt*yr
            interest1=f*ir/100
            print (f"when calculated using (simple interest) interest after {yr} is {interest1} and the amount is {amt+interest1}")
            r=(1+ir/100)**yr
            interest2=amt*r
            print (f"when calculated using (coumpund interest)interest after {yr} is {interest2}and the amount is {amt+interest2}")
        else:
            print("Please enter a valid number for the process")
    else:
        print("try again !")
else :

    print ("Sorry!! Required age not reached ,try again . ")
