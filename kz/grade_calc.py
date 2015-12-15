def grades(midterm, final, homework):
    print "You got %d on your midterm." % midterm
    print "You got %d on your final." % final
    print "You got %d on your homework." % homework
    final_grade = (.4*midterm)+(.5*final)+(.1*homework)
    if (final_grade>90):
        print "You got an A in the class."
    elif (final_grade>80):
        print "You got a B in the class."
    elif (final_grade>70):
        print "You got a C in the class."
    elif (final_grade>60):
        print "You got a D in the class."
    else: 
        print "You failed, see you next year."

grades(70, 99, 80)