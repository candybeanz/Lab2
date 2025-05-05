w=float(input("Enter w: "))
h=float(input("Enter h: "))

def calBMI(w,h):
    print("Height is: " + str(h))
    print("Weight is: " + str(w))
    bmi=w/(h*h)
    return bmi

bmivalue=calBMI(w,h)
print("Your BMI is: "+str(bmivalue))

def condi(bmivalue):
    bm=bmivalue
    if (bm<18.5):
        print("Underweight..")
        return -1
    elif(bm>=18.5 and bm<=25.0):
        print("Normal weight...")
        return 0
    else:
        print("Overweight")
        return 1
    return
condi(bmivalue)

