import numpy as np
a = int(input('plz entr n1 :'))
b = int(input('plz entr n2 :'))
c = int(input('plz entr n3 :'))
d = int(input('plz entr n4 :'))
e = int(input('plz entr n5 :'))
f = int(input('plz entr n6 :'))
g = int(input('plz entr n7 :'))
h = int(input('plz entr n8 :'))
i = int(input('plz entr n9 :'))
j = int(input('plz entr n10 :'))
k = int(input('plz entr n11 :'))
l = int(input('plz entr n12:'))
m = int(input('plz entr n13:'))
n = int(input('plz entr n14:'))
o = int(input('plz entr n15:'))
p = int(input('plz entr n16 :'))
q = int(input('plz entr n17 :'))
r = int(input('plz entr n18 :'))
s = int(input('plz entr n19 :'))
t = int(input('plz entr n20 :'))
u = int(input('plz entr n21 :'))
v = int(input('plz entr n22 :'))
w = int(input('plz entr n23 :'))
x = int(input('plz entr n24 :'))
y = int(input('plz entr n25 :'))

A = np.mat([[a, b, c, d, e], [f, g, h, i, j], [
           k, l, m, n, o], [p, q, r, s, t], [u, v, w, x, y]])
print('\n', A)
val, vec = np.linalg.eig(A)
print('\nur eigen values is : ', val)
print('\nur eigen vactors is : ', vec)
