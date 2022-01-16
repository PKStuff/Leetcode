def boatsToSavePeople(peoples, limit):
    peoples = sorted(peoples)
    left = 0
    right = len(peoples)-1
    no_of_boats = 0
    while left <= right:
        if left==right:
            no_of_boats+=1
            break
        elif (peoples[left]+peoples[right]<=limit):
            left+=1
            right-=1
            no_of_boats+=1
        else:
            right-=1
            no_of_boats+=1
    return no_of_boats

peoples = [3, 3, 3, 2]
limit = 3
print(boatsToSavePeople(peoples, limit))