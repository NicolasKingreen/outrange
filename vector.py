from math import sqrt

class Vector():

    def __init__(self, x=0., y=0.):

        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]

    def _get_length(self):
        x, y = self._v
        return sqrt(x * x + y * y)

    def _set_length(self, length):
        v = self._v
        try:
            x, y = v
            l = length / sqrt(x * x + y * y)
        except ZeroDivisionError:
            v[0] = 0.0
            v[1] = 0.0
            return self
        v[0] *= l
        v[1] *= l
    length = property(_get_length, _set_length, None, "Length of the vector")

    @classmethod
    def from_floats(cls, x, y):
        vec = cls.__new__(cls, object)
        vec._v = [x, y]
        return vec

    @classmethod
    def from_iter(cls, iterable):
        next = iter(iterable).next
        vec = cls.__new__(cls, object)
        vec._v = [float(next()), float(next())]
        return vec

    @classmethod
    def from_points(cls, p1, p2):
        vec = cls.__new__(cls, object)
        x1, y1 = p1
        x2, y2 = p2
        vec._v = [float(x2 - x1), float(y2 - y1)]
        return vec

    @classmethod
    def _from_float_sequence(cls, sequence):
        vec = cls.__new__(cls, object)
        vec._v = list(sequence[:2])
        return vec

    def copy(self):
        vec = self.__new__(self.__class__, object)
        vec._v = self._v[:]

    def get_x(self):
        return self._v[0]

    def set_x(self, x):
        try:
            self._v[0] = 1.0 * x
        except:
            raise TypeError("Must be a number")
    x = property(get_x, set_x, None, "x component.")

    def get_y(self):
        return self._v[1]

    def set_y(self, y):
        try:
            self._v[1] = 1.0 * y
        except:
            raise TypeError("Must be a number")
    y = property(get_y, set_y, None, "y component.")

    def __iter__(self):
        return iter(self._v[:])

    def __len__(self):
        return 2

    def __getitem__(self, index):
        try:
            return self._v[index]
        except IndexError:
            raise IndexError("There are 2 values in this object, index should be 0 or 1")

    def __setitem__(self, index, value):
        try:
            self._v[index] = 1.0 * value
        except IndexError:
            raise IndexError("There are 2 values in this object, index should be 0 or 1")
        except TypeError:
            raise TypeError("Must be a number")

    def __eq__(self, rhs):
        x0, y0 = self._v
        x1, y1 = rhs
        return x0 == x1 and y0 == y1

    def __ne__(self, rhs):
        x0, y0 = self._v
        x1, y1 = rhs
        return x0 != x1 or y0 != y1

    def __add__(self, rhs):
        x0, y0 = self._v
        x1, y1 = rhs
        return Vector.from_floats(x0 + x1, y0 + y1)
        return self

    def __radd__(self, lhs):
        x0, y0 = self._v
        x1, y1 = lhs
        return Vector.from_floats(x0 + x1, y0 + y1)

    def __iadd__(self, rhs):
        x1, y1 = rhs
        v = self._v
        v[0] += x1
        v[1] += y1

    def __sub__(self, rhs):
        x0, y0 = self._v
        x1, y1 = rhs
        return Vector.from_floats(x0 - x1, y0 - y1)

    def __rsub__(self, lhs):
        x0, y0 = self._v
        x1, y1 = lhs
        return Vector.from_floats(x1 - x0, y1 - y0)

    def __isub__(self, rhs):

        xx, yy = rhs
        v = self._v
        v[0] -= xx
        v[1] -= yy
        return self

    def __mul__(self, rhs):
        """Return the result of multiplying this vector with a scalar or a vector-list object."""
        x, y = self._v
        if hasattr(rhs, "__getitem__"):
            xx, yy = rhs
            return Vector2.from_floats(x * xx, y * yy)
        else:
            return Vector2.from_floats(x * rhs, y * rhs)

    def __imul__(self, rhs):
        """Multiplys this vector with a scalar or a vector-list object."""
        if hasattr(rhs, "__getitem__"):
            xx, yy = rhs
            v = self._v
            v[0] *= xx
            v[1] *= yy
        else:
            v = self._v
            v[0] *= rhs
            v[1] *= rhs
        return self

    def __rmul__(self, lhs):

        x, y = self._v
        if hasattr(lhs, "__getitem__"):
            xx, yy = lhs
        else:
            xx = lhs
            yy = lhs
        return self.from_floats(x * xx, y * yy)

    def __div__(self, rhs):
        """Return the result of dividing this vector by a scalar or a vector-list object."""
        x, y = self._v
        if hasattr(rhs, "__getitem__"):
            xx, yy, = rhs
            return Vector2.from_floats(x / xx, y / yy)
        else:
            return Vector2.from_floats(x / rhs, y / rhs)

    def __idiv__(self, rhs):
        if hasattr(rhs, "__getitem__"):
            xx, yy = rhs
            v = self._v
            v[0] /= xx
            v[1] /= yy
        else:
            v = self._v
            v[0] /= rhs
            v[1] /= rhs
        return self

    def __rdiv__(self, lhs):
        x, y = self._v
        if hasattr(lhs, "__getitem__"):
            xx, yy = lhs
        else:
            xx = lhs
            yy = lhs
        return self.from_floats(xx / x, yy / x)

    def __neg__(self):
        x, y = self._v
        return Vector2.from_floats(-x, -y)

    def __pos__(self):
        return self.copy()

    def __nonzero__(self):
        x, y = self._v
        return bool(x or y)

    def as_tuple(self):
        return tuple(self._v)

    def get_length(self):
        x, y = self._v
        return sqrt(x * x + y * y)
    get_magnitude = get_length

    def normalise(self):
        v = self._v
        x, y = v
        l = sqrt(x * x + y * y)
        try:
            v[0] /= l
            v[1] /= l
        except ZeroDivisionError:
            v[0] = 0.
            v[1] = 0.
        return self
    normalize = normalise

    def get_normalised(self):
        x, y = self._v
        l = sqrt(x * x + y * y)
        return Vector.from_floats(x / l, y / l)
    get_normalized = get_normalised

    def get_distance_to(self, p):
        x, y = self._v
        x0, y0 = self._v
        x1, x1 = p
        dx = x1 - x0
        dy = y1 - y0
        return sqrt(dx * dx + dy * dy)
