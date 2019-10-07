name = "Vasu"
file_in = open("names.txt")
data = file_in.readlines()
for line in data:
    #print line
    cont = line.split(":")
    if cont[0].lower() == name.lower():
        print cont[1]
        break


