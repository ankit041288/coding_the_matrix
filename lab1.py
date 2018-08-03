

print(7*24*60)
print(2304811 %47)

print(type  (5!=4))

# <Expression> if<Condition> else <>
# python evaluates condition and if its >0
print(1 if 1>0 else 2)

S={1,2,4}
print(6 in S)
T = S
T= {x**2 for x in T}
print(T)

#Lists

L =[1,10,20,30,40,50,60]
print(L[2:])

print(L[:2])

print(L[::2])

print(L[2::2])

[a,b,c]=[1,2,3]
print( a)

# Tuple
(1,2,3)

# Scaling Vectors
v =[2,3]


# class Vec
class Vec:
    def __init__(self,lables, functions):
        self.D=lables
        self.f = functions

v=Vec({'a','b','c'},{'a':1})

for d in v.D:
    for d in v.f:
        print(v.f[d])

# defining a zero vector
def zero_vec(D):
    return Vec(D,{d:0 for d in D});
#Setter
def setter(vector,d,val): vector.f[d]=val

#getter
def getter(vector,d): return vector.f[d] if d in vector.f else 0


setter(v,'b',2);

print(getter(v,'b'))



