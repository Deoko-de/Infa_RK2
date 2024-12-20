a = "101101"
b = "110011"

a_int = int(a, 2)
b_int = int(b, 2)

and_res = bin(a_int & b_int)[2:]
sum_res = bin(a_int + b_int)[2:]

print(f"AND ({a}, {b}): {and_res}")
print(f"Сумма ({a}, {b}): {sum_res}")
