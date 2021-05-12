import shapely
from shapely.geometry import LineString
import random



line1 = LineString([(0,0), (1,1)])
line2 = LineString([(1,1), (1,-2)])

int_pt = line1.intersection(line2)

try:
    print(int_pt.x, int_pt.y)
except AttributeError:
    print('No match')

'''
x1, y1, x2, y2, x3, y3, x4, y4'''




def findIntersection(*args):
    x1, y1, x2, y2, x3, y3, x4, y4 = args
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
            (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
            (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    # print(px, py)
    return (px, py)

def check_work():
    for i in range(100):
        a = [random.randint(-1, 10) for i in range(8)]
        try:
            findIntersection(*a)
        except ZeroDivisionError:
            print(None)



xxx = ([[1,2],[3,4]],[[5,6],[7,8]])
def flat(x):
    a,b = x
    c= a+b
    v= c[0]+c[1]+c[2]+c[3]
    print(v)

def flatten(lists):
  results = []
  for numbers in lists:
    for numbers2 in numbers:
        results.append(numbers2)
  return results

if __name__ == '__main__':
    check_work()
