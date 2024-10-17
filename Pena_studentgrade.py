Name = input("Enter your name:")
Section = input("Enter your section:")
Prelim = float(input("Enter prelim grade:"))

if (Prelim>=40)and(Prelim<=100):
    Midterm = float(input("Enter midterm grade:"))
    if (Midterm>=40)and(Midterm<=100):
        Finals = float(input("Enter final grade:"))
        if (Finals>=40)and(Finals<=100):
            prelim_average = Prelim*33.33/100
            midterm_average = Midterm*33.33/100
            finals_average = Finals*33.33/100
            Final_Grade = (round(prelim_average + midterm_average + finals_average))
            print ("Final Grade:", Final_Grade)
            if (Final_Grade >= 99)and(Final_Grade <= 100):
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "GPA:1.00" ,'\n', "Excellent")
            elif (Final_Grade >= 96)and(Final_Grade <= 98):
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "Your GPA is 1.25, Outstanding")
            elif (Final_Grade >= 93)and(Final_Grade <= 95):
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "Your GPA is 1.50, Superior")
            elif (Final_Grade >= 90)and(Final_Grade <= 92):
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "Your GPA is 1.75, Very Good")
            elif (Final_Grade >= 87)and(Final_Grade <= 89):
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "Your GPA is 2.00, Good")   
            elif  (Final_Grade >= 84)and(Final_Grade <= 86):
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "Your GPA is 2.25, Satisfactory")
            elif (Final_Grade >= 81)and(Final_Grade <= 83):
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "Your GPA is 2.50, Fairly Satisfactory")
            elif (Final_Grade >= 78)and(Final_Grade <= 80):
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "Your GPA is 2.75, Fair")
            elif (Final_Grade >= 75)and(Final_Grade <= 77):
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "Your GPA is 3.00, Passed")
            else:
                print ('\n' , "Name:" , Name , '\n' , "Section:" , Section , '\n', "Final Grade:", Final_Grade , '\n', "Your GPA is 5.00, Failed")
        else:
             print ("Invalid input. Please put a grade ranging from 40-100")
    else:
         print ("Invalid input. Please put a grade ranging from 40-100")
else:
    print ("Invalid input. Please put a grade ranging from 40-100")
>>>>>>> de8c750 (Final commit)
