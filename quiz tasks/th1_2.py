five_digit_number = int(input())
a = five_digit_number - five_digit_number%1000 - int(five_digit_number/10000)*10000
b = five_digit_number%100 - five_digit_number%10
print (five_digit_number+a+b)