import random





class Perlin:
    def __init__(self):





    # List for Gradient Vectors
        self.gradients1D = []
    




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
    



