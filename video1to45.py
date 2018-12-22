#%%
p = []
n = 5
for i in range(n):
    p.append(1/n)

print(p)

#%%
p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit  = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))

    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s

    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        # Only Exact Move
        # q.append(p[(i - U) % len(p)])

        # Inexact Move
        s = pExact * p[(i - U) % len(p)]
        s += pOvershoot * p[(i - U - 1) % len(p)]
        s += pUndershoot * p[(i - U + 1) % len(p)]
        q.append(s)
    return q

# for k in range(len(measurements)):
#     p = sense(p, measurements[k])

# print(move(p, 1))

# p = move(p, 1)
# p = move(p, 1)

for k in range(1000):
    p = move(p, 1)

print(p)