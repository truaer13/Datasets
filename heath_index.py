def estimate_height(parent1_height_cm, parent2_height_cm, gender='male'):
    if gender == 'male':
        estimated_height = (parent1_height_cm + parent2_height_cm + 13) / 2
    else:
        estimated_height = (parent1_height_cm + parent2_height_cm - 13) / 2
    return estimated_height

def calculate_bmi(weight_kg, height_m):
  #Calculate Body Mass Index (BMI).
  return weight_kg / (height_m ** 2)


def calculate_bmr(weight_kg, height_cm, age, gender='male'):
  #Calculate Basal Metabolic Rate (BMR)
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    return bmr