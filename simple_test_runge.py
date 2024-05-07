import numpy
def func(x):
    return x**2
class TestRungeKutt:
    def __init__(self, A, b, w, V, time_start, time_end):
        # Creating data
        self.epsilon = []
        self.x_axis = []
        self.TAU_mass = numpy.arange(0.0001, 0.001, 0.0001)
        for h in self.TAU_mass:
            self.x = [0] * round((time_end - time_start) / h)
            self.x_axis = numpy.arange(time_start, time_end, h)
            self.time = numpy.arange(time_start, time_end, h)
            self.eps = 0
            for i in range(1, round(len(self.x))):
                k1x = 2 * self.time[i]
                k2x = 2 * (self.time[i] + h / 2)
                k3x = 2 * (self.time[i] + h / 2)
                k4x = 2 * (self.time[i] + h)
                self.x[i] = self.x[i-1] + (k1x + 2 * k2x + 2 * k3x + k4x) * (h/6)
                self.eps = max(self.eps, abs(self.x[i] - func(self.time[i])))
            self.epsilon.append(numpy.log(self.eps))

    def count(self):
        return self.epsilon, self.TAU_mass, self.x, self.x_axis