import os



class Program:
    
    def createFile():
        name = input("Name of the File ")
        file = open(name,"w+")
        print("1 = Java code")
        print("2 = Html code")
        choise = int(input("Input your choise number "))
        Java = f"public class {name}"+{}
        Html = "<Html><Head></Head><title></title><body></body></Html>"
        if choise == 1:
            file.write(Java)
        elif choise == 2:
            file.write(Html)
        else:
            print("Invalid Number")
        
        file.close()
    def exsyscom():
        command = input("Any Command ")
        os.system(command)
    while True:
        choise = int(input("Enter a choise number "))
        if choise == 1:
            createFile()
        elif choise == 2:
            exsyscom()
