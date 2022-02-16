from sympy import diff, log, N, Symbol 
# Differentiate, Natural logarithm, Numerical solver, Symbols for values (they are able to represent/get treated as a value)

from termcolor import colored, cprint #coloring for text in terminal
from time import sleep #pause program for x seconds



#--------------FANCY STUFF------------------#

#for printing each characther individually
def printF(txt):
    for char in txt:
        print(char, end="", flush=True)
        sleep(.01)

#print logo
cprint("""

███╗   ██╗██╗   ██╗██╗     ██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗████████╗███████╗                
████╗  ██║██║   ██║██║     ██╔══██╗██║   ██║████╗  ██║██║ ██╔╝╚══██╔══╝██╔════╝                
██╔██╗ ██║██║   ██║██║     ██████╔╝██║   ██║██╔██╗ ██║█████╔╝    ██║   ███████╗                
██║╚██╗██║██║   ██║██║     ██╔═══╝ ██║   ██║██║╚██╗██║██╔═██╗    ██║   ╚════██║                
██║ ╚████║╚██████╔╝███████╗██║     ╚██████╔╝██║ ╚████║██║  ██╗   ██║   ███████║                
╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                
                                                                                               
██████╗ ███████╗███████╗████████╗███████╗███╗   ███╗███╗   ███╗███████╗██╗     ███████╗███████╗
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║████╗ ████║██╔════╝██║     ██╔════╝██╔════╝
██████╔╝█████╗  ███████╗   ██║   █████╗  ██╔████╔██║██╔████╔██║█████╗  ██║     ███████╗█████╗  
██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██║     ╚════██║██╔══╝  
██████╔╝███████╗███████║   ██║   ███████╗██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗███████╗███████║███████╗
╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝

""", "white", "on_green")

sleep(2)
#------------FANCY STUFF END----------------#

#print method options
printF("""
 
 Vælg en af følgende metoder:
------------------------------

 1) Bisektion

 2) Newton Raphson


""")

methodrun = True
while methodrun:
    method = input(colored("Metode Nummer: ", "green")) #choose method


    #-------------BISECTION METHOD------------#
    if method.upper() == "1":
        print(colored("Nulpunkt via bisektion", "white")) #inform user of selected method
        print("")

        x = Symbol("x") #treat x as a placeholder for a value

        L = [2, 1]
        while L[0] > L[1]: #while v > h

            try:
                L = [float(i) for i in input(colored("input v;h = ", "green")).split(";")]
                #get input from user, seperate by ";" and list other stuff, convert str to float
                
                if L[0]>L[1]: #if v > h, inform user that arg must -> v < h 
                    print(colored("v skal være mindre end h", "red"))
                    print("")
                
                elif len(L) > 2: #if more than 2 args is given, inform user
                    print(colored("intervallet skal kun indeholde 2 værdier", "red"))
                    print("")
                    L = [2, 1]

                else:
                    f = input(colored("f(x) = ", "green"))

            except: #secure errors if given arg is not a number
                print(colored("Intervallet skal være tal", "red"))
                print("")

        testfor = L[1]-L[0] > 0.0001
        while testfor: #secure precision on 4 decimals
            x = (L[0]+L[1])/2
            calc = round(eval(f), 6) #needs to be rounded or else we will get an error, ex.: 2.22044604925031e-16

            if calc == 0:
                testfor = False
            elif calc < 0: #if f(x) < 0 -> x overwrites v
                L[0] = x
            else:
                L[1] = x #if f(x) > 0 -> x overwrites h
        print("")

        #fancy printing with colors and stuff
        print("Sidste Interval: ", end=""), print(colored(f"]{round(L[0], 6)} ; {round(L[1], 6)}[", "cyan"))
        print("Skæring for f(x) ift. x-aksen: ", end=""), print(colored(round(x, 6), "cyan"))

    #-------------BISECTION METHOD END-------------#



    #-------------NEWTON RAPHSON METHOD------------#

    elif method.upper() == "2":
        print("Nulpunkt via Newton Raphson") #inform user of selected method
        print("")

        x = Symbol("x") #treat x as a placeholder for a value

        f = input(colored("f(x) = ", "green"))
        f_ = str(diff(eval(f), "x"))
        
        #make sure the value that x will hold is a number:
        x = "a"
        testfor = type(x) != float or type(x) != int
        while testfor:
            try:
                x = float(input(colored("x = ", "green")))
                testfor = False
            except:
                print(colored("x skal være et tal", "red"))
                print("")
        
        print("")
        print("Differentiet funktion: ", end=""), print(colored(f_, "cyan")) #print differentiated func

        calc = (x*eval(f_) - eval(f)) / eval(f_)
        print("Fixpunktsfunktion: ", end=""), print(colored(f"x * {f_} - {f} / {f_}  ;  x0 = {x}", "cyan")) #clarify method for user
        res = N(calc) # N -> numerical solver
        # x - f(x) / f'(x)
        # IN OTHER TERMS, FOLLOWING THE METHOD: (x*f'(x) - f(x)) / f'(x)

        while abs(x-res) > 0.0001:
            x = res
            res = N((x*eval(f_) - eval(f)) / eval(f_))
        print("Skæring for f(x) ift. x-aksen: ", end=""), print(colored(round(res, 6), "cyan")) #print answer
            
    #-------------NEWTON RAPHSON METHOD END------------#



    #------------------SECURE TYPOS--------------------#
    else:
        print(colored("Vælg imellem de 2 metoder, tak!", "red"))
        print("""
 1) Bisektion
 2) Newton Raphson
         """)
    
    print("")
