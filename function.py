def show(name="admin", age='0'):
    """
        this is a simple function that print name and age
        age should be str because we can not concatenate
        str and int yet!!!!
    """
    print("Hello " + name + " and you are " + age + " years old")


show("pourya", "22")
show()
