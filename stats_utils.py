import math


def non_empty_check(samples):
    if len(samples) == 0:
        raise ArithmeticError("Cannot operate on empty list")


def mean(samples):
    """
    Computes the mean of the given list.
    Uses the typical sum(allElements) / N formula.
    :param samples: A non-empty list of numerical values
    :return: Returns the mean of the given input
    """
    non_empty_check(samples)
    sum = 0
    for x in samples:
        sum += x
    return sum / len(samples)


def mode(samples):
    """
    Computes the mode(s), or the most frequent value(s), of the given list.
    :param samples: A non-empty list of numerical values.
    :return:  Returns a single-value or a list containing the mode(s) of the given input.
    """
    non_empty_check(samples)
    # Creates a frequency table based upon the given sample
    # Elements of samples are the keys of the dictionary and their frequency will be the value
    freq = {}
    for x in samples:
        if x in freq:
            freq[x] = freq[x] + 1
        else:
            freq[x] = 1
    # Finds which key(s) in the frequency table have the largest value.
    max_value = 0
    to_return = []
    for x in freq.keys():
        # If this x is the most frequent of all, update accordingly
        if freq[x] > max_value:
            max_value = freq[x]
            to_return = [x]
            continue
        # If this x is as frequent as the most frequent, add to to_return
        if freq[x] == max_value:
            to_return.append(x)
    # If unimodal, only return the singular mode.
    if len(to_return) == 1:
        return to_return[0]
    return to_return


def median(samples):
    """
    Computes the median of the given list.
    :param samples: A non-empty list of numerical values.
    :return: Returns the median of the given list
    """
    non_empty_check(samples)
    samples.sort()
    N = len(samples)
    # If samples is of even length, return average of two middle-most elements
    if N % 2 == 0:
        # The left and right middle indices
        middle_index_left, middle_index_right = int((N / 2) - 1), int(N / 2)
        return mean([samples[middle_index_left], samples[middle_index_right]])
    # If samples is of odd length, return the middle element
    return samples[int((N - 1) / 2)]


def sum_squared_deviations_definitional(samples):
    """
    Computes the sum of squared deviations from the mean of the given list using the definitional formula.
    :param samples: A non-empty list of numerical values.
    :return: Returns the sum of squared deviations from the mean.
    """
    non_empty_check(samples)
    mu = mean(samples)
    SS = 0
    for x in samples:
        # First the different of x and mu, then square, and then add to final sum
        SS += pow(x - mu, 2)
    return SS


def sum_squared_deviations_computational(samples):
    """
    Computes the sum of squared deviations from the mean of the given list using the computational formula.
    :param samples: A non-empty list of numerical values.
    :return: Returns the sum of squared deviations from the mean.
    """
    non_empty_check(samples)
    # The sum of all points after being squared
    sum_x_squared = 0
    # The sum of all points
    sum_x = 0
    for x in samples:
        sum_x_squared += pow(x, 2)
        sum_x += x
    # The computational formula
    return sum_x_squared - pow(sum_x, 2) / len(samples)


def variance(samples, population=True):
    """
    Computes the variance of the given list.
    :param samples: A non-empty list of numerical values.
    :param population: If True, then use the population formula for variance; otherwise, use sample formula.
    :return: Returns the variance based upon the given input.
    """
    non_empty_check(samples)
    SS = sum_squared_deviations_computational(samples)
    N = len(samples)
    # Population variance
    if population:
        return SS / N
    # Avoid size 1 samples
    if N == 1:
        raise ArithmeticError('Cannot have sample of length 1')
    return SS / (N - 1)


def std_dev(samples, population=True):
    """
    Computes the standard deviation of the given list.
    :param samples: A non-empty list of numerical values.
    :param population: If True, then use the population formula for standard deviation; otherwise, use sample formula.
    :return: Returns the standard deviation based upon the given input.
    """
    if population:
        return math.sqrt(variance(samples))
    return math.sqrt(variance(samples, False))


'''
patch incorect formula
def std_error_from_mean(samples):
    """
    Computes the standard error from the mean.
    Assumes that the given list is a sample of a larger population.
    :param samples: A non-empty list of numerical values.
    :return: Returns the standard error of the mean.
    """
    # Formula:  std_dev of the sample / sqrt N
    return std_dev(samples, False) / math.sqrt(len(samples))


def coefficient_of_variation(samples):
    """
    Computes the coefficient of variation.
    Assumes that the given list is a population.
    :param samples: A non-empty list of numerical values.
    :return: Returns the coefficient of variation.
    """
    # Formula: std_dev of the population / sqrt N
    return std_dev(samples) / math.sqrt(len(samples))
'''


def statistical_summary(samples, population=True):
    print('Mean', mean(samples))
    print('Mode', mode(samples))
    print('Median', median(samples))
    if population:
        print('Variance (Population)', variance(samples))
        print('StDev (Population)', std_dev(samples))
        # print('Coefficient of Variation', coefficient_of_variation(samples))
    else:
        print('Variance (Sample)', variance(samples, False))
        print('StDev (Sample)', std_dev(samples, False))
        # print('StdErr from the Mean', std_error_from_mean(samples))
    print('Min', min(samples))
    print('Max', max(samples))
