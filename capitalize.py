# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
import re
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

n = input()
cp_word = solve(n)
print(cp_word)