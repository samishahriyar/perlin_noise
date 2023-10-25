import random
class Perlin:
    def __init__(self):





    # List for Gradient Vectors
        self.gradients2D = []
    




    # Smoothing function
    def f(self, x):
        return 6*x**5-15*x**4+10*x**3





    # Linear interpolation function
    def lerp(self, a, b, c):
        return a*(1-c)+b*c
    




    # 2 Dimensional noise function
    def noise2D(self, x, y):





        # Lattice points
        x0=int(x)
        x1=x0+1
        dx0=x-x0
        dx1=x-x1
        y0=int(y)
        y1=y0+1
        dy0=y-y0
        dy1=y-y1





        # Generating enough Gradient Vectors
        while len(self.gradients2D)<=x+1:
            self.gradients2D.append([])
        while len(self.gradients2D[x0])<=y+1:
            self.gradients2D[x0].append([random.uniform(-1, 1), random.uniform(-1, 1)])
        while len(self.gradients2D[x1])<=y+1:
            self.gradients2D[x1].append([random.uniform(-1, 1), random.uniform(-1, 1)])
            
        



        # Calculating dot products
        dot00=self.gradients2D[x0][y0][0]*dx0+self.gradients2D[x0][y0][1]*dy0
        dot01=self.gradients2D[x0][y1][0]*dx0+self.gradients2D[x0][y1][1]*dy1
        dot10=self.gradients2D[x1][y0][0]*dx1+self.gradients2D[x1][y0][1]*dy0
        dot11=self.gradients2D[x1][y1][0]*dx1+self.gradients2D[x1][y1][1]*dy1





        # Returning noise value for the corresponding coordinate
        return self.lerp(self.lerp(dot00, dot01, self.f(dy0)), self.lerp(dot10, dot11, self.f(dy0)), self.f(dx0))




