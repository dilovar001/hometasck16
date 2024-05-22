my_list=["Soft club", "C++", "Python","Django"]
with open("fille.txt","w") as file:
    for i in my_list:
        file.write(i +"\n")
    print("operation successfully")
        