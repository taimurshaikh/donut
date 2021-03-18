class Vector:
    def __init__(self, elems):
        self.x = elems[0]
        self.y = elems[1]
        self.z = elems[2]

class Matrix3x3:
    def __init__(self, elems):
        self.elems = elems

    def vecMatMul(self, v):
        """ Multiplies 3-dimensional Vector with 3xn matrix """
        return Vector(v.x*self.elems[0][0] + v.y*self.elems[1][0] + v.z*self.elems[2][0],
                       v.x*self.elems[0][1] + v.y*self.elems[1][1] + v.z*self.elems[2][1],
                       v.x*self.elems[0][2] + v.y*self.elems[1][2] + v.z*self.elems[2][2])
