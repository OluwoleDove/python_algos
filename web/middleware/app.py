from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5000")


# THIS PROGRAM TAKES TWO INTEGER NUMBERS AND RETURNS A LIST OF ODD NUMBERS 
# AND A COUNT OF EVEN NUMBERS BETWEEN THE INTEGERS
def even_odd(i, j):
    try:
        if not isinstance(i, int) or not isinstance(j, int):
            raise ValueError("Only Integer values please")
        else:
            if i > j:
                k = j
                j = i
                i = k
    except ValueError as e:
        return str(e)
    
    return_list = []
    odd_num_list = []
    even_num_count = 0

    for number in range(i, j+1):
        if number % 2 == 1: # number is an odd number
            odd_num_list.append(number)
        elif number % 2 == 0: # number is an even number
            even_num_count += 1
    return_list.append(odd_num_list)
    return_list.append(even_num_count)
    return return_list

def multi_five(n):
    if n == 0:
        return 0
    else:
        if n % 5 == 0:
            return n + multi_five(n-5)
        else:
            return multi_five(n-1)

def char_tri(char, lim):
    char = str(char)
    try:
        if char == "" or char == " ":
            raise ValueError("Your first input can't be empty")
        elif not isinstance(int(lim), int):
            raise ValueError("The limit should be an integer.")
    except ValueError as e:
        return str(e)
    
    lim = int(lim)
    str_out = ""
    main_str = ""

    for i in range(1, lim+1):
        str_out += char
        main_str += str_out + "\n"
    return main_str

def check_anagram(A, B):
    C = []
    count = 0

    for i in range(len(A)):
        for j in range(len(A[i])):
            for k in range(len(B[i])):
                if A[i][j] == B[i][k]:
                    count += 1
                    break
        C.append(count == len(B[i]))
        count = 0
    return C

def _bubble_sort(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-1):
            if my_list[j+1] < my_list[j]:
                num = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = num
    return my_list

def multi_table(n):
    n = int(n)
    try:
        if not isinstance(n, int):
            raise ValueError("Integer value alone please")
    except ValueError as e:
        return str(e)
   
    out_str = ""

    for i in range(1, n+1):
        for j in range(1, n+1):
            num = i * j
            out_str += str(i) + " * " + str(j) + " = " + str(num) + "\n"
    return out_str

def determine_palindrome(palindrome):
    iter_count = len(palindrome) // 2
    truth_list = []
    neg = -1
    for x in range(iter_count):
        truth_list.append(palindrome[x] == palindrome[neg])
        neg -= 1
    if False in truth_list:
        return f"{palindrome} is not a palindrome"
    else:
        return f"{palindrome} is a palindrome"

def find_prefix(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-1):
            if len(my_list[j]) > len(my_list[j+1]):
                this_string = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = this_string

    prefix_str = ""
    count = 1
    for i in range(len(my_list[0])):
        letter = ""
        for j in range(len(my_list)-1):
            letter = my_list[j][i]
            if my_list[j][i] == my_list[j+1][i]:
                count += 1
            else:
                count -= 1

        if count == len(my_list):
            prefix_str += letter
        else:
            break
        count = 1

    return prefix_str

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def combination(n, r):
    c_val = factorial(n) // (factorial(n-r) * factorial(r))
    return int(c_val)

def pascal_T(n):
    my_str = ""
    for i in range(n+1):
        val = combination(n, i)
        my_str += str(val) + "     "
    return my_str

def pascalT_iter():
    unit_num = 1
    col_list = []
    new_list = []
    pascal_dict = {}
    pascal_tri = ''
    user_input = int(input("Type a number: "))
    for i in range(1, user_input+1):
        col_list.append(unit_num)
        if len(col_list) == i:
            pascal_dict.update({i: col_list})
            col_list = []
        elif len(col_list) / 2 == 1:
            col_list.append(unit_num)
            pascal_dict.update({i: col_list})
        else:
            col_list = []
            col_list.append(1)
            new_list = pascal_dict[i-1]
            for j in range(0, len(new_list)-1):
                col_list.append(new_list[j] + new_list[j+1])
            col_list.append(1)
            pascal_dict.update({i: col_list})
            col_list = []

    for k in range(1, len(pascal_dict)+1):
        col_str = '  '.join([str(num) for num in pascal_dict[k]]).center(40)
        pascal_tri += col_str + "\n"

    return pascal_tri

def find_sub_sequence(main_seq, sub_seq):
    main_seq = main_seq.split(',')
    sub_seq = sub_seq.split(',')
    i = 0
    j = 0
    while i < len(sub_seq) and j < len(main_seq):
        if sub_seq[i] == main_seq[j]:
            i += 1
        j += 1

    return i == len(sub_seq)

# Endpoints for each function
@app.route('/even_odd', methods=['POST'])
def even_odd_endpoint():
    data = request.get_json()
    i = int(data['i'])
    j = int(data['j'])
    result = even_odd(i, j)
    return jsonify(result)

@app.route('/multi_five', methods=['POST'])
def multi_five_endpoint():
    data = request.get_json()
    n = int(data['n'])
    result = multi_five(n)
    return jsonify(result)

@app.route('/char_tri', methods=['POST'])
def char_tri_endpoint():
    data = request.get_json()
    char = data['char']
    lim = int(data['lim'])
    result = char_tri(char, lim)
    return jsonify(result)

@app.route('/check_anagram', methods=['POST'])
def check_anagram_endpoint():
    data = request.get_json()
    A = data['A']
    B = data['B']
    result = check_anagram(A, B)
    return jsonify(result)

@app.route('/_bubble_sort', methods=['POST'])
def bubble_sort_endpoint():
    data = request.get_json()
    my_list = data['my_list']
    result = _bubble_sort(my_list)
    return jsonify(result)

@app.route('/multi_table', methods=['POST'])
def multi_table_endpoint():
    data = request.get_json()
    n = int(data['n'])
    result = multi_table(n)
    return jsonify(result)

@app.route('/determine_palindrome', methods=['POST'])
def determine_palindrome_endpoint():
    data = request.get_json()
    palindrome = data['palindrome']
    result = determine_palindrome(palindrome)
    return jsonify(result)

@app.route('/find_prefix', methods=['POST'])
def find_prefix_endpoint():
    data = request.get_json()
    my_list = data['my_list']
    result = find_prefix(my_list)
    return jsonify(result)

@app.route('/factorial', methods=['POST'])
def factorial_endpoint():
    data = request.get_json()
    n = int(data['n'])
    result = factorial(n)
    return jsonify(result)

@app.route('/fibonacci', methods=['POST'])
def fibonacci_endpoint():
    data = request.get_json()
    n = int(data['n'])
    result = fibonacci(n)
    return jsonify(result)

@app.route('/combination', methods=['POST'])
def combination_endpoint():
    data = request.get_json()
    n = int(data['n'])
    r = int(data['r'])
    result = combination(n, r)
    return jsonify(result)

@app.route('/pascal_T', methods=['POST'])
def pascal_T_endpoint():
    data = request.get_json()
    n = int(data['n'])
    result = pascal_T(n)
    return jsonify(result)

@app.route('/pascalT_iter', methods=['POST'])
def pascalT_iter_endpoint():
    result = pascalT_iter()
    return jsonify(result)

@app.route('/find_sub_sequence', methods=['POST'])
def find_sub_sequence_endpoint():
    data = request.get_json()
    mainSeq = data['mainSeq']
    subSeq = data['subSeq']
    result = find_sub_sequence(mainSeq, subSeq)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
