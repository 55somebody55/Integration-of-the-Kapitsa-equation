import numpy

# definitions

sin = numpy.sin
cos = numpy.cos
e = numpy.exp
ln = numpy.log
sqrt = numpy.sqrt


def func(A, b, w, time):
    return A * e(-b*time) * cos(sqrt(w**2 - b**2)*time)


class TestRungeKutt:

    def __init__(self, A, b, w, V, time_start, time_end):

        # Creating data
        self.epsilon = []
        self.x_axis = []
        self.TAU_mass = numpy.arange(0.0001, 0.001, 0.0001)
        for h in self.TAU_mass:
            self.x_axis = numpy.arange(time_start, time_end, h)
            self.time = numpy.arange(time_start, time_end, h)
            self.x = [A] * len(self.x_axis)
            self.z = [V] * len(self.x_axis)
            self.eps = 0
            for i in range(1, len(self.x_axis)):
                k1z = (-1) * (w ** 2 * self.x[i - 1] + 2 * b * self.z[i - 1]) * h
                k1x = self.z[i - 1] * h
                k2z = (-1) * (w ** 2 * (self.x[i - 1] + k1x / 2) + 2 * b * (self.z[i - 1] + k1z / 2)) * h
                k2x = (self.z[i - 1] + k1z / 2) * h
                k3z = (-1) * (w ** 2 * (self.x[i - 1] + k2x / 2) + 2 * b * (self.z[i - 1] + k2z / 2)) * h
                k3x = (self.z[i - 1] + k2z / 2) * h
                k4z = (-1) * (w ** 2 * (self.x[i - 1] + k3x) + 2 * b * (self.z[i - 1] + k3z)) * h
                k4x = (self.z[i - 1] + k3z) * h
                self.x[i] = self.x[i - 1] + (k1x + 2 * k2x + 2 * k3x + k4x) * (1/6)
                self.z[i] = self.z[i - 1] + (k1z + 2 * k2z + 2 * k3z + k4z) * (1/6)
                self.eps = max(self.eps, abs(self.x[i] - func(A, b, w, self.time[i])))
            self.epsilon.append(ln(self.eps))

    def count(self):
        return self.epsilon, self.TAU_mass, self.x, self.x_axis
