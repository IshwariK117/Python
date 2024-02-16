'''
-try:test the code
-except:lets you handle the error
-else:executed when there is no error
-finally:always executed ,regardless of try-except block
'''

try:
    print(x)  # x is not defined
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
