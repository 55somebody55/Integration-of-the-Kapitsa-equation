import numpy

# definitions

sin = numpy.sin
cos = numpy.cos


class RungeKutt:
    g = 9.81

    def __init__(self, L, f0, A, w, F0, time_start, time_end, h):

        # Creating data
        self.F = [F0] * round((time_end - time_start) / h)
        self.z = [f0] * round((time_end - time_start) / h)
        self.time = time_start
        error = -50

        for i in range(1, round(len(self.F))):
            k1z = (1/L) * (A * w**2 * sin(w * self.time) - RungeKutt.g) * sin(self.F[i - 1])
            k1f = self.z[i-1]
            k2z = (1/L) * (A * w**2 * sin(w * (self.time + h/2)) - RungeKutt.g) * sin(self.F[i - 1] + h * k1f/2)
            k2f = self.z[i - 1] + h * k1z/2
            k3z = (1/L) * (A * w ** 2 * sin(w * (self.time + h / 2)) - RungeKutt.g) * sin(self.F[i - 1] + h * k2f / 2)
            k3f = self.z[i - 1] + h * k2z / 2
            k4z = (1 / L) * (A * w ** 2 * sin(w * (self.time + h)) - RungeKutt.g) * sin(self.F[i - 1] + h * k3f)
            k4f = self.z[i - 1] + h * k3z
            self.F[i] = self.F[i-1] + (k1f + 2 * k2f + 2 * k3f + k4f) * (h/6)
            self.z[i] = self.z[i-1] + (k1z + 2 * k2z + 2 * k3z + k4z) * (h/6)
            self.time += h

    def count(self):
        return self.F, self.z