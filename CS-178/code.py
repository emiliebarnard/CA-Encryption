#(c) Emilie Menard Barnard
#Project for Professor Koc's CS178 at UC Santa Barbara, Winter 2013

#CELLULAR AUTOMATA ENCRYPTION
#Note: I used WolframAlpha as my source for all of the rule definitions

import copy

#Define all the rules:
def thirty(oldVector, p, q, r):
    #rule: p XOR (q OR R)=(p+q+r+qr) mod 2
    return (oldVector[p]+oldVector[q]+oldVector[r]+(oldVector[q]*oldVector[r]))%2

def fourtyfive(oldVector, p, q, r):
    #rule: p XOR (q OR (NOT r))=(1+p+r+qr) mod 2
    return (1+oldVector[p]+oldVector[r]+(oldVector[q]*oldVector[r]))%2

def onehundredten(oldVector, p, q, r):
    #rule: (q AND (NOT p)) OR (q XOR r)=(q+r+qr+pqr) mod 2
    return (oldVector[q]+oldVector[r]+(oldVector[q]*oldVector[r])+(oldVector[p]*oldVector[q]*oldVector[r]))%2

############################################

#My CA function that performs the encryption:
def ca(caVector, ruleNumber, numSteps):
    # This function runs the CA 45 rule on the input vector caVector
    
    print "Vector 0: " +repr(caVector)

    for vectorNum in range (1,numSteps+1): #We will produce numSteps many new vectors
        
        oldVector=copy.deepcopy(caVector); #store the old vector values
    
        print ("Vector "+repr(vectorNum)+":"),
        
        for vectorIndex in range(len(caVector)): #this will iterate through the elements in the vector and update the values
            
            p=(vectorIndex-1)%17 #wrap around for boundary cases
            q=vectorIndex%17
            r=(vectorIndex+1)%17
            
            #My hack-ish switch case set up since python doesn't have its own switch case support:
            callRule={30: thirty,
                        45: fourtyfive,
                        110: onehundredten,
            }
                            
            caVector[vectorIndex]=callRule[ruleNumber](oldVector, p, q, r)
            
            print (repr(caVector[vectorIndex])),
    
        print "\n"

    return

############################################

#call the code (hard-coded inputs for meow):

inputVector=([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) #must be of size 2*numSteps+1
rule=110
numSteps=8

ca(inputVector, rule, numSteps)