bob = ["bob smith", 42, 300000, 'software']
sue = ["sue jones", 45, 400000, 'hardware']
#print (bob[0],sue[2]) #fetch name , pay

#print (bob[0].split()[-1]) #bob's last name
#sue[2] *=1.25 #increase 1.25 times sue salary
#print(sue[2])

def showLastNames(ppl):
    for p in ppl:
        print(p[0].split()[-1])

def showAll(ppl):
    for p in ppl:
        print(p)

def incSalary(ppl, ratio):
    for p in ppl:
        p[2] *= ratio

def selectPay(ppl):
    return [p[2] for p in ppl]

def selectPay2(ppl):
    return list(map(lambda x:x[2], ppl))

