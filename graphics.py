import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89])
y = np.array([1.793, 1.870, 1.950, 2.019, 2.093, 2.180, 2.303, 2.428, 2.580, 2.718, 2.882, 3.045, 3.398, 3.700, 4.089])
model = LinearRegression().fit(x.reshape((-1, 1)), y)
r_sq = model.score(x.reshape((-1, 1)), y)
print('coef', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
# rss = np.sum(np.square(x - y))
# print(rss
y_pred = model.predict(np.array([0]).reshape((-1, 1)))
print(y_pred)
slope, intercept = np.polyfit(x, y, 1)
print(f'Функция {round(slope, 4)} * x + {round(intercept, 4)}')

# plt.plot(x, y, 'blue')
plt.title('Коэффициенты и проходы при 1:0')
plt.plot(x, y, 'o')
plt.plot(x, slope*x + intercept, 'red')
plt.show()


# e = math.exp(1)
# x = np.linspace(-10, 10, 100)
# y = 1 / (1 + e ** -x)
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# plt.plot(x, y, 'blue')
# plt.show()


# x = np.array([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
# y = np.array([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# model = LinearRegression().fit(x.reshape((-1, 1)), y)
# r_sq = model.score(x.reshape((-1, 1)), y)
# print('coef', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
# # rss = np.sum(np.square(x - y))
# # print(rss
# y_pred = model.predict(np.array([0]).reshape((-1, 1)))
# print(y_pred)
# slope, intercept = np.polyfit(x, y, 1)
# print(f'Функция {round(slope, 4)} * x + {round(intercept, 4)}')

# # plt.plot(x, y, 'blue')
# plt.title('Коэффициенты и проходы при 1:0')
# plt.plot(x, y, 'o')
# plt.plot(x, slope*x + intercept, 'red')
# plt.show()


# import hashlib
#
# password = 'hK9pk7S8E9TT'
#
# hash_object = hashlib.md5(password.encode('utf8'))
# print(hash_object.hexdigest())
#
# cur_x = 3  # The algorithm starts at x=3
# rate = 0.01  # Learning rate
# precision = 0.000001  # This tells us when to stop the algorithm
# previous_step_size = 1  #
# max_iters = 10000  # maximum number of iterations
# iters = 0  # iteration counter
# df = lambda x: (x + 5) ** 2  # Gradient of our function
# while previous_step_size > precision and iters < max_iters:
#     prev_x = cur_x  # Store current x value in prev_x
#     cur_x = cur_x - rate * df(prev_x)  # Grad descent
#     previous_step_size = abs(cur_x - prev_x)  # Change in x
#     iters = iters + 1  # iteration count
#     print("Iteration", iters, "\nX value is", cur_x)  # Print iterations
#
# print("The local minimum occurs at", cur_x)
