import numpy as np
import matplotlib.pyplot as plt


# Task 1
mathematics = np.array([5, 5, 6, 4, 3, 2])
chemistry = np.array([6, 6, 5, 4, 7, 6])
physics = np.array([1, 1, 2, 3, 1, 2])

subjects = ["Mathematics", "Chemistry", "Physics"]
means = [np.mean(mathematics), np.mean(chemistry), np.mean(physics)]
stds = [np.std(mathematics), np.std(chemistry), np.std(physics)]

print("Means:", means)
print("Standard deviations:", stds)

plt.figure()
plt.bar(subjects, means)
plt.title("Arithmetic means")
plt.ylabel("Grade")
plt.show()

plt.figure()
plt.bar(subjects, stds)
plt.title("Standard deviations")
plt.ylabel("Standard deviation")
plt.show()


# Task 2
m = 1
g = 9.81
h = 100
t = np.linspace(0, np.sqrt(2*h/g), 100)

Ek = 0.5 * m * (g*t)**2
Ep = m * g * (h - 0.5*g*t**2)

plt.figure()
plt.plot(t, Ek, label="Kinetic energy")
plt.plot(t, Ep, label="Potential energy")
plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")
plt.title("Ball falling freely")
plt.legend()
plt.grid()
plt.show()


# Task 3
A = np.loadtxt("zadanie3.txt", dtype=int)
np.savetxt("ts3.txt", A @ A.T, fmt="%d")
print("A @ A.T:\n", A @ A.T)


# Task 4
t = np.linspace(0, 5, 100)
a = 10
s = 0.5*a*t**2

s_after_3 = 0.5*a*3**2
print("Distance after 3 seconds:", s_after_3, "m")

plt.figure()
plt.plot(t, s)
plt.scatter(3, s_after_3, color="red")
plt.annotate(f"{s_after_3} m", (3, s_after_3))
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Motion with constant acceleration")
plt.grid()
plt.show()


# Task 5
n = 3
primes = []
number = 2

while len(primes) < n*n:
    for d in range(2, int(np.sqrt(number)) + 1):
        if number % d == 0:
            break
    else:
        primes.append(number)

    number += 1

matrix = np.array(primes).reshape(n, n)
np.savetxt("ts5.txt", matrix, fmt="%d")
print("Prime matrix:\n", matrix)
