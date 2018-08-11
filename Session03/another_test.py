# # list / array
# menu = ["kem", "xoi", "pho", "thit", "tao pho"]
# # separator : phân cách với nhau = dấu j đó ta dùng sep = " "
# print(*menu, sep=" , " ) # dâu * để lấy ra hết tất cả các phần tử
# print(len(menu)) # lấy chiều dài của chuỗi
# menu.append("Chè") # thêm 1 phần tử
# print(*menu, sep = ", ") 
# # print(len(menu))
# print("Hi there, here your favorite thing so far")
# favs = ["death note", "nnetflix", "teaching"]
# print(*favs, sep=", ")
# # new_food = input("Name one thing you want to add? coding: ")
# # favs.append(new_food)
# # print(*favs, sep = ", ")
# để lấy ra phần tử tại vị trí nào đó
# item = menu[:3]
# for i in range(len(menu)):
#     print(menu[i])
# for index, item in enumerate(menu):
#     print(index, item)
# for item in menu:
#     print(item)
# sửa thông tin trong list
# menu[1] = "Khoai tay"
# print(*menu, sep = ", ")

favs = ["read book", "play game", "coding"]
print(*favs, sep = ", ")
# print("*" * 40 )
# for index, item in enumerate(favs):
#     print(index+1, item, sep = ". ")
# print("*" * 40)
# new_index = int(input("Position you want to update? "))
# new_favs = input("Your replacing favorite? ")
# favs[new_index - 1]  = new_favs
# for index, item in enumerate(favs):
#     print(index+1, item, sep = ". ")
# del favs[1]
# favs.pop(1)
favs.remove(menu[1])
print(*favs, sep =", ")