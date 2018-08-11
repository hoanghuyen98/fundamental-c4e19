dicts = {
    "hc" : "Học, học hỏi, học tập",
    "ng" : "Người",
    "pt" : "Phát triển, Phú Thọ",
    "eny": "Em người yêu",
    "any": "Anh người yêu",
    "ns" : "Nói, nói chuyện",
    "ngta": "Người ta",
    "lm" : "Làm, lắm",
    "rk" : "Rồi",
    "stt" : "status" 
}
loop = True
while loop:
    for key in dicts.keys():
        print(key, end = "\t")
    print()

    input_dict = input(" ===>  Your code ? ")
    if input_dict in dicts:
        print("* "*20)
        print("Code: ", input_dict)
        print("Translation: ", dicts[input_dict])
        print("* "*20)
    else:
        print("No found! ")
        choose = input(" Do you want to contribute this word (Y/N): ").lower()
        if choose == "y":
            # new_key = input(" Bạn nhập key ? ")
            new_value = input(" Your translation: ")
            dicts[input_dict] = new_value
            print("Updated")  
        if choose == "N" or choose == "n":
            print("Tạm Biệt !! ")
            loop = False
        