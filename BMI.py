'''
n = int(input('enter no of persons: '))
for i in range(n):
    name = input('enter the name: ')
    weight = float(input('enter weight in kgs: '))
    height = float(input('enter height in meters: '))
    if weight > 0 and height > 0:
        bmi = weight/(height**2)
        if bmi < 18.5:
            print(f'{name} is into Under Weight category and BMI is {bmi} ')
        elif 18.5 <= bmi <= 24.9:
            print(f'{name} is into Normal Weight category and BMI is {bmi} ')
        elif 25 <= bmi <=29.9:
            print(f'{name} is into Over Weight category and BMI is {bmi} ')
        else:
            print(f'{name} is into Obesity category and BMI is {bmi} ')
    else:
        print('make sure to enter only postive values')
'''
n = int(input('enter no of persons: '))
for i in range(n):
    while True:
        name = input('enter the name: ')
        weight = float(input('enter weight in kgs: '))
        height = float(input('enter height in meters: '))
        try:
            if weight > 0 and height > 0:
                bmi = weight/(height**2)
                if bmi < 18.5:
                    print(f'{name} is into Under Weight category and BMI is {bmi} ')
                elif 18.5 <= bmi <= 24.9:
                    print(f'{name} is into Normal Weight category and BMI is {bmi} ')
                elif 25 <= bmi <=29.9:
                    print(f'{name} is into Over Weight category and BMI is {bmi} ')
                else:
                    print(f'{name} is into Obesity category and BMI is {bmi} ')
                break
            else:
                print('Height and weight must be postive values')
                pass
        except Exception as e:
            print(f'the Error is {e}')

            