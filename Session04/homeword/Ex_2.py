numb = int(input("Enter your balance : ")) 
int_to_str = str(numb) # chuyển từ int sang str
str_to_list = list(int_to_str) # chuyển tử str sang list
reversed_list = str_to_list.reverse() # đảo list 
new_list = []
for i in range(len(str_to_list)):
    if i % 3 == 0 :
        new_list += ","
    new_list += str_to_list[i]
new_list.reverse()
del new_list[len(new_list)-1]
print(' \t \t ===> Your updated balance: $', ''.join(new_list))

# có thể dùng format print ra luôn :3. Thay thế 11 dòng dài loằng ngoằng ở trên
# Nhưng mà em chẳng hiểu vì sao format nó làm đc như vậy :(( 
# print(" Your updated balance : ${:0,d}".format(numb))






# print(name)

# print(new)
# print(" Your updated balance : ${}".format(bal))
    
# print(check_firt)