import random
import string

#List of random names for name generation (this includes numbers and single characters)
RN_list =["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu", "Themis", "Calliope", "Thalia", "Electryone"]
Random_number =["0","10000"]
Random_characters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#List of each department within the company
#["Advertising", "Public Relations", "Market Research", "Marketing", "Content Creation", "Event Management", "Brand Management", "Accounting", "FinOps", "Analytics and Insights" ]

#List of allowed department within the company to use the naming generator
allowed_departments = ['Marketing' , 'Accounting' , 'FinOps' ]

print('''
===================================================================
======= GREETINGS, THIS IS THE EC2 RANDOM NAME GENERATOR! =========
===================================================================
''')

department_ec2 = int(input('How many EC2 instances would you like to launch today with randomize names?: '))
print(f"Generating {department_ec2} randomly name EC2 instances:")

while True:
    department_name = input('Enter your department name: ' )
    if department_name in allowed_departments:
        print('Thank you for the infomation!')
        break
    else:
      print('* This department is not allowed to use this random naming generator! *')
      continue
print(f"Compeleted request of generating random name EC2 instances with the infomation that was provided above. * Please be aware that the maximum limit for EC2 instances is 20 per region *.")

RC = ''.join(random.choices(string.ascii_lowercase, k=4))
RN = ''.join(random.choices(string.digits, k=3))
for _ in range(department_ec2):
        unique_ec2_name = random.choice(RN_list)
        print(f"- {department_name} | {unique_ec2_name}-({RC}{RN})")