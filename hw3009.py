#1
a = str(input("Наберите любое предложение: ", ))
print("Количество слов: ", len(a.split()))
#2
a = str(input("Наберите любое предложение: ", ))
b = a.split()
for j in b:
        s = str(j)
        f = s.replace(j, "😎")
print(f)