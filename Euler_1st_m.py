import numpy

# definitions

sin = numpy.sin
cos = numpy.cos


class EulerFirstM:
    g = 9.81

    def __init__(self, L, f0, A, w, F0, time_start, time_end, h):

        # Creating data
        self.F = [F0] * round((time_end - time_start) / h)
        self.z = [f0] * round((time_end - time_start) / h)
        self.time = time_start

        for i in range(1, round(len(self.F))):
            self.time += h
            self.z[i] = (h/L) * (sin(self.z[i-1] * h + self.F[i-1])) * (A * w**2 * sin(w * self.time) - EulerFirstM.g) + self.z[i-1]
            self.F[i] = self.z[i] * h + self.F[i-1]

    def count(self):
        return self.F, self.z

