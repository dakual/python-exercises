class Personel:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def show(self):
        print(self.name, self.surname, self.age)

per = Personel("daghan kurtay", "altunsoy", 37)
per.show()


a = {"isim":"daghan","soyad":"altunsoy","yas":35}
for k,v in a.items():
    print(k,v)
