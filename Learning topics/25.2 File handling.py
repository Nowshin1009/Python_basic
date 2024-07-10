filename = "14. Range.py"
try:
    fp=open(filename,"rt")
    content = fp.read()
    print(content)

    fp.close()
except FileNotFoundError:
    print("Check if the filename is correct, or if the file exists")