import random
import matplotlib.pyplot as plt
class Perlin:
    def __init__(self):





    # List for Gradient Vectors
        self.gradients1D = []
        self.gradients2D = []
        self.gradients3D = []
    




    # Smoothing function
    def f(self, x):
        return 6*x**5-15*x**4+10*x**3





    # Linear interpolation function
    def lerp(self, a, b, c):
        return a*(1-c)+b*c





    # 1 Dimensional noise function
    def noise1D(self, x):





        # Lattice points
        x0=int(x)
        x1=x0+1
        dx0=x-x0
        dx1=dx0-1





        # Generationg enough Gradient Vectors
        while len(self.gradients1D)-1<=x:
            self.gradients1D.append(random.uniform(-1, 1))





        # Calculating dot products
        dot0=self.gradients1D[x0]*dx0
        dot1=self.gradients1D[x1]*dx1





        # Returning noise value for the corresponding coordinate
        return self.lerp(dot0, dot1, self.f(dx0))
    




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





    def noise3D(self, x, y, z):





        # Lattice points
        x0=int(x)
        x1=x0+1
        dx0=x-x0
        dx1=x-x1
        y0=int(y)
        y1=y0+1
        dy0=y-y0
        dy1=y-y1
        z0=int(z)
        z1=z0+1
        dz0=z-z0
        dz1=z-z1





        # Generating enough Gradient Vectors
        while len(self.gradients3D)<=x+1:
            self.gradients3D.append([])
        while len(self.gradients3D[x0])<=y+1:
            self.gradients3D[x0].append([])
        while len(self.gradients3D[x1])<=y+1:
            self.gradients3D[x1].append([])
        while len(self.gradients3D[x0][y0])<=z+1:
            self.gradients3D[x0][y0].append([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)])
        while len(self.gradients3D[x0][y1])<=z+1:
            self.gradients3D[x0][y1].append([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)])
        while len(self.gradients3D[x1][y0])<=z+1:
            self.gradients3D[x1][y0].append([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)])
        while len(self.gradients3D[x1][y1])<=z+1:
            self.gradients3D[x1][y1].append([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)])





        # Calculating dot products
        dot000=self.gradients3D[x0][y0][z0][0]*dx0+self.gradients3D[x0][y0][z0][1]*dy0+self.gradients3D[x0][y0][z0][2]*dz0
        dot001=self.gradients3D[x0][y0][z1][0]*dx0+self.gradients3D[x0][y0][z1][1]*dy0+self.gradients3D[x0][y0][z1][2]*dz1
        dot010=self.gradients3D[x0][y1][z0][0]*dx0+self.gradients3D[x0][y1][z0][1]*dy1+self.gradients3D[x0][y1][z0][2]*dz0
        dot100=self.gradients3D[x1][y0][z0][0]*dx1+self.gradients3D[x1][y0][z0][1]*dy0+self.gradients3D[x1][y0][z0][2]*dz0
        dot110=self.gradients3D[x1][y1][z0][0]*dx1+self.gradients3D[x1][y1][z0][1]*dy1+self.gradients3D[x1][y1][z0][2]*dz0
        dot011=self.gradients3D[x0][y1][z1][0]*dx0+self.gradients3D[x0][y1][z1][1]*dy1+self.gradients3D[x0][y1][z1][2]*dz1
        dot101=self.gradients3D[x1][y0][z1][0]*dx1+self.gradients3D[x1][y0][z1][1]*dy0+self.gradients3D[x1][y0][z1][2]*dz1
        dot111=self.gradients3D[x1][y1][z1][0]*dx1+self.gradients3D[x1][y1][z1][1]*dy1+self.gradients3D[x1][y1][z1][2]*dz1





        # Returning noise value for the corresponding coordinate
        return self.lerp(self.lerp(self.lerp(dot000, dot010, self.f(dy0)), self.lerp(dot001, dot101, self.f(dy0)), self.f(dz0)), self.lerp(self.lerp(dot010, dot110, self.f(dy0)), self.lerp(dot011, dot111, self.f(dy0)), self.f(dz0)), self.f(dx0))
if __name__=="__main__":
    noise=Perlin()
    plt.plot([noise.noise1D(x/20)*20 for x in range(100)])
    plt.show()