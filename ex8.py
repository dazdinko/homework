def int_to_roman(num):
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_nums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    change_num = ''
    i = 0
    while num > 0:
        for _ in range(num // num[i]):
            change_num += roman_nums[i]
            num -= num[i]
        i += 1
    return change_num