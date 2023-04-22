list_of_heights = input("Input a list of heights to be averaged...\n")

height_list = list_of_heights.split()

for n in range(0, len(height_list)):
    height_list[n] = int(height_list[n])
    
x=0
count=0
for height in height_list:
    x += height
    count += 1
print(round(x/count))