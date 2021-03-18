class Matrix3x3:
    def __init__(self, elems):
        self.elems = elems
    
    def add(self, mat):
        if len(self.elems[0]) != len(mat.elems):
            raise ValueError
        else:
            for i in range(len(self.elems)):
                for j in range(len(self.elems[i])):
                    self.elems[i][j] += mat.elems[i][j]

    def sub(self, mat):
        if len(self.elems[0]) != len(mat.elems):
            raise ValueError
        else:
            for i in range(len(self.elems)):
                for j in range(len(self.elems[i])):
                    self.elems[i][j] -= mat.elems[i][j]
        
def vecMatMul(elems, v):
    """ Multiplies 3-dimensional Vector with 3xn matrix """
    return PVector(v.x*elems[0][0] + v.y*elems[1][0] + v.z*elems[2][0], 
                v.x*elems[0][1] + v.y*elems[1][1] + v.z*elems[2][1],
                v.x*elems[0][2] + v.y*elems[1][2] + v.z*elems[2][2])

def matMul(a, b):
    colsA = len(a[0])
    rowsA = len(a)
    colsB = len(a[0])
    rowsB = len(a)
    print(colsA)
    print(rowsA)
    
    result = []
    
    if colsA != rowsB:
        raise ValueError
        return None
    
    for i in range(rowsA):
        result.append([])
        for j in range(colsB):
            s = 0
            for k in range(colsB):
                s += a[i][k] * b[k][j]
            result[i].append(s)
    return result
    
    
