import random
class Perlin:
    def __init__(self):





    # List for Gradient Vectors
        self.gradients3D = []
    




    # Smoothing function
    def f(self, x):
        return 6*x**5-15*x**4+10*x**3





    # Linear interpolation function
    def lerp(self, a, b, c):
        return a*(1-c)+b*c

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




