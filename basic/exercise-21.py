students = []
with open("notlar.txt") as file:
    fileLines = file.readlines()[1:]
    for line in fileLines:
        spac = line.replace("\n","").split(" ")
        student = []
        student.append(spac[0].replace("-"," "))
        student.append(' '.join([str(elem) for elem in spac[1:len(spac)-1]]))

        notlar = spac[-1].split("/")
        final  = int(notlar[2])
        ortala = round(int(notlar[0]) * 0.3 + int(notlar[1]) * 0.3 + final * 0.4, 1)
        student.append(ortala)
        student.append(final)

        if(ortala >= 70 and final >= 70):
            student.append("GEÇTİ")
        else:
            student.append("KALDI")
        
        students.append(student)
        
with open("sonuclar.txt","w") as sonuclar:
    for line in students:
        sonuclar.write(line[0])
        sonuclar.write(" " * (25 - len(line[0])))
        sonuclar.write(line[1])
        sonuclar.write(" " * (25 - len(line[1])))
        sonuclar.write(str(line[2]))
        sonuclar.write(" " * (15 - len(str(line[2]))))
        sonuclar.write(str(line[3]))
        sonuclar.write(" " * (15 - len(str(line[3]))))
        sonuclar.write(str(line[4]))        
        sonuclar.write("\n")
