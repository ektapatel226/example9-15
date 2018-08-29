from sys import argv

script, filename = argv, "ex15_sample.py"
txt = open("ex15_sample.txt")

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
