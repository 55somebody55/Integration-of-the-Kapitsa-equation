import numpy

# definitions

sin = numpy.sin
cos = numpy.cos


class EulerThird:
    g = 9.81

    def __init__(self, L, f0, A, w, F0, time_start, time_end, h):

        # Creating data
        self.F = [F0] * round((time_end - time_start) / h)
        self.z = [f0] * round((time_end - time_start) / h)
        self.time = time_start

        for i in range(1, round(len(self.F))):
            z = (h / L) * (sin(self.F[i - 1])) * (A * w ** 2 * sin(w * self.time) - EulerThird.g) + self.z[i - 1]
            F = self.z[i - 1] * h + self.F[i - 1]
            self.z[i] = (h/(2*L)) * ((sin(self.F[i-1])) * (A * w**2 * sin(w * self.time) - EulerThird.g) + (sin(F)) * (A * w**2 * sin(w * (self.time + h)) - EulerThird.g)) + self.z[i-1]
            self.F[i] = (self.z[i-1] + z) * (h/2) + self.F[i-1]
            self.time += h

    def count(self):
        return self.F, self.z
