# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import numpy
#from scipy import stats
#import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# VARIJABLE

# LISTE

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
speed2 = [32, 111, 138, 28, 59, 77, 97]  # druga lista za probu
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]  # lista random godina s W3Schoolsa

lista = numpy.random.uniform(0.0, 5.0, 100000)  # kreiranje 100000 različitih float vrijednosti između 0 i 5
# x = numpy.random.randint(2, 17, 20)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
     12, 13, 14, 16, 17, 18, 19, 20, 22]
# y = numpy.random.randint(85, 111, 20) # najmanja vrijednost, najveća vrijednost, veličina
# (u pravilu loš model)
y = [100,90,80,60,70,60,55,60,65,
     70,70,75,76,78,79,90,95,99,99,100]  # primjer za dobar odnos veličina i
# dobar model za predviđanje vrijednosti

# LISTE NORMALNIH RAZDIOBA

xlista = numpy.random.normal(20, 1, 10000)
ylista = numpy.random.normal(10, 2, 10000)
normalna = numpy.random.normal(5.0, 2.0, 100000)
"""normalna distribucija gdje je srednja vrijednost (mode) 5.0,
standardna devijacija je 2.0 i generiranih vrijednosti je 100000"""

# linearna regresija

slope, intercept, r, p, std_err = stats.linregress(x, y)  # slope,... su parametri koje vraća funkcija linregress()
def linearnaRegresija(q):
    return slope * q + intercept
model = list(map(linearnaRegresija, x))  # vraća listu vrijednosti y pridruženih svakoj x vrijednosti iz liste
brzina = linearnaRegresija(21)

# POLINOMSKA REGRESIJA
# https://www.w3schools.com/python/python_ml_polynomial_regression.asp
# https://www.w3schools.com/python/numpy/numpy_array_sort.asp
# https://www.w3schools.com/python/matplotlib_getting_started.asp
model1 = numpy.poly1d(numpy.polyfit(x, y, 5))  # polyfit traži 2 liste i stupanj polinomske funkcije
linija = numpy.linspace(1, 22, 100)  # ravnomjerno raspoređeni brojevi unutar zadanog intervala
# (x, y, broj vrijednosti između x i y)
predict = model1(15)

# ISPIS

## linearna

# print(x)
# print(y)
print(r)
print(model)

## polinomska

# print(r2_score(y, model1(x)))  # r2_score pokazuje koliko je dobar odnos vrijednosti, između 0 i 1
# 0 je najgori odnos, 1 je najbolji
# print(predict)

# plt graf postavke
# https://www.w3schools.com/python/matplotlib_intro.asp
plt.title("Probni graf")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(axis = 'both', color = 'black', linewidth = 0.5)
# plt.plot(xpoints, ypoints, marker = 'o', ms = 10, mec = 'g') # ms = marker size
# argument se može staviti x ili o (nisam testirao drugo) da prikaže isključivo te točke, ne kao liniju
# marker = 'o' arguement koristi se za naglašavanje svake točke na grafu
# https://www.w3schools.com/python/matplotlib_markers.asp pogledaj za markere
# plt.hist(normalna, 100)  # histogram s 100 stupaca koji prikazuje koliko se puta pojavljuje koja vrijednost u listi "normalna"

plt.scatter(x, y)  # potrebne dvije liste iste veličine (x i y vrijednosti točaka) i crta prikaz točaka u koordinatnom
plt.plot(x, model)
# plt.plot(linija, model1(linija)) # polinomska funkcija
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
