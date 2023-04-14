# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:40:25 2019

@author: Kerri Norton
"""

# -*- coding: utf-8 -*-

import pylab
from math import sqrt

# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
# pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers, e.g., circles representing points
# set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1


def getData(fileName, reduced=False):
    dataFile = open(fileName, 'r')
    x = []
    trials = [[], [], [], []]
    dataFile.readline()
    for line in dataFile:
        values = line.split()
        x.append(float(values[0]))
        for i in range(1, len(values)):
            trials[i - 1].append(float(values[i]))
    dataFile.close()
    # if reduced:
    #     amt_remove = 6
    #     y = y[: len(y) - 6]
    #     x = x[: len(x) - 6]
    return (x, trials)


#
#
# masses, distances = getData('springData.txt')
# print('masses: ', masses)
# print('distances: ', distances)


def plotData(inputFile, reduced=False):
    masses, distances = getData(inputFile, reduced)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = masses * 9.81
    pylab.plot(forces, distances, 'bo',
               label='Measured displacements')
    title = 'Measured Displacement of Spring'
    if reduced:
        title += ' Reduced'
    pylab.title(title)
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    pylab.savefig(f'{title.replace(" ", "")}_noline.pdf')
    # pylab.show()


def rSquared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
               predicted a one-dimensional array of predicted values
       Returns coefficient of determination"""
    estimateError = ((predicted - measured) ** 2).sum()
    meanOfMeasured = measured.sum() / len(measured)
    variability = ((measured - meanOfMeasured) ** 2).sum()
    return 1 - estimateError / variability


def fitData(x, y, xLabel, yLabel, title, reduced=False):
    x = pylab.array(x)
    y = pylab.array(y)
    print(x, y)
    pylab.plot(x, y, 'ko', label='Measured displacements')
    if reduced:
        title += ' Reduced'
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    a, b, c = pylab.polyfit(x, y, 2)
    predicted = a * pylab.array(x) * pylab.array(x) + b * pylab.array(x) + c
    k = 1.0 / a
    pylab.plot(x, predicted,
               label='Displacements predicted by\n'
                     'quadratic fit, k = ' + str(round(k, 5)))
    pylab.legend(loc='best')
    # pylab.text(1, .35, f'Line: y={round(a, 3)}x+{round(b, 3)}')
    pylab.savefig(f'{title.replace(" ", "")}.pdf')
    pylab.show()
    # r_squared = rSquared(y, predictedDistances)
    # r = sqrt(r_squared)
    # print('R: ', r)
    # print('R-squared: ', rSquared(y, predictedDistances))


if __name__ == '__main__':
    x, trials = getData('launcherData.txt')
    for i in range(len(trials)):
        y = trials[i]
        fitData(x, y, 'Distance', 'Values', f'Launcher Data Trial {i + 1}')
# fitData('springData.txt', True)

# foot_length = [8.5, 10, 11, 8, 9.5]
# height = [64, 67, 71, 61, 67]
# fitData(foot_length, height)
# plotData('springData.txt', True)
