"""
WELCOME TO File Input and Output EXAMPLES

BEFORE YOU DO ANY CODING COPY THE BELOW TEXT INTO THE .replit FILE

language = "python3"
run = "cd 'Lesson 3 - Lists, IO, Random'; cd examples; python3 file_io_examples.py"

"""
# this is where the file is located
file_path1 = "../text_files/hello1.txt"

# r means you want to read the file
f = open(file_path1, "r")
contents1 = f.read()
print(contents1)
f.close()

contents2 = "Hello to this new file\n"
file_path2 = "../text_files/hello2.txt"
f = open(file_path2, "w")
f.write(contents2)
f.close()

