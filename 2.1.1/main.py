def count_down():
    global number
    for number in range(10, 1 , 1):
        print(number)
    return "Blast off"

print(count_down())