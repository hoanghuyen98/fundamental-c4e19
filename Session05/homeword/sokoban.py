print(" P is player ===== ", end = "\t")
print(" B is boxes ===== ", end = "\t")
print(" D is destination =====", end = "\t")
print(" # is obstacle or wall ")

# set player position
# rep : ☻
player = {
    'x' : 1,
    'y' : 0
}
player_copy = player.copy()
old_player = player_copy.copy()

# set boxes position 
# rep : ♥
boxes = [
    {'x': 1, 'y': 3},
    {'x': 2, 'y': 4},
    {'x': 3, 'y':3}
]
boxes_copy = [box.copy() for box in boxes ]

# set detination position 
# rep: ✉
des = [
    {'x': 4, 'y': 5},
    {'x': 4, 'y': 4},
    {'x': 4, 'y': 3}
]

#set obstacle position
# rep : ✖
obs = [
    {'x': 2, 'y': 0},
    {'x': 3, 'y': 1},
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 4}
]

# set map_size
size_map = {
    'x': 6,
    'y': 7
}

#saved

saved_player = player.copy()
saved_boxes = [box.copy() for box in boxes]

def reset_game(saved_player, save_boxes):
    global player,boxes
    player = saved_player.copy()
    boxes = [box.copy() for box in saved_boxes]

def check_is_here(x, y, items):
    for item in items:
        if x == item['x'] and y == item['y']:
            return item
    return None

def check_box(box_x, box_y, boxes, dx, dy):
    rest_box = ( box for box in boxes if box['x'] != box_x or box['y'] != box_y)
    return check_box(box_x + dx, box_y + dy, rest_box)

def check_obs(obs_x, bos_y, obs, dx, dy):
    rest_obs = ( ob for ob in obs if ob['x'] != obs_x or ob['y'] != obs_y)
    return check_box(obs_x + dx, obs_y + dy, rest_obs)

def print_map(size_map, player, boxes):
    for y in range(size_map['y']):
        for x in range(size_map['x']):
            if x == player['x'] and y == player['y']:
                print(" ☻ ", end = "")
            elif check_is_here(x, y, boxes):
                print(" ♥ ", end = "")
            elif check_is_here(x, y, des):
                print(" ✉  ", end = "")
            elif check_is_here(x, y, obs):
                print(" ✖ ", end = "")
            else:
                print(" - ", end = "")
        print()

def is_in_map(x, y, size_map):
    return 0 <= x < size_map['x'] and 0 <= y < size_map['y']

def check_win(boxes, des):
    count = 0
    for box in boxes:
        if check_is_here(box['x'], box['y'], des) is not None:
            count += 1
    if count == len(boxes):
        return True
    else:
        return False 


def input_direction(direction):
    dx = 0 
    dy = 0 
    if direction == 'W':
        dy -= 1
    elif direction == 'S':
        dy += 1
    elif direction == 'D':
        dx += 1
    elif direction == 'A':
        dx -= 1
    else:
        print(" !!!!! Error !!!!! ")
        print(" You enter wrong button . Please do this again, Buzzzz :v ")
    return dx, dy


def move(item, dx, dy):
    item['x'] += dx
    item['y'] += dy
    return item

#main
while True:
    print_map(size_map, player, boxes)

    if check_win(boxes, des):
        print("*****************************")
        print(" ********** You WIN ********* ")
        print("******** Cảm ơn Sếp đã check bài cho em :3 *********")
        print("*********** Good Lucky *************")
        print("********************************")
        break
   
    direction = input("==> What is your move? (W/A/S/D) (Enter R to reset the Game) : ").upper()
    if direction == "R":
        reset_game(saved_player,saved_boxes)

    dx, dy = input_direction(direction)
   
    found_box = check_is_here(player['x'] + dx, player['y'] + dy, boxes)
    found_obs = check_is_here(player['x'] + dx, player['y'] + dy, obs)

    if found_box is not None:
        if check_is_here(found_box['x'] + dx, found_box['y'] + dy, boxes) is None:
            if is_in_map(found_box['x'] + dx, found_box['y'] + dy, size_map):
                found_box = move(found_box, dx, dy)
                player = move(player, dx, dy) 
    elif found_obs is not None:
        if check_is_here(found_obs['x'] + dx, found_obs['y'] + dy, obs) is not None:
                found_obs = move(found_obs, dx, dy)
                player = move(player, dx, dy)

    elif is_in_map(player['x'] + dx, player['y'] + dy, size_map):
        player = move(player, dx, dy)

    

   
   

    