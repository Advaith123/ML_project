import diet_recommender as dr

def calcbmi(weight, height):
    bmi = weight/((height/100)**2)
    print("Your body mass index is: ", bmi)
    if (bmi < 16):
        print("Acoording to your BMI, you are Severely Underweight")
        clbmi=4
    elif ( bmi >= 16 and bmi < 18.5):
        print("Acoording to your BMI, you are Underweight")
        clbmi=3
    elif ( bmi >= 18.5 and bmi < 25):
        print("Acoording to your BMI, you are Healthy")
        clbmi=2
    elif ( bmi >= 25 and bmi < 30):
        print("Acoording to your BMI, you are Overweight")
        clbmi=1
    elif ( bmi >=30):
        print("Acoording to your BMI, you are Severely Overweight")
        clbmi=0
    return bmi, clbmi



if __name__ == '__main__':
    ans = ''
    while(ans != 'BYE!'):
        print("######################################")
        ans = input()
        print("PLEASE ANSWER THE FOLLOWING QUESTIONS:")
        print("How old are you?: ")
        age = int(input())
        print("Are you a vegetarian or a non-vegetarian?(0/1): ")
        veg = int(input())
        print("Please enter your Weight in kg: ")
        weight = float(input())
        print("Please enter your Height in cm: ")
        height = float(input())
        print('Please choose your goal: ')
        print('1. Weight Loss\n2. Weight Gain\n3. Maintain Health')
        choice = int(input())
        bmi, clbmi = calcbmi(weight, height)
        if choice == 1:
            dr.Weight_Loss()
        elif choice == 2:
            dr.Weight_Gain()
        elif choice == 3:
            dr.Healthy(age, veg, bmi, clbmi)
        else:
            print("Invalid Choice!!")
