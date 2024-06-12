with open('myfile2.txt','r') as fp:
    content = fp.read()
    print(content)

with open('myfile2.txt','r') as fp:
    content = fp.readlines()
    print(content)