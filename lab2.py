
# problem 1
v=[-1,3]
u=[0,4]

# v+u
w = [v[i]+u[i]for i in range(len(v))]
print(w)

# v - u
print([v[i]-u[i] for i in range(len(v))])

# 3 v - 2 u
print([3*v[i]-2*u[i] for i in range(len(u))])

# problem 2

v = [2,-1,5]
u = [-1,1,1]

print([v[i]+u[i] for i in range(len(v))])
