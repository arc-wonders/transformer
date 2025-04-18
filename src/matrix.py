# matrix.py

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0.0 for _ in range(cols)] for _ in range(rows)]

    def set(self, r, c, value):
        self.data[r][c] = value

    def get(self, r, c):
        return self.data[r][c]

    def fill_dummy(self):
        val = 1.0
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = val
                val += 1

    def fill(self, val):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = val

    def print(self):
        for row in self.data:
            print(" ".join(f"{val:.1f}" for val in row))
        print()

    def add(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def multiply(self, other):
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

    def scalar_multiply(self, scalar):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * scalar
        return result

    def dot_product(self, other):
        result = 0.0
        for i in range(self.rows):
            for j in range(self.cols):
                result += self.data[i][j] * other.data[i][j]
        return result
    
    def dot(self, other):
        assert self.cols == other.rows, "Matrix dimensions do not match for dot product"
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum_val = 0
                for k in range(self.cols):
                    sum_val += self.data[i][k] * other.data[k][j]
            result.data[i][j] = sum_val
        return result

 