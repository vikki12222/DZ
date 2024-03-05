f = open("pb.csv", "r")
# назвала его как pb.csv
num_of_phones = int(f.readline())
pb = {}
for i in range(num_of_phones):
    data = f.readline().split()
    name = data[0]
    phone_number = data[1]
    pb[name] = phone_number
f.close()
user_n = input("имя: ")
if user_n in pb:
    print("Номер телефона:", pb[user_n])
else:
    print("Нету")