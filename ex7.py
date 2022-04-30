def calc_formula(d):
    c = 50
    h = 30
    result = ((1.0)*(2 * c * d)/h)**(0.5)
    return str(int(result))

input_nums = input("Give me a few numbers:")
result = []
for num in input_nums.split(','):
    int_num = int(num)
    temp = calc_formula(int_num)
    result.append(temp)

print(','.join(result))