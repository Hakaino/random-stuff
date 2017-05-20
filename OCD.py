# -*- coding: utf-8 -*-
import os

# renames all the files of a serie in a folder instantaniously
confirmation = parent = ""
a = "\'"

while confirmation != "s":
    location = raw_input("Origem: ")
    newName = raw_input("Mudar nome para: ")
    confirmation = raw_input("Escreve 's' para confirmar: ")
    print ("--------------------------------------")

division = location.split("/")
for word in range(len(division) - 1):
    parent += division[word] + "/"
folder = os.popen("ls " + a + location + a).read().split("\n")

#set a minimal name for the files based on the folder name
if newName == "":
    if len(division) > 1:
        Name = location.split(parent)[1]
    else:
        Name = location
else:
    Name = newName
if len(Name) > 15:
    name = ""
    for word in Name.split(" "):
        name += word[0]
else:
    name = Name
print ("nome dos episódios:", name)

#order file names by number
pointer = []
for item in folder:
    number = "0"
    for character in item:
        try:
            if character in "0123456789":
                number += character
        except ValueError:
            pass
    pointer.append([int(number), item])
    pointer.sort()

#change file names based on the number and name inside the folder
for item in range(1, len(pointer)):
    object1 = a + location + "/" + pointer[item][1] + a
    part = len(pointer[item][1].split(".")) - 1
    kind = "." + pointer[item][1].split(".")[part]
    object2 = a + location + "/" + name + " " + str(item) + kind + a
    os.popen("mv " + object1 + " " + object2)

#change the name of the folder
if newName != "":
    origin = a + location + a
    destiny = a + parent + "/" + newName + a
    print ((os.popen("mv " + origin + " " + destiny)))
