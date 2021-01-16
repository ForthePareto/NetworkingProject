

class Bmi:
    def __init__(self, weight, height, age, gender="M"): 
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender.upper()
        self.bmi_calculated = self.calculate_bmi(weight, height)
        

    
    def calculate_bmi(self, weight, height):
        bmi = 0
        if height != 0:
            bmi = weight/(height**2)
        return bmi

    def calculate_daily_calories(self):
        pass

    def check_health_state(self):
        state = " "
        if (20 < self.bmi_calculated < 50) and self.gender == "M":
            state = "healthy"
        elif self.gender == "F":
            state = "kill yourself"
        return state
