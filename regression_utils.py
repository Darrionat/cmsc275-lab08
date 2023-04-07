from stats_utils import mean, std_dev, sum_squared_deviations_computational
from readcsv import load_data
from math import sqrt


def z_score(point, data, population=True):
    m = mean(data)
    sd = std_dev(data, population)
    return (point - m) / sd


def sum_of_squares_xy(x, y):
    n = len(x)
    assert n > 0, n == len(y)
    xy_sum, x_sum, y_sum = 0, 0, 0
    for i in range(n):
        xy_sum += x[i] * y[i]
        x_sum += x[i]
        y_sum += y[i]
    return xy_sum - (x_sum * y_sum) / n


def linear_regression_correlation_definitional(data):
    """
    Computes r, by the definitional formula, for a set of data that is assumed to be a 2-dimensional array where every
    entry is an array of length 2.
    I.e. data should have dimension n x 2.
    :param data: Pairs of x,y points.
    :return: Returns the linear regression coefficient of the data.
    """
    x, y = [row[0] for row in data], [row[1] for row in data]
    n = len(x)
    assert n > 1
    sum_of_zscore_product = 0
    for i in range(n):
        z_x = z_score(x[i], x, False)
        z_y = z_score(y[i], y, False)
        sum_of_zscore_product += z_x * z_y
    return sum_of_zscore_product / (n - 1)


def linear_regression_correlation_computational(data):
    """
    Computes r, by the computational formula, for a set of data that is assumed to be a 2-dimensional array where every
    entry is an array of length 2.
    I.e. data should have dimension n x 2.
    :param data: Pairs of x,y points.
    :return: Returns the linear regression coefficient of the data.
    """
    x, y = [row[0] for row in data], [row[1] for row in data]
    SSxy = sum_of_squares_xy(x, y)
    SSx = sum_squared_deviations_computational(x)
    SSy = sum_squared_deviations_computational(y)
    return SSxy / sqrt(SSx * SSy)


if __name__ == '__main__':
    # data = load_data('CSPhDvsArcade.csv')
    data = load_data('Cigarettes_AgeLived.csv')
    r = linear_regression_correlation_computational(data)
    # print(linear_regression_correlation_definitional(data))
    print(r)
    print(r ** 2)
