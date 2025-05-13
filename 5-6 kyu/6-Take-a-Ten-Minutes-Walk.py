# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
# The city provides its citizens with a Walk Generating App on their phones -- 
# everytime you press the button it sends you an array of one-letter strings 
# representing directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block for each letter (direction) 
# and you know it takes you one minute to traverse one city block, 

# so create a function that will return true 
# if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) 
# and will, of course, return you to your starting point. 
# Return false otherwise.

# ==========================================================

# Note. Steps in different directions:
# 'n' = [0, 1]  
# 's' = [0, -1] 
# 'w' = [-1, 0] 
# 'e' = [1, 0] 

# ==========================
# 1) One solution
# ==========================

def is_valid_walk(walk):
    walk_time = len(walk)
    x_coordinate, y_coordinate = 0, 0
    
    if walk_time != 10:
        return False

    for w in walk:
        if w == "n":
            y_coordinate += 1
        elif w == "s":
            y_coordinate -= 1
        elif w == "w":
            x_coordinate -= 1
        else:
            x_coordinate += 1
    
    return x_coordinate == 0 and y_coordinate == 0


# ==========================
# 2) And another one
# ==========================

def isValidWalk(walk):
	walk_time = len(walk)
	if walk_time != 10:
		return False
	return walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')


