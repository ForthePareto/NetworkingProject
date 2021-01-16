class BMI():

    def __init__(self,mass,height):
        bmi = self.calcBmi(mass,height)
        self.notify(bmi)
    def calcBmi(self,mass,height):
    
        return round(mass / ((height / 100) ** 2),ndigits=1)

    def identifyCategory(self,bmi):
        if (0 < bmi <= 16):
            return 'Severely Underweight'
        elif (16 < bmi <= 18.5):
            return 'Underweight'
        elif (18.5 < bmi <= 25):
            return 'Normal'
        elif (25 < bmi < 30):
            return 'Overwight'
        elif (30 < bmi):
            return 'Obese'
        else:
            return 'why r u gai'
        


    def notify(self,bmi):
        print(f'Your BMI is {bmi}, {self.identifyCategory(bmi)}')

# b = BMI(65,190)