def foo(letter_grade):
    gpaA = "4.00"
    gpaB = "3.00"
    gpaC = "2.00"
    gpaD = "1.00"
    gpaF = "0.00"

    #This is for all of the A letter grades. If one doesn'the work, it'll go to the next code.
    if (letter_grade == ("A")) :
      return ("Your GPA is a " + gpaA + ".")

    #This is for all of the B letter grades. If one doesn'the work, it'll go to the next code.
    if (letter_grade == ('B')):
      return ("Your GPA is a " + gpaB + ".")

    #This is for all of the C letter grades. If one doesn'the work, it'll go to the next code.
    if (letter_grade == ("C")) :
      return ("Your GPA is a " + gpaC + ".")

    #This is for all of the D letter grades. If one doesn'the work, it'll go to the next code.
    if (letter_grade == ("D")):
      return ("Your GPA is a " + gpaD + ".")

    #This is for all of the F letter grades. If one doesn'the work, it'll go to the next code.
    if (letter_grade == ("F")):
      return("Your GPA is a " + (gpaF) + ".")

    else :
      return ("")