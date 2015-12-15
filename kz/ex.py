def displayBoard:
    for i in range(0,4):
        for j in range(0,4):
            location = i*4 + j
            if (location<10):
                location = " " +str(location)
            print location,
        print

