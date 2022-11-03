# square_nums = list(map (int,(lambda x: x ** 2 for x in range(0,21))))


numbers = [i for i in range(1,21)]
squares = list(map(lambda x:x*x,numbers))
print(squares)