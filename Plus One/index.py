def plusOne(digits: list):
    result_digit = []
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        sum = digits[i]+carry
        carry = sum//10
        sum = sum%10
        result_digit.append(sum)
    if carry == 1:
        result_digit.append(1)
    return list(reversed(result_digit))

digits = [1,2,3]
digits = [4,3,2,1]
digits = [9]
print(plusOne(digits))
