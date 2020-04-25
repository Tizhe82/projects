def func1(name):
    return f"Hello{name}"
    
def func2(name):
    return f"{name} , how you doin ?"


def func3(func4):
    return func4( "Dear learner")

print (func3(func1)) #function inside a function 
print(func3 (func2))