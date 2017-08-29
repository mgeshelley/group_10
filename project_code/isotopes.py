#!/usr/bin/env python
import numpy as np
import sys
import matplotlib.pyplot as plt


label_o17 = np.genfromtxt('O_isotopes_chain_NushellX/o_17b.lpt',skip_header=6, usecols=(4),max_rows=5, dtype='string')
#print label_o17
e_o17 = np.genfromtxt('O_isotopes_chain_NushellX/o_17b.lpt',skip_header=6, usecols=(2),max_rows=5)
#print e_o17
x_o17 =[]
for i in range(len(e_o17)):
    x_o17.extend([1])
e_o17_code = [-3.926, -3.208,  2.112]
x_o17_code =[]
for i in range(len(e_o17_code)):
    x_o17_code.extend([1])
#print x_o17

label_o18 = np.genfromtxt('O_isotopes_chain_NushellX/o_18b.lpt',skip_header=6, usecols=(4),max_rows=5, dtype='string')
#print label_o17
e_o18 = np.genfromtxt('O_isotopes_chain_NushellX/o_18b.lpt',skip_header=6, usecols=(2),max_rows=5)
#print e_o17
x_o18 =[]
for i in range(len(e_o18)):
    x_o18.extend([2])
e_o18_code = [-11.932,  -9.933,  -8.405,  -7.572, -7.339]
x_o18_code =[]
for i in range(len(e_o18_code)):
    x_o18_code.extend([2])

label_o19 = np.genfromtxt('O_isotopes_chain_NushellX/o_19b.lpt',skip_header=6, usecols=(4),max_rows=5, dtype='string')
#print label_o17
e_o19 = np.genfromtxt('O_isotopes_chain_NushellX/o_19b.lpt',skip_header=6, usecols=(2),max_rows=5)
#print e_o17
x_o19 =[]
for i in range(len(e_o19)):
    x_o19.extend([3])
e_o19_code = [-15.956,  -15.838, -14.389, -13.586, -13.072]
x_o19_code =[]
for i in range(len(e_o19_code)):
    x_o19_code.extend([3])

label_o20 = np.genfromtxt('O_isotopes_chain_NushellX/o_20b.lpt',skip_header=6, usecols=(4),max_rows=5, dtype='string')
#print label_o17
e_o20 = np.genfromtxt('O_isotopes_chain_NushellX/o_20b.lpt',skip_header=6, usecols=(2),max_rows=5)
#print e_o17
x_o20 =[]
for i in range(len(e_o20)):
    x_o20.extend([4])
e_o20_code = [-23.632, -21.886, -20.013, -19.478, -18.518 ]
x_o20_code =[]
for i in range(len(e_o20_code)):
    x_o20_code.extend([4])

label_o21 = np.genfromtxt('O_isotopes_chain_NushellX/o_21b.lpt',skip_header=6, usecols=(4),max_rows=5, dtype='string')
#print label_o17
e_o21 = np.genfromtxt('O_isotopes_chain_NushellX/o_21b.lpt',skip_header=6, usecols=(2),max_rows=5)
#print e_o17
x_o21 =[]
for i in range(len(e_o21)):
    x_o21.extend([5])
e_o21_code = [-27.404, -26.029,-25.406, -24.439,-24.341 ]
x_o21_code =[]
for i in range(len(e_o21_code)):
    x_o21_code.extend([5])

label_o22 = np.genfromtxt('O_isotopes_chain_NushellX/o_22b.lpt',skip_header=6, usecols=(4),max_rows=5, dtype='string')
#print label_o17
e_o22 = np.genfromtxt('O_isotopes_chain_NushellX/o_22b.lpt',skip_header=6, usecols=(2),max_rows=5)
#print e_o17
x_o22 =[]
for i in range(len(e_o22)):
    x_o22.extend([6])
e_o22_code = [-34.498, -31.340,-29.736, -29.703,-28.135]
x_o22_code =[]
for i in range(len(e_o22_code)):
    x_o22_code.extend([6])

label_o23 = np.genfromtxt('O_isotopes_chain_NushellX/o_23b.lpt',skip_header=6, usecols=(4),max_rows=5, dtype='string')
#print label_o17
e_o23 = np.genfromtxt('O_isotopes_chain_NushellX/o_23b.lpt',skip_header=6, usecols=(2),max_rows=5)
#print e_o17
x_o23 =[]
for i in range(len(e_o23)):
    x_o23.extend([7])
e_o23_code = [-37.079, -34.486, -33.078, -30.136, -30.068]
x_o23_code =[]
for i in range(len(e_o23_code)):
    x_o23_code.extend([7])

label_o24 = np.genfromtxt('O_isotopes_chain_NushellX/o_24b.lpt',skip_header=6, usecols=(4),max_rows=5, dtype='string')
#print label_o17
e_o24 = np.genfromtxt('O_isotopes_chain_NushellX/o_24b.lpt',skip_header=6, usecols=(2),max_rows=5)
#print e_o17
x_o24 =[]
for i in range(len(e_o24)):
    x_o24.extend([8])
e_o24_code = [-41.225, -36.183, -35.266,-33.681, -33.251]
x_o24_code =[]
for i in range(len(e_o24_code)):
    x_o24_code.extend([8])

fig, ax = plt.subplots()
#ax.scatter(x_o17, e_o17)
for i, txt in enumerate(label_o17):
    ax.annotate(txt, (x_o17[i],e_o17[i]))

for i, txt in enumerate(label_o18):
    ax.annotate(txt, (x_o18[i],e_o18[i]))

for i, txt in enumerate(label_o19):
    ax.annotate(txt, (x_o19[i],e_o19[i]))

for i, txt in enumerate(label_o20):
    ax.annotate(txt, (x_o20[i],e_o20[i]))

for i, txt in enumerate(label_o21):
    ax.annotate(txt, (x_o21[i],e_o21[i]))

for i, txt in enumerate(label_o22):
    ax.annotate(txt, (x_o22[i],e_o22[i]))

for i, txt in enumerate(label_o23):
    ax.annotate(txt, (x_o23[i],e_o23[i]))

for i, txt in enumerate(label_o24):
    ax.annotate(txt, (x_o24[i],e_o24[i]))

plt.plot(x_o17, e_o17,'b_', markersize=20)
plt.plot(x_o17_code, e_o17_code,'rx', markersize=5)
plt.plot(x_o18, e_o18,'b_', markersize=20)
plt.plot(x_o18_code, e_o18_code,'rx', markersize=5)
plt.plot(x_o19, e_o19,'b_', markersize=20)
plt.plot(x_o19_code, e_o19_code,'rx', markersize=5)
plt.plot(x_o20, e_o20,'b_', markersize=20)
plt.plot(x_o20_code, e_o20_code,'rx', markersize=5)
plt.plot(x_o21, e_o21,'b_', markersize=20)
plt.plot(x_o21_code, e_o21_code,'rx', markersize=5)
plt.plot(x_o22, e_o22,'b_', markersize=20)
plt.plot(x_o22_code, e_o22_code,'rx', markersize=5)
plt.plot(x_o23, e_o23,'b_', markersize=20)
plt.plot(x_o23_code, e_o23_code,'rx', markersize=5)
plt.plot(x_o24, e_o24,'b_', markersize=20)
plt.plot(x_o24_code, e_o24_code,'rx', markersize=5)


# These statements makes a pretty plot:
plt.xlabel('valence neutrons')
plt.ylabel('Binding energy respect to 16O g.s. [MeV] ')
plt.legend(['output NushellX','output our code'], fontsize=12)
plt.title('O isotopes chain', fontsize=20)
plt.xlim(0, 13)
plt.ylim(-50, 5)
# This statement shows the plot, but you can also save the figure directly with savefig('filename'):
#plt.grid()
plt.show()

