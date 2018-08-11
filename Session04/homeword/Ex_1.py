name = input("You full name : \n \t \t =====> ").lower()
upper_name = name.title()
list_name = list(upper_name)
# Xóa khoảng trắng thừa
for i in range(len(list_name)):
    for j in range(len(list_name)):
        if list_name[j] == ' ' and list_name[j+1] == ' ':
            del list_name[j+1]
            break
print("\t \t Updated : ", end="")
print(''.join(list_name))
# có thể dùng split() để xóa khoảng trắng thừa , thay cho vòng lặp ở trên
# upper_char = name.title()
# print(*upper_char.split())

 