



class Cross_Line:

    @staticmethod
    def flat_coor(x):
        a, b = x
        c = a + b
        v = c[0] + c[1] + c[2] + c[3]
        return v

    @classmethod
    def findIntersection(cls,x):
        x1, y1, x2, y2, x3, y3, x4, y4 = Cross_Line.flat_coor(x)

        try:
            px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                    (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                    (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            return (px,py)
        except ZeroDivisionError:
            return None

if __name__ == '__main__':
    c = Cross_Line()
    print(c.findIntersection(([[-1,2],[3,-4]],[[0,-6],[1,8]])))