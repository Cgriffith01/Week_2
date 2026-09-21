birds = ["robin","wren","humming bird","crow"]
print(birds)

new_bird= input("What is another bird that can be added to this list?: ")

birds.append(new_bird)
print(birds)

birds.sort()

for bird in birds:
    print(bird)

popped_bird = birds.pop(1)
print(f"The {popped_bird} has been removed.")

print(birds)

del birds[-1]
print("The last bird on the list has been removed.")
print(birds)