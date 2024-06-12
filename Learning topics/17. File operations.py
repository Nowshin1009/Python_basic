# Write in a file
fp = open ('myfile.txt', 'w')

fp.write("this is a text file\n")

fp.close()



fp = open ('myfile2.txt', 'w')

lines = ['Apple\n', 'Banana\n','Orange']
fp.writelines(lines)

fp.close()


# Read a file

fp = open ('myfile2.txt', 'r')

content= fp.read()
print(content)

fp.close()