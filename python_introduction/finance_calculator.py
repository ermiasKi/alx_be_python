inc = int(input("Enter your monthly income:"))
ex = int(input("Enter your total monthly expenses:"))
save = inc - ex

print(f"Your monthly savings are: {inc - ex}")
print(f"Projected savings after one year, with interest, is: {save * 12 + (save * 12 * 0.05)}")