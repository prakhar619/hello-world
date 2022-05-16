N = float(input(" Enter a positive no "))
approx = float(input(" Enter the neighbourhood size for approximation "))
loopvar = 1
step = approx ** 2
logvar = 0
if (N >= 1): 
    while(loopvar<= N) and (abs(N-loopvar**2)> approx):  # checking if loopvar( square root guess ) is in 0.1 neighbourhood of N
        loopvar+= step                                  # stepping up guess value
        logvar += 1                                     # no of iterations
        print( logvar , " guess " , loopvar)
else:
    while (abs(N-loopvar**2)>approx):  # checking if loopvar( square root guess ) is in 0.1 neighbourhood of N
        loopvar-= step                                  # stepping up guess value
        logvar += 1                                     # no of iterations
        print( logvar , " guess " , loopvar)
print(" The square root of the no is " , loopvar, "   method : Linear Search")
print(" Time taken ", logvar, "sec")
