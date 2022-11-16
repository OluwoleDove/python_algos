'''SOME ALGORITHMS I WROTE IN PYTHON '''

#THIS PROGRAM TAKES TWO INTEGER NUMBERS AND RETURNS A LIST OF ODD NUMBERS 
#AND A COUNT OF EVEN NUMBERS BETWEEN THE INTEGERS
def even_odd(i, j):
    try:
        if isinstance(i, int) == False and isinstance(j, int) == False:
            raise ValueError("Only Integer values please")
        else:
            if i > j:
                k = j
                j = i
                i = k
    except ValueError as e:
        print(e)
    
    print(("ITERATING BETWEEN {0} AND {1}").format(i, j))
    return_list = []
    odd_num_list = [] #An empty list
    even_num_count = 0 #integer value for even number counts initialized to zero

    for number in range(i, j):
        if number % 2 > 0: #number is an odd nuber
            odd_num_list.append(number)
        elif number % 2 == 0: #is number an even number, i.e is the remainder = 0?
            even_num_count += 1
    return_list.append(odd_num_list)
    return_list.append(even_num_count)
    return return_list

'''PROGRAM TO PRINT TRIANGLE OF CHARACTERS'''
def char_tri(char, lim):
    char = str(char)
    try:
        if char == "" or char == " ":
            raise ValueError("Your first input can't be empty")
        elif isinstance(int(lim), int) == False:
            raise ValueError("The limit should be an integer.")
    except ValueError as e:
        print(e)
    lim = int(lim)
    print("\nPRINTING A TRIANGLE OF CHARACTERS BY CALLING PRINT METHOD ONCE")
    str_out = ""
    main_str = ""

    for i in range(1,lim+1):
        str_out += char
        main_str += str_out + "\n"
    return main_str

def check_anagram(A, B):
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
    return C

#SORTING FUNCTION
def _bubble_sort(my_list):
    sort_file = open('sorted.txt', 'w')
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

#MULTIPLICATION TABLE
def multi_table(n):
    n = int(n)
    try:
        if isinstance(n, int) == False:
            raise ValueError("Integer value alone please")
    except ValueError as e:
        print(e)
   
    print("PRINTING MULTIPLICATION TABLE HORIZONTALLY")
    num = 0
    out_str = "" #Initializing output string
    #Below are 12 instances of i and 144 instances of j
   
    print("\nPRINTING TABLES VERTICALLY")
    for i in range(1, n+1):
        for j in range(1, n+1):
            num = i*j
            out_str += str(i) + " * " + str(j) + " = " + str(num) + "\n"
        print(out_str)
        out_str = "" #After eact complete j iterations, initialize output string again
        print()
    print('\nYou can also have it side by side\n')
    print("PRINTING 9 BY 12 MULTIPLICATION TABLE SIDE BY SIDE")

    for i in range(1, 13):
        for j in range(1, 10):
            num = j*i
            out_str += str(j) + "*" + str(i) + "=" + str(num) + "\t\t"
        print(out_str)
        out_str = "" #After each complete j iterations, initialize output string again 

def determine_palindrome(palindrome):
    iter_count = len(palindrome)//2 #Floor division
    truth_list = []
    neg = -1
    for x in range(iter_count):
        #Comapre letters and append the boolean outcomes to the list
        truth_list.append(palindrome[x] == palindrome[neg])
        neg -= 1
    print(truth_list)
    if False in truth_list:
        print(("{0} is not a palindrome").format(palindrome))
    else:
        print(("{0} is a palindrome").format(palindrome))

def find_prefix(_list):
    #sorting the List
    for i in range(len(_list)-1):
        for j in range(len(_list)-1):
            if len(_list[j+1]) < len(_list[j]):
                _word = _list[j]
                _list[j] = _list[j+1]
                _list[j+1] = _word
    print(_list)

    #CHCKING FOR PREFIXES
    count = 0
    pref = ""
    
    for i in range(len(_list[0])):
        for j in range(len(_list)-1):
            letter = _list[j][i]
            if _list[j][i] == _list[j+1][i]:
                count += 1
            else:
                count -= 1
        if count == len(_list)-1:
            pref += letter
        count = 0

    return pref
    
#FACTORIAL FUNCTION
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
#FIBONACCI SERIES - THE RECURSIVE WAY
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

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

#THIS FUNCTION CALLS OTHER FUNCTIONS
def test_algo():
    #EXECUTING EVEN_ODD FUNCTION
    print("THIS PROGRAM OUTPUTS THE ODD NUMBERS AND THE COUNT OF EVEN BETWEEN TWO INTEGERS")
    i = int(input("The first integer number please: "))
    j = int(input("Your second integer number: "))
    even_odd_list = even_odd(i, j)
    print(("The odd numbers are: \n{0} \nThe range contains {1} even numbers").format(even_odd_list[0], even_odd_list[1]))
    print()

    #CALLING FUNCTION TO PRINT TRIANGLE OF CHARACTERS
    print("LET'S HAVE A TRIANGLE OF CHARACTERS, SHALL WE?")
    i = input("Type a character please: ")
    j = input("Type an integer please: ")
    triangle = char_tri(i, j)
    print(triangle +'\n')

    #LET'S PRINT MULTIPLICATION TABLES
    print("\nLET'S GENERATE MULTIPLICATION TABLE")
    i = input("Enter an integer number: ")
    multi_table(abs(int(i)))

    #PROGRAM ANAGRAM
    #Anagrams are words that are made up of the same letters but have different meanings
    print("THIS PROGRAM COMPARES TWO LISTS TO CHECK FOR ANAGRAMS\n Examples:")
    A = ["abode", "man", "live", "heart", "ear"]
    B = ["adobe", "nan", "evil", "earth", "car"]
    print('A = ["abode", "man", "live", "heart", "ear"]\nB = ["adobe", "nan", "evil", "earth", "car"]\n')
    #declare an empty list
    anagram_check = check_anagram(A, B)
    print(anagram_check)
    print()

    #PRINTING THE LONGEST PREFIX
    word_list = ["flower", "flow", "flight", "floor", "flood"]
    print("\nChecking the longest prefix in the list")
    _prefix = find_prefix(word_list)
    print(("Longest Prefix is {0}").format(_prefix))

    #PRINTING FACTORIAL
    user_input = int(input("Type a number to print it's factorial: "))
    print("PRINTING FACTORIAL")
    print(factorial(user_input))
    print()

    #ITERATIVELY GENERATING FIBONACCI SERIES
    print("LET'S ITERATIVELY PRINT FIRST 10 NUMBERS OF THE FIBONACCI SERIES")
    fib_list = [0]
    new_item = 1
    if len(fib_list) < 2:
        fib_list.append(new_item)
        while len(fib_list) < 10:
            new_item = fib_list[-1] + fib_list[-2]
            fib_list.append(new_item)
    print(fib_list)
    print()

    #fib_series CODE
    print("\nNOW LET'S DO IT THE RECURSION WAY")
    fib_series = []
    user_input = int(input("Type a number: "))
    for i in range(user_input):
        fib_series.append(fibonacci(i))
    #LET'S PRINT STUFF
    print("PRINTING FIBONACCI")
    print(fib_series)     
    user_input = int(input("Type a number, let's get the Fibonacci value: "))   
    print(fibonacci(user_input))
    print()

    #PROGRAM PALINDROME - A Palindrome is a word that spells the same in the same direcion
    #Examples are level, racecar, saippuakivikauppias
    print("THIS PROGRAM CHECKS IF A WORD IS A PALINDROME")
    print("A Palindrome is a word that spells the same in both directions.\n")
    word_strng = input("Type a word: ")
    result = determine_palindrome(word_strng)


#PROGRAM SORT LIST
    print("THIS FUNCTION SORTS A LIST IN ASCENDING ORDER")
    print()

    my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    print(('Sorting this list\n {0}').format(my_list))
    my_sorted_list = _bubble_sort(my_list)
    print(my_sorted_list)

    #This program prints Pascal Triangle
    print("PRINTING PASCAL'S TRIANGLE")
    user_input = int(input("Type an integer number: "))
    for i in range(user_input):
        print(pascal_T(i).center(80))
    
    #Pascal Triangle - Every list starts and ends with 1
    print("NOW THAT WAS A FUNCTIONAL APPROACH TO IT.\nLET'S GENERATE PASCTAL'S TRIANGLE ITERATIVELY")
    unit_num = 1
    col_list = []
    new_list = []
    pascal_dict = {}
    pascal_tri = ''
    user_input = int(input("Type a number: "))
    for i in range(1, user_input+1):
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
        col_str = '  '.join([str(num) for num in pascal_dict[k]]).center(40)
        pascal_tri += col_str + "\n"
    print(pascal_tri)

check = input("Let's Start, shall we? Type 'Y' to start and 'N' to quit.\n")
while check == "Y" or check == "y":
    test_algo()
    check = input("Ha-ha! Super you. Wanna try again? Y/N\n")