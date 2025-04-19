
class Polynomial:
    def __init__(self, coeffs, var = "x"):
        self.coefficients = coeffs 
        self.var = var 
        self.degree = len(self.coefficients) - 1
    
    def getCoeffs(self):
        return self.coefficients 
    
    def getVarName(self):
        return self.var
    

    #digit must be a number 0 through 9
    def superScriptMap(self, digit):
        if(digit == 0):
            return "\u2070"
        elif(digit == 1):
            return "\u00b9"
        elif(digit == 2):
            return "\u00b2"
        elif(digit == 3):
            return "\u00b3"
        elif(digit == 4):
            return "\u2074"
        elif(digit == 5):
            return "\u2075"
        elif(digit == 6):
            return "\u2076"
        elif(digit == 7):
            return "\u2077"
        elif(digit == 8):
            return "\u2078"
        else:
            return "\u2079"
        

    
    #Prints a representation of the polynomial
    def getRepresentation(self):
        s = ""
        n = self.degree 
        for c in self.coefficients:
            if(c == 0):
                n -= 1
                continue
            if(n > 1):
                nString = str(n)
                if(len(nString) > 1):
                    digitsConcatenated = ""
                    for i in range(len(nString)):
                        digitsConcatenated += self.superScriptMap(nString[i])
                    if(c > 0):
                        s += str(c) + self.var + digitsConcatenated + " + "
                        n -= 1
                    else:
                        s = s[:-2]
                        s += str(c) + self.var + digitsConcatenated + " + "
                        n -= 1

                else:
                    if(c > 0):
                        s += str(c) + self.var + self.superScriptMap(n)  + " + " 
                        n -= 1
                    else:
                        s = s[:-2]
                        s += str(c) + self.var + self.superScriptMap(n) + " + "
                        n -= 1

            elif(n == 1):
                if(c > 0):
                    s += str(c) + self.var + " + "
                    n -= 1
                elif(c < 0):
                    s = s[:-2]
                    s += str(c) + self.var + " + "
                    n -= 1
                else:
                    s += str(c) + self.var
                    return s
            elif(n == 0):
                print("c is " + str(c))
                s += str(c)
                return s
        return s
        
    
        







def powerRule(var, exp):
    s = ""
    if (exp == 0):
        s = "0"
        return s
    else:
        s = str(exp) + str(var) + "^" + str(exp-1)
        return s


def coefficients(coeff, var, exp):
    if(coeff == 1):
        return powerRule(var, exp)
    else:
        return str(int(exp)*int(coeff)) + str(var) + "^" + str(int(exp)-1)

def derivOfSum(expression):
    terms = expression.split('+')
    derivsOfTerms = []
    for term in terms:
        indexOfVar = term.find('x')
        if (indexOfVar == -1):
            continue
        else:
            coeff = term[:indexOfVar]
            exp = term[indexOfVar+2:]
            derivsOfTerms.append(coefficients(coeff, 'x', exp))
    s = ""
    for item in derivsOfTerms:
        s = s + item + "+ "
    if(len(s) > 2):
        s = s[:-2]
    return s



x = "x"
#print(coefficients(6, x, 3))
formula = "3x^5 + 4x^3 -x + 4"
#print(derivOfSum(formula))


def gcd(a, b):
    #if b is bigger, switch them so a is always the bigger term 
    if(b > a):
        temp = b 
        b = a 
        a = temp 
    x = b 
    #loop until we get the gcd
    while(x > 0):
        if((a - a//b) == 0):
            return x 
        x = a - (a // b)*b 
        a = b
        b = x 
    return a

print(gcd(60, 12))


p = Polynomial([-3, 4, 0, -8, 12, 4], "z")
print(p.getVarName())
q = Polynomial([1, 2, -1])
print(q.getVarName())

print(p.getRepresentation())

#print("Aaron" + q.superScriptMap(0))
    
    