print("AWS Re-Start: Lab-10")
print("Inicia proceso")


file1 = open("lsinsulin-seq-clean.txt",'r')
data = file1.read()
number_of_characters = len(data)
print("Caracteres en lsinsulin-seq-clean.txt ::: " + str(number_of_characters) + " de 24")


file2 = open("binsulin-seq-clean.txt",'r')
data = file2.read()
number_of_characters = len(data)
print("Caracteres en binsulin-seq-clean.txt ::: " + str(number_of_characters) + " de 30")

file3 = open("cinsulin-seq-clean.txt",'r')
data = file3.read()
number_of_characters = len(data)
print("Caracteres en cinsulin-seq-clean.txt ::: " + str(number_of_characters) + " de 35")

file4 = open("ainsulin-seq-clean.txt",'r')
data = file4.read()
number_of_characters = len(data)
print("Caracteres en ainsulin-seq-clean.txt ::: " + str(number_of_characters) + " de 21")