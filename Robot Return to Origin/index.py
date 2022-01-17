def judgeCircle(moves):
    x = y = 0
    for direction in moves:
        if direction == 'U':
            y+=1
        elif direction == 'D':
            y-=1
        elif direction == 'L':
            x-=1
        elif direction == 'R':
            x+=1
    if x == 0 and y == 0:
        return True
    return False

moves = "LL"
print(judgeCircle(moves))
