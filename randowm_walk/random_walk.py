from random import choice

class RandomWalk():
    """Uma classe para gerar passeios aleatórios"""
    def __init__(self, num_points=50000):
        """Inicializa os atributos de um passeio"""
        self.num_points = num_points

        # Todos os passeios começam em 0,0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todos os pontos do passeio."""
        # Continua dando passos até que o passeio alcance o tamanho desejado.
        while len(self.x_values) < self.num_points:
            # Decide a direção a ser seguida e a distancia a ser percorrida nessa direção
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # Calcula os proximos valores de x e de y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)