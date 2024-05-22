with open("file.txt", "r") as file:
    my_list = file.read().split()
maxx = my_list[0]  
for i in my_list:
    if len(i) > len(maxx): 
        maxx = i  

print(maxx)