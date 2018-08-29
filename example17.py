from sys import argv
from os.path import exists

script, from_file, to_file = argv,"ex_17.txt","ex_17_new.txt"

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open("ex_17.txt")
indata = in_file.read()
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open("ex_17_new.txt", 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()