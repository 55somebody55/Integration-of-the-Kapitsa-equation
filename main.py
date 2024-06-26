import matplotlib.pyplot as plt
import numpy
import numpy as np
from Euler_1st import EulerFirst
# from Euler_1st_m import EulerFirstM
from Euler_3nd import EulerThird
from Runge_Kutt import RungeKutt
from test_Runge_Kutt import TestRungeKutt

# Definitions:

sin = numpy.sin
cos = numpy.cos
ln = numpy.log

# Constants:

h = 0.00001
time_start = 0
time_end = 20
x_axis = np.arange(time_start, time_end, h)

# Input conditions:

# 1) constants
L = 10
f0 = 0

# 2) values

A = 10
w = 100
F0 = 0.1

if __name__ == '__main__':

    # Using methods

    # euler_first_data, diagram_euler_first_data = EulerFirst(L, f0, A, w, F0, time_start, time_end, h).count()
    # euler_third_data, diagram_euler_third_data = EulerThird(L, f0, A, w, F0, time_start, time_end, h).count()
    runge_kutt_data, diagram_runge_kutt_data = RungeKutt(L, f0, A, w, F0, time_start, time_end, h).count()
    # test_epsilon, test_x_axis, test_runge_kutt_data, test_runge_x_axis = TestRungeKutt(4, 0, 11, 0, time_start, time_end).count()

    # Configuring graphics
    fig, ax = plt.subplots(2, 1, figsize=(8, 7))
    # plt.setp(ax, xlim=(time_start, time_end), ylim=(-4, 4))

    # Drawing graphics

    # ax[0, 0].plot(x_axis, euler_first_data, label="f(t)")
    # ax[0, 0].set_title("Euler first")
    # ax[1, 0].plot(euler_first_data, diagram_euler_first_data, label="f(t)")
    # ax[1, 0].set_title("Euler first diagram")
    #
    # ax[0, 1].plot(x_axis, euler_third_data, label="f(t)")
    # ax[0, 1].set_title("Euler third")
    # ax[1, 1].plot(euler_third_data, diagram_euler_third_data, label="f(t)")
    # ax[1, 1].set_title("Euler third diagram")

    ax[1].set_xlabel("x(time)")
    ax[1].set_ylabel("x'(time)")
    ax[0].plot(x_axis, runge_kutt_data, label="f(t)")
    ax[0].set_title("Runge Kutt")
    ax[0].set_xlabel("time")
    ax[0].set_ylabel("x(time)")
    ax[1].plot(runge_kutt_data, diagram_runge_kutt_data, label="f(t)")

    # ax[1].plot(ln(test_x_axis), test_epsilon, label="f(t)")
    # ax[1].text(-8.5, -18, "log Runge-Kutt", fontsize=12)
    # ax[1].set_xlabel("ln(tau)")
    # ax[1].set_ylabel("ln(eps))")
    # print(numpy.polyfit(ln(test_x_axis), test_epsilon, 1)[0])
    #
    # ax[0].plot(test_runge_x_axis, test_runge_kutt_data, label="f(t)")
    # ax[0].set_title("Test Runge-Kutt")
    # ax[0].set_xlabel("time")
    # ax[0].set_ylabel("x(time)")
    plt.show()
