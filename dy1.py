#
#! pb1

vowels = ['a', 'e', 'i', 'o','u']

vo = ''.join(vowels)
# print(vo)
stg = 'ITI is a great place to learn from'
cnt = 0
for char in stg.lower():
    if char in vowels:
        cnt+=1


for vowel in vo :
    cnt+= stg.lower().count(vowel)

print(cnt)
str1 =''
for char in stg.lower():
    if char in vo and char not in str1:
        cnt+=stg.lower().count(char)
        str1 += char
# print(cnt)

def cnt_vowels(s):
    lowered_str = s.lower()
    return sum(lowered_str.count(vo) for vo in vowels)

# print(cnt_vowels(stg))

#!pb2

# arr = ['e','f','a','b','l']
# arr = [2,4,3,232,22,4]

# arr = list(input('enter :').split())
# print(arr)
# arr.sort()
# print(arr)
# arr.sort(reverse=True)
# print(arr)


#!pb3
# iti occurs 
word = 'iti'
str1 =  'iti is a great place to learn from it is iti'
# cnt = str1.count(word)
# print(cnt)
#? another way
lst = list(str1.split())
# print(lst)
for chars in lst:
    if word == chars:
        cnt+=1
print(cnt)

#!pb4
for char in str1.lower():
    if char in vo:
        str1 = str1.replace(char,'')

print(str1)

#!pb5
# get the index of first i
# append the index in a list
# replace it with empty str

indxs = []

for char in str1:
    if char in 'i':
        indxs.append(str1.index('i'))
        str1=str1.replace('i','',1)
print(indxs)

#!pb6
num_passed = int(input('num='))

# nested loop and range()

# empty list to append the other lists 
main_lst = []
for num1 in range(1,num_passed+1):
    temp_lst = []
    for num2 in range(1,num1+1):
        temp_lst.append(num1*num2)
    
    main_lst.append(temp_lst)

print(main_lst)

#!pb7 

# try using range()
# num in range(1,passed_num+1)
# 1 => paased - num print(' '*+'*'*num)

for current_num in range(num_passed+1):
    space_num = num_passed-current_num
    print(' '*space_num+'*'*current_num)
