#!/usr/bin/python3
Square = __import__('6-square').Square


my_square_1 = Square(3)
print(f"Position: {my_square_1.position}")
print(f"PositionX: {my_square_1.position[0]}")
my_square_1.my_print()

print("--")

my_square_2 = Square(4, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
print(f"Position: {my_square_3.position}")
print(f"PositionX: {my_square_3.position[0]}")
my_square_3.position = [4, 3]
print(f"Position: {my_square_3.position}")
print(f"PositionX: {my_square_3.position[0]}")
my_square_3.my_print()

print("--")
