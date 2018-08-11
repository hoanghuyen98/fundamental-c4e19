# from random import randint
print(" Sang trái  : a  --------- ", end = "")
print(" Sang phải  : d  ")
print(" Lên trên   : w  --------- ", end = "")
print(" Xuống dưới : s ")
print("P là Payer ")
print("B là Boxes")
print("D là Destinations")

map = {
    "size_x": 5,
    "size_y": 5
}

player = { 
    "x": 3, 
    "y": 4 
}

boxes = [
    { "x": 1, "y": 1},
    { "x": 2, "y": 2},
    { "x": 3, "y": 3}
]
destinations = [
    { "x": 2, "y": 1},
    { "x": 3, "y": 2},
    { "x": 4, "y": 3}
]
playing = True
while playing:
    for y in range(map['size_y']) :
        for x in range(map['size_x']):

            player_is_here = False
            if x == player['x'] and y == player['y']:
                player_is_here = True

            box_is_here = False
            for box in boxes:
                if box['x'] == x and box['y'] == y and player_is_here is not True :
                    box_is_here = True
                    break
            
            destinations_is_here = False
            for des in destinations:
                if des['x'] == x and des['y'] == y and player_is_here is not True :
                    destinations_is_here = True
                    break

            if player_is_here :
                print(" P ", end = "")
            elif box_is_here :
                print(" B ", end = "")
            elif destinations_is_here :
                print(" D ", end = "")
            else:
                print(" - ", end = "")      
        print()

    move = input(" Your move: ").upper()

    dx = 0
    dy = 0

    if move == "W":
        dy -= 1 

    elif move == "S":
        dy += 1

    elif move == "A":
        dx -= 1
        
    elif move == "D":
        dx += 1
      
    else:
        print("Buzzzz")
        playing = False

    check_box = True
    if 0 <= player['x'] + dx < map['size_x'] and 0 <= player['y'] + dy < map['size_y']:
        player['x'] += dx
        player['y'] += dy

    for box in boxes:
        if 0 <= box['x'] + dx < map['size_x'] and 0 <= box['y'] + dy < map['size_y']:  
                 
            if box['x'] == player['x'] and box['y'] == player['y']:                                                                                 
                box['x'] += dx
                box['y'] += dy
                check_box = False
                break
                
    win = True
    for box in boxes:
        if box not in destinations:
            win = False
    if win:
        print(" ****** * * * *  Your Win !!!!!! ** ** * * * *")
        break                
                

                        
           


                    
            
            
                