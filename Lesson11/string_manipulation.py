with open('example.txt', 'r') as file:
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)

with open('example.txt', 'r') as file:
    for line in file:
        words = line.strip().split()
        print(words)

name = "Drin"
age = 17

with open('output.txt', 'w') as file:
    file.write("Name: "+name + "\n")
    file.write("Age: "+str(age) + "\n")

with open('output.txt', 'w') as file:
    file.write(f"Name:  {Name}\n")
    file.write(f"Age:  {Age}\n")

with open('output.txt', 'w') as infile, open('output.txt', 'w') as outline:
    for line in inline:
        cleaned_line = line.strip()
        modified_line = cleaned_line.replace("Line 1", "Line x")
        outfile.write = (modified_line + "\n")
