import matplotlib.pyplot as plt
import numpy as np

class Volter:
        h = 0.01
        tpoints = np.arange(0, 30, h)
        xpoints, ypoints = [], []
        graph = np.array([1, 1], float)

        def put_points(self):
                for t in self.tpoints:
                        self.xpoints.append(self.graph[0])
                        self.ypoints.append(self.graph[1])
                        self.graph += self.calc_Runge_Kutta(t)

        def calc_Runge_Kutta(self, t):
                k1 = self.h*self.calc_val_of_func(self.graph, t)
                k2 = self.h*self.calc_val_of_func(self.graph+0.5*k1, t+0.5*self.h)
                k3 = self.h*self.calc_val_of_func(self.graph+0.5*k2, t+0.5*self.h)
                k4 = self.h*self.calc_val_of_func(self.graph+k3, t+self.h)
                return (k1 + 2*k2 + 2*k3 + k4)/6

        def print_graph(self):
                plt.plot(self.tpoints, self.xpoints, color='green', label='Жертвы')
                plt.plot(self.tpoints, self.ypoints, color='red', label='Хищники')
                plt.legend()
                plt.xlabel("Время")
                plt.ylabel("Популяция")
                plt.title("Модель Лотки-Вольтерра")
                plt.show()

        def calc_val_of_func(self, r, t):
                alpha = 1.0 #размножение жертв
                beta = 0.5 #поедание хищниками жертв
                gamma = 0.5 #вымирание хищников
                sigma = 2.0 #размножение хищников
                x, y = r[0], r[1]
                fxd = x*(alpha - beta*y)
                fyd = -y*(gamma - sigma*x)
                return np.array([fxd, fyd], float)


if __name__ == '__main__':
        model = Volter()
        model.put_points()
        model.print_graph()



