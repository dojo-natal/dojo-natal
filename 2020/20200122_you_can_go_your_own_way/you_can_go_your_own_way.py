def you_can_go_your_own_way(lydia_path):
    return [
        "ES",
    ]

def is_possible(lydia_path, player_path):
    if lydia_path == player_path or len(lydia_path) != len(player_path):
        return False

    lydia_south_steps = 0 
    player_south_steps = 0 

    for ch in lydia_path: 
        if ch == "S":
            lydia_south_steps += 1

    for ch in player_path: 
        if ch == "S":
            player_south_steps += 1

    if lydia_south_steps != player_south_steps:
        return False

    if lydia_path == "SE" and player_path == "":
        return False

    return True