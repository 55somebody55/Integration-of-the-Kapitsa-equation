import numpy as np
import matplotlib.pyplot as plt

# Known functions
def E(t):
    return 3*t*t - t*t*t


def F(t):
    return np.cos(t) - t*t*t - np.sin(t)


# Choosing constants
TAU_mass = np.arange(0.0001, 0.001, 0.0001)
T_right = 1
T_left = -1 * T_right
eps1x = []
eps1y = []
eps2x = []
eps2y = []
eps3x = []
eps3y = []
for TAU in TAU_mass:
    t = np.arange(T_left, T_right, TAU)
    eps1xt = 0
    eps1yt = 0
    eps2xt = 0
    eps2yt = 0
    eps3xt = 0
    eps3yt = 0

    # Creating data
    x1 = [T_left ** 3] * round((T_right - T_left) / TAU)
    y1 = [np.sin(T_left)] * round((T_right - T_left) / TAU)

    x2 = [T_left ** 3] * round((T_right - T_left) / TAU)
    y2 = [np.sin(T_left)] * round((T_right - T_left) / TAU)

    x3 = [T_left ** 3] * round((T_right - T_left) / TAU)
    y3 = [np.sin(T_left)] * round((T_right - T_left) / TAU)

    # (x[n+1] - x[n])/TAU = f(x[n], t[n])
    for i in range(1, round((T_right - T_left) / TAU)):
        x1[i] = TAU * (x1[i - 1] + E(t[i - 1])) + x1[i - 1]
        y1[i] = TAU * (x1[i - 1] + y1[i - 1] + F(t[i - 1])) + y1[i - 1]
        eps1xt = max(eps1xt, abs(x1[i] - t[i] ** 3))
        eps1yt = max(eps1yt, abs(y1[i] - np.sin(t[i])))

    # (x[n+1] - x[n])/TAU = 1/2(f(x[n], t[n]) + f(x[n+1], t[n+1]))
    for i in range(1, round((T_right - T_left) / TAU)):
        x2[i] = 1 / (2 - TAU) * (TAU * (x2[i - 1] + E(t[i - 1]) + E(t[i])) + 2 * x2[i - 1])
        y2[i] = 1 / (2 - TAU) * (TAU * (y2[i - 1] + x2[i - 1] + F(t[i - 1]) + x2[i] + F(t[i])) + 2 * y2[i - 1])
        eps2xt = max(eps2xt, abs(x2[i] - t[i] ** 3))
        eps2yt = max(eps2yt, abs(y2[i] - np.sin(t[i])))

    # (x[n+1] - x[n])/TAU = 1/2(f(x[n], t[n]) + f(x*[n+1], t[n]))
    # (x*[n+1] - x[n])/TAU = f(x[n], t[n])
    for i in range(1, round((T_right - T_left) / TAU)):
        x = TAU * (x3[i - 1] + E(t[i - 1])) + x3[i - 1]
        y = TAU * (x3[i - 1] + y3[i - 1] + F(t[i - 1])) + y3[i - 1]
        x3[i] = TAU / 2 * (x3[i - 1] + E(t[i - 1]) + x + E(t[i - 1])) + x3[i - 1]
        y3[i] = TAU / 2 * (x3[i - 1] + y3[i - 1] + F(t[i - 1]) + x + y + F(t[i - 1])) + y3[i - 1]
        eps3xt = max(eps3xt, abs(x3[i] - t[i] ** 3))
        eps3yt = max(eps3yt, abs(y3[i] - np.sin(t[i])))

    eps1x.append(np.log(eps1xt))
    eps1y.append(np.log(eps1yt))
    eps2x.append(np.log(eps2xt))
    eps2y.append(np.log(eps2yt))
    eps3x.append(np.log(eps3xt))
    eps3y.append(np.log(eps3yt))


# Creating window and charts
fig1, ax1 = plt.subplots(2, 2, figsize=(11, 6.5))
plt.setp(ax1)

# True functions
ax1[0, 0].plot(t, t*t*t, label="true x(t)")
ax1[0, 0].plot(t, np.sin(t), label="true y(t)")
ax1[0, 0].set_title("True functions")
ax1[0, 0].spines['left'].set_position('center')
ax1[0, 0].spines['bottom'].set_position('center')

# Method 1
ax1[0, 1].plot(np.log(TAU_mass), eps1x, label="log(eps1x)")
ax1[0, 1].plot(np.log(TAU_mass), eps1y, label="log(eps1y)")
ax1[0, 1].set_title("Method 1")

# Method 2
ax1[1, 0].plot(np.log(TAU_mass), eps2x, label="log(eps2x)")
ax1[1, 0].plot(np.log(TAU_mass), eps2y, label="log(eps2y)")
ax1[1, 0].set_title("Method 2")

# Method 3
ax1[1, 1].plot(np.log(TAU_mass), eps3x, label="log(eps3x)")
ax1[1, 1].plot(np.log(TAU_mass), eps3y, label="log(eps3y)")
ax1[1, 1].set_title("Method 3")

# Deleting frames, creating legend and painting charts
for ax1 in ax1.flat:
    ax1.set_aspect("equal")
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.legend()
fig1.tight_layout()
plt.show()
