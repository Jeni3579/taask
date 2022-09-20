#Filterd even num list 
Input_list = range(1,61)
out = []
for num in Input_list:
    if num %2 == 0:
        out.append(num)
print(out)


# Eligible for voting 
age = int(input("Enter your age :"))

if age >= 18:
    print("You are eligible for voting ")
else:
    print("You are not eligible for voting")


###
f_name=input("Firstname")   
s_name=input("Secondname")

def full_name_generator(first_name,second_name):
    full_name = f"{first_name} {second_name}"
    return full_name

print("Your full name is:", full_name_generator(f_name,s_name))

###days list  
days_list =[
    'Sunday',
    'Monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
]

for day in days_list:
    print(f"The single days is: {day}")


#odd
def odd(x):
    return x % 2 == 1
 
a = [2, 5, 7, 8, 10, 13, 16]
 
result = filter(odd, a)
print('Original List :', a)
print('Filtered List :', list(result))