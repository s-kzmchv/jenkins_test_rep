import numpy as np
#from semester10.Теория_множественного_доступа.class_markov_chain import MarkovChain


class MarkovChain:
    def __init__(self, start_point, conversion_matrix):
        for i in range(len(start_point)):
            if start_point[i] == 1:
                self.curr_state = i
                self.begin_state = i

        self.conversion_matrix = conversion_matrix

    def return_in_begin_state(self):
        self.curr_state = self.begin_state

    def t_conversion(self, t):
        res_vec_conversion = []
        res_vec_conversion.append(self.curr_state)
        for _ in range(t):
            self.conversion()
            res_vec_conversion.append(self.curr_state)

        return res_vec_conversion

    def conversion(self):
        prob = np.random.random(1)[0]
        curr_cumulative_p = 0
        for num_curr_conversion in range(len(self.conversion_matrix[self.curr_state])):
            curr_cumulative_p += self.conversion_matrix[self.curr_state][num_curr_conversion]
            if prob < curr_cumulative_p:
                self.curr_state = num_curr_conversion
                break

    def get_stationary_distribution(self):
        theoretical_linEq = self.conversion_matrix.transpose().copy()  # меняем переходы
        for i in range(len(theoretical_linEq)):
            theoretical_linEq[i][i] -= 1  # добавляем к диагонали -1
            theoretical_linEq[len(theoretical_linEq) - 1][i] = 1  # меняем последнее уравнение

        theoretical_linEq = np.linalg.inv(
            theoretical_linEq.transpose())  # берем обратную матрицу к полученной транспонированной матрице

        b = np.zeros(len(self.conversion_matrix[0, :]))
        b[-1] = 1
        theoretical_linEq = np.matmul(b, theoretical_linEq)  # умножаем на вектор\

        return theoretical_linEq


# admission 3
N = 100000
P = np.array([[0.7, 0.2, 0.1],
              [0.3, 0.2, 0.5],
              [0.0, 0.0, 1.0],])

start_point = np.array([1, 0, 0])



markov_chain = MarkovChain(start_point, P)
counter_all = 0
for _ in range(N):
    counter = 0
    # conversions = [markov_chain.begin_state, ]
    while markov_chain.curr_state != 2:
        markov_chain.conversion()
        # conversions.append(markov_chain.curr_state)
        counter += 1
    counter_all += counter
    markov_chain.return_in_begin_state()

print("average conversions = {}".format(counter_all / N))



theoretical_matrix_x = np.array([[1 - P[0, 0], -P[0, 1], ],
                               [-P[1, 0], 1 - P[1, 1], ],])

theoretical_matrix_y = np.array([1,1])

theoretical_res = theoretical_matrix_y @ np.linalg.inv(theoretical_matrix_x).transpose()



print(theoretical_res)

