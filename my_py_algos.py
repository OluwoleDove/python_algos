''' THIS IS A COMPILATION OF SOME ALGORITHMS I WROTE IN PYTHON '''

#THIS PROGRAM TAKES TWO INTEGER NUMBERS AND RETURNS A LIST OF ODD NUMBERS 
#AND A COUNT OF EVEN NUMBERS BETWEEN THE INTEGERS
def even_odd(i, j):
    try:
        if isinstance(i, int) == False or isinstance(j, int) == False:
            raise ValueError("Only Integer values please")
        else:
            if i > j:
                k = j
                j = i
                i = k
    except ValueError as e:
        print(e)
    print(("ITERATING BETWEEN [0] AND [1]").format(i, j))
    return_list = []
    odd_num_list = [] #An empty list
    even_num_count = 0 #integer value for even number counts initialized to zero

    for number in range(i, j):
        if number % 2 > 0: #number is an odd nuber
            odd_num_list.append(number)
        elif number % 2 == 0: #is number an even number, i.e is the remainder = 0?
            even_num_count += 1
    return_list.append(odd_num_list, even_num_count)

'''EXECUTING THE FUNCTION'''
i = int(input("The first integer number please: "))
j = int(input("Your second integer number: "))
even_odd = even_odd(i, j)
print("Odd numbers are \n", even_odd[0])
print()
print("The count of even numbers are ", even_odd[1])

####LET's PRINT TRIANGLES OF ASTERISKS
print("\n")
print("PRINTING A TRIANGLE OF ASTERISKS BY CALLING PRINT METHOD ACCORDING TO THE NUMBER OF ROWS")
char = "*"
str_out = ""
for i in range(1,11):
    str_out += char
    print(str_out)
    
#LET'S CALL THE PRINT FUNCTION ONCE
print("\n")
print("PRINTING A TRIANGLE OF ASTERISKS BY CALLING PRINT METHOD ONCE")
char = "*"
str_out = ""
main_str = ""

for i in range(1,11):
    str_out += char
    main_str += str_out + "\n"
print(main_str)

##PRINT MULTIPLATION TABLE FROM 1 TO 12
print("PRINTING 12 BY 12 MULTIPLICATION TABLE HORIZONTALLY")
num = 0
out_str = "" #Initializing output string
#Below are 12 instances of i and 144 instances of j

for i in range(1,13):
    for j in range(1,13):
        num = i*j
        out_str += str(i) + " * " + str(j) + " = " + str(num) + "\n"
    print(out_str)
    out_str = "" #After eact complete j iterations, initialize output string again
    print()

        

##PRINT MULTIPLATION TABLE FROM 1 TO 12
print("PRINTING 12 BY 12 MULTIPLICATION TABLE SIDE BY SIDE")
num = 0
out_str = "" #Initializing output string
#Below are 12 instances of i and 144 instances of j

for i in range(1,13):
    for j in range(1,13):
        num = j*i
        out_str += str(j) + "*" + str(i) + "=" + str(num) + "\t"
    print(out_str)
    out_str = "" #After each complete j iterations, initialize output string again    
        
    
print(int(input("What is your age")))

#PROGRAM ANAGRAM
#Anagrams are words that are made up of the same letters but have different meanings
print("THIS PROGRAM COMPARES TWO LISTS TO CHECK FOR ANAGRAMS")
A = ["abode", "man", "live", "heart", "ear"]
B = ["adobe", "nan", "evil", "earth", "car"]
#declare an empty list
C = []
#Declare a count 'variable' and nitialize it to zero
count = 0
print()

for i in range(len(A)): #Iteratively select each element in List A
    for j in range(len(A[i])): #Iteratively select the letters in each element
        for k in range(len(B[i])): #Check for the letter in an element in B that has the same index as that of A
            if A[i][j] == B[i][k]:
                count = count + 1
                break
    C.append(count == len(B[i]))
    count = 0
print(C + '\n')


#PROGRAM PALINDROME - A Palindrome is a word that spells the same in the same direcion
'''Examples are level, racecar, saippuakivikauppias'''
print("THIS PROGRAM CHECKS IF A WORD IS A PALINDROME")
palindrome = input("Type a word: ")
iter_count = len(palindrome)//2 #Floor division
truth_list = []
neg = -1
for x in range(iter_count):
    #Comapre letters and append the boolean outcomes to the list
    truth_list.append(palindrome[x] == palindrome[neg])
    neg -= 1
print(truth_list)
if False in truth_list:
    print(("[0] is not a palindrome").format(palindrome))
else:
    print(("[0] is a palindrome").format(palindrome))

#PROGRAM SORT LIST
print("THIS FUNTION SORTS A LIST IN ASCENDING ORDER")
print()
sort_file = open('sorted.txt', 'w')

def _bubble_sort(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-1):
            if my_list[j+1] < my_list[j]:
                num = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = num
    sort_file.write(str(my_list))
    sort_file.close()
    sort_file = open('sorted.txt', 'r')
    sorted_list = sort_file.read()
    return sorted_list

my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
my_sorted_list = _bubble_sort(my_list)
print(my_sorted_list)

#PRINTING THE LONGEST PREFIX
strs = ["flower", "flow", "flight", "floor", "flood"]
#strs = ["dog", "racecar", "car"]

#BUBBLE SORT ALGORITHM
strs =  _bubble_sort(strs)
print(strs)

#CHCKING FOR PREFIXES
count = 0
pref = ""
for i in range(len(strs[0])):
    for j in range(len(strs)-1):
        letter = strs[j][i]
        if strs[j][i] == strs[j+1][i]:
            count += 1
        else:
            count -= 1
    if count == len(strs)-1:
        pref += letter
    count = 0

print("Longest Prefix is " + pref)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#Testing the function
print("PRINTING FACTORIAL")
print(factorial(6))
print()

#ITERATIVELY GENERATING FIBONACCI SERIES
print("FIRST 10 NUMBERS OF THE FIBONACCI SERIES")
fib_list = [0]
new_item = 1
if len(fib_list) < 2:
    fib_list.append(new_item)
    while len(fib_list) < 10:
        new_item = fib_list[-1] + fib_list[-2]
        fib_list.append(new_item)
print(fib_list)
print()

#FIBONACCI SERIES - THE RECURSIVE WAY
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#fib_series CODE
print('\nTHIS PROGRAM PRINTS FIBONNACY SERIES')
fib_series = []
user_input = int(input("Type a number: "))
for i in range(user_input):
    fib_series.append(fibonacci(i))
#LET'S PRINT STUFF
print("PRINTING FIBONACCI")
print(fib_series)        
print(fibonacci(4))
print()


#COMBINATION FUNCTION CALLING FACTORIAL FUNCTION
def combination(n, r):
    c_val = factorial(n)/(factorial(n-r)*factorial(r))
    int_val = int(c_val)
    return int_val


#PASCAL_T FUNCTIOIN CALLS COMBINATION FUNCTION
def pascal_T(n):
    my_str = ""
    for i in range(n+1):
        val = combination(n, i)
        my_str += str(val) + "     "
    return my_str

#This program prints Pascal Triangle
print("PRINTING PASCAL'S TRAINGLE")
user_input = int(input("Type a number: "))
for i in range(user_input+1):
    print(pascal_T(i).center(80))


#Pascal Triangle - Every list starts and ends with 1
print("ITERATIVELY GENERATING PASCAL'S TRIANGLE")
unit_num = 1
col_list = []
new_list = []
pascal_dict = {}
pascal_tri = ''
user_input = int(input("Type a number: "))
for i in range(1, user_input):
    col_list.append(unit_num)
    #Just using i to guage row lengths
    if len(col_list) == i:
        pascal_dict.update({i:col_list})
        col_list = []
    elif len(col_list)/2 == 1:
        col_list.append(unit_num)
        pascal_dict.update({i:col_list})
    else:
        col_list = []
        col_list.append(1)
        new_list = pascal_dict[i-1]
        for j in range(0, len(new_list)-1):
            col_list.append(new_list[j] + new_list[j+1])
        col_list.append(1)
        pascal_dict.update({i:col_list})
        col_list = []

print(pascal_dict)
print()
print("PASCAL'S TRANGLE")
for k in range(1, len(pascal_dict)+1):
    col_str = ' '.join([str(num) for num in pascal_dict[k]]).center(40)
    pascal_tri += col_str + "\n"
print(pascal_tri)

