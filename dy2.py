
#! pb1 

def generate_arr(len,st):
    st-=1
    arr = [st+i for i in range(1,len+1)]
    # range(num) for num
    return arr

def gener_arr(len,st):
    arr = []
    for i in range(len):
        arr+=[st]
        st+=1
    return arr
# print(gener_arr(4,3))
# print(generate_arr(3,1))

#! pb2
# define a functio that takes a num 
def num_divisible(num:int):
    # num /3 ? or num /5 or both
    if isinstance(num,int):
        if num%3 == 0 and num%5 == 0:
            print('FizzBuzz')
        elif num%3 == 0:
            print('Fizz')
        elif num%5 == 0:
            print('Buzz')
        else:
            print('NOt Divisable')
    else:
        print('Please enter an Iteger Value!!')

# num_divisible(3)
# num_divisible(15)
# num_divisible(10)
# num_divisible(12)

#!pb 3

def enter_str():
    user_inp = input('type str: ')
    user_inp = user_inp[::-1]
    return user_inp

# print(enter_str())

#!pb 4
import re
# while loop => probmt user to enter his name 

# while True:
#     name_pattern = r"^[A-Za-z]+$"   
#     ur_name = input('ur name: ')

#     if bool(re.match(name_pattern,ur_name)):
#         email_pattern = r'\w+@\w+\.\w+'
#         ur_email = input('ur Email: ')
#         if bool(re.match(email_pattern,ur_email)):
#             print(ur_name,ur_email)
#             break
#         else:
#             print('please Enter a Valid email Adress')
#     else:
#         print('Enter a Valid name!!')


#!pb 5
alphabet = "abcdefghijklmnopqrstuvwxyz"

# strg = 'abdelrhman'

def find_longest_alphabetical_substring(input_str):
    temp_str = ''
    dic = {}
    for idx in range(len(input_str)):
        
        if idx == 0 :
            temp_str+= input_str[idx]
            continue
        elif ord(input_str[idx-1]) + 1 == ord(input_str[idx]):
            temp_str+= input_str[idx]
        else:
            dic[temp_str] = len(temp_str)
            temp_str = ''
    max_key = max(dic, key=lambda key: dic[key])
    return max_key

# print(find_longest_alphabetical_substring('abdlerhman'))

def find_longest_alphabetical_substring(input_str):
    temp_str = ''
    logest_str = ''
    for idx in range(len(input_str)):
        
        if idx == 0 :
            temp_str+= input_str[idx]
            continue
        elif ord(input_str[idx-1]) + 1 == ord(input_str[idx]):
            temp_str+= input_str[idx]
        else:
            temp_str = ''
        if len(temp_str) > len(logest_str):
            logest_str = temp_str
    return logest_str

# print(find_longest_alphabetical_substring('abcdealfjsdalkfj'))

def read_number():
    summ= 0
    cnt = 0
    while True:
        num = input('num= ')
        if num == 'done':
            break
        else:
            try:
                summ+=float(num)
                cnt+=1
            except ValueError:
                print('please just type an number')
    try:
        print(summ,summ/cnt)
    except ZeroDivisionError:
        print('No number is Entered')

# read_number()

# import modules
import re
import random

def guessing_game():
    words = ['apple', 'banana', 'cat','dog','cicle','python']
    rand_word = random.choice(words)
    selected_litters = ''
    ur_name = input('What is ur Name? ')
    for i in range(7):
        selected_litter = input('enter a letter: ')
        if selected_litter in rand_word:
            selected_litters+=selected_litter
            pattern = f'[^{selected_litters}]'
            substr =re.sub(pattern,'-',rand_word)
            print(substr)
        else:
            print('worong\ntry Again :(')
    
        if substr == rand_word :
            print(f'Congratulations {ur_name}:)')
            return
    print('U FAILED :(')

guessing_game()