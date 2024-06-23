def func():
    name = input("Enter Your Name :")
    age = input("Enter Your Age :")
    print(f"Name : {name} Age : {age}")

def read_file(filename):
    with open(filename,"r") as file:
        content = file.read()
        print(content)

def write_file(filename,output):
    with open(filename,"a") as file:
        file.write(output)
        # content = file.read()
        # print("Content is " + content)

read_file("sample.txt")
# write_file("sample.txt"," This is my world of coding.")
# func()