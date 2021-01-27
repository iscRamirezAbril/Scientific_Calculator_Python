# This is the library that will help with text color.
from colorama import init, Fore
init(autoreset=True)

print(Fore.CYAN + "=============================================================================================")
print(Fore.CYAN + "------------------------- Welcome to the Scientific Calculator! :D --------------------------")
print(Fore.CYAN + "=============================================================================================")

# Principal Menu
print("This is the principal menu.")
print("a. Basic Math Functions")
print("b. More Math Functions")
print("c. Trigonometric Functions")