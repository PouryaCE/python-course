a = 12.5
print(round(a))
b = 12.4
print(round(b))
c = 12.6
print(round(c))
################################
# string is a set of chars those between
# single qoutes or double qoutes

name = "pourya"
family = "janparvar"


fullname = name + " " + family
print(fullname)
print(name+" "+family) # without saving
print(name ,family)     # without + operator
print("pourya" " janparvar")




age = 20
# f = name + age  we got error
f = name + "20"  # it is ok



# long string
situation = "hello my name is pourya"\
            "and i am 22 years old"\
            "what is your name"
            
print(situation)


situation2 = ("hello my name is pourya"
              "and i am 22 years old"
              "what is your name")
print(situation2)


print("what's your name")
# print('what's your name') error
print('what\'s your name') # skaping
print(r'what\s your name') # raw

#_______________________________________
message = "hello from python."
print(len(message))
#_______________________________________
q = "my name is pourya"
x = q[0]
print(x)
x = q[2:8]
print(x)
x = q[2:]
print(x)
x = q[:5]
print(x)
x = q[:]
print(x)
x = q[::3]
print(x)
# start => default=0
# stop  => default=last
# step  => defaul=1






