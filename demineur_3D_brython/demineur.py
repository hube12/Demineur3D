import random, sys

sys.setrecursionlimit(2000)
pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)]
grille3D = [[[0] * 20 for i in range(20)] for j in range(20)]

# functions
def output(g):
    for col in g: print(" ".join(map(str, col)))


def bombe(d):
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    while grille3D[d][y][x] == "*":
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    grille3D[d][y][x] = "*"
    number(x, y, d)


def number(x, y,d):
    for c in pos:
        if 20>(y+c[0])>-1 and 20>(c[1]+x) > -1 :
            #grille courante
            if grille3D[d][y + c[0]][x + c[1]] != "*":
                grille3D[d][y + c[0]][x + c[1]] += 1
            #grille en retroaction: base inferieure du cube
            if d>0 and grille3D[d-1][y + c[0]][x + c[1]] != "*" :
                grille3D[d-1][y + c[0]][x + c[1]] += 1
            #grille en proaction: base superieure du cube
            if d<19:
                grille3D[d + 1][y + c[0]][x + c[1]] += 1


def onclick(grille, x, y,revele):
        if grille[y][x] == "*":
            print("perdu")
            return grille
        if grille[y][x] != 0:
            revele[y][x] = 1
            return revele
        grille[y][x] = "@"
        revele[y][x] = 1
        for c in pos:
            if 20>x + c[0] > -1 and 20>y + c[1] > -1:
                onclick(grille,x + c[0], y + c[1],revele)
        return revele

def outputFace(g):
    for i in range(20):
        print(" ".join(map(str, g[0][i])),end="  ")
        print(" ".join(map(str, g[1][i])),end="  ")
        print(" ".join(map(str, g[2][i])))
    print()

def main():
    for i in range(20):
        for loop in range(int(20*20*0.05)):
            bombe(i)
    print("e")
    outputFace(grille3D)
main()

