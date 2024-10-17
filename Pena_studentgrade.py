Name = input("Enter your name:")
Section = input("Enter your section:")
Prelim = float(input("Enter prelim grade:"))
Midterm = float(input("Enter midterm grade:"))
Finals = float(input("Enter final grade:"))

if (100 < Prelim < 40) and (100<Midterm<40) and (100<Finals<40):
    Prelim_grade = (Prelim*33.33/100)
    Midterm_grade = (Midterm*33.33/100)
    Finals_grade = (Finals*33.33/100)

    Final= (Prelim_grade + Midterm_grade + Finals_grade)

    print (Final)
else:
    print ("Invalid input. Please input a grade ranging from 40 - 100")