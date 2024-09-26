#Sep 25/2024
#The below program check if a String is a palindrome or symmetrical
is_symmetrical = 'Kenya'
is_symmetrical2 = 'Mum'
S1 = is_symmetrical.lower()
S2 = is_symmetrical2.lower()
if S1[::-1] == S1:
    print("True")
else:
    print("False")

if S2[::-1] ==  S2:
    print("true")
else:
    print("false")

# Ways to remove the i'th character from a String
stringExample = "String"
ith = "S"
indx = stringExample.index(ith)
print(stringExample.replace(stringExample[indx], ' '))
#finding String Length in python
length = "Length"
print(len(length))
#Avoiding Spaces in String
example = "list example"
splited = example.strip(' ').replace(' ', '')
print(splited)
#Program to print even length words in a String
def even(ListtL):
    even_list = []
    print(listL)
    x = ''
    for item in listL:
         x = item[:2]
         even_list.append(x)
    return even_list
even_length_string = 'This is a python script'
listL = list(even_length_string.split(' '))
print(str(even(ListtL=listL)).strip(']['))
#26 sep/2024
#This program Uppercases the latter half of the String
List_uppercase = "Encyclopedia"
length = int(len(List_uppercase)/2)*-1
ln = length * -1
List_uppercase = List_uppercase[:ln] + List_uppercase[length:].upper()
print(List_uppercase)
#This program capitalises the first word and the last word in a String
String_example = 'thisIsCapital'
first = String_example[0].upper()
last = String_example[-1].upper()
String_example=String_example.replace(String_example[0], first)
String_example = String_example.replace(String_example[-1], last)
print(String_example)
#This program checks if a string contains
stringNum = "Ilove254"
flag = False
flag_d = False
for i in stringNum:
    if i.isalpha():
        flag = True
    if i.isdigit():
        flag_d = True

if flag and flag_d:
    print("True")
else:
    print("False")
#This programs accepts a string if it contains a vowel in it
def vowel(vowels_tests):
    vowels = list('aeiou')
    changed = list(vowels_tests)
    iS = [i for i in vowels if i in vowels_tests]
    if vowels == iS:
        print("accepted")
    else:
        print("Not accepted")

vowel(vowels_tests='abracadabraiou')
#This program prints matching characters in two strings
St1 = list("onehundre42di")
St2 = list("2")
new = [i for i in St1 if i in St2]
print(new)