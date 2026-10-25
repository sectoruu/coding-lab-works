big_decimal_code = 65
small_decimal_code = 97
order_num = 0
while big_decimal_code <= 90:
    print(f"{order_num:02}    {chr(big_decimal_code)}    {big_decimal_code:03}    {big_decimal_code:#03X}")
    big_decimal_code += 1
    order_num += 1

while small_decimal_code <= 122:
    print(f"{order_num:02}    {chr(small_decimal_code)}    {small_decimal_code:03}    {small_decimal_code:#03X}")
    small_decimal_code += 1
    order_num += 1
