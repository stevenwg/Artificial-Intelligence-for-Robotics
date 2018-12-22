#%%
from math import *
def update(mean1, var1, mean2, var2):
    new_mean = 1./(var1 + var2)*(var2*mean1 + var1*mean2)
    new_var = 1./(1./var1 + 1/var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

print(update(10., 4., 12., 4.))
print(predict(10., 4., 12., 4.))