# provide the instructions for John to follow. The instructions are as follows:
instructions = "<<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<\
<><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><\
<>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>>\
<>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<>\
<><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><><\
><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<\
><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><<\
<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><>\
<><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><\
<>><<>><<>><"

#use a for loop to iterate through the floors he goes through.
floor = 0
for char in instructions:
    if char == "<":
        floor += 1
    elif char == ">":
        floor -= 1
#print out the current floor on the console.
print("John ended up on floor", floor)
