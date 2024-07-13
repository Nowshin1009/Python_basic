filename ="Hello.py"

with open(filename,mode="r+") as fp:
    #print(fp.read())
    content = fp.read()
    print(content)
    fp.wrte("\nx= 900")
    content = fp.read()
    print(content)

