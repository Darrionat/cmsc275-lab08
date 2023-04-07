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
pylab.rcParams['xtick.labelsize'] = 16
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
    distances = []
    masses = []
    dataFile.readline()
    for line in dataFile:
        d, m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    if reduced:
        amt_remove = 6
        masses = masses[: len(masses) - 6]
        distances = distances[: len(distances) - 6]
    return (masses, distances)


masses, distances = getData('springData.txt')
print('masses: ', masses)
print('distances: ', distances)


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


def fitData(inputFile, reduced=False):
    masses, distances = getData(inputFile, reduced)
    distances = pylab.array(distances)
    forces = pylab.array(masses) * 9.81
    pylab.plot(forces, distances, 'ko',
               label='Measured displacements')
    title = 'Measured Displacement of Spring'
    if reduced:
        title += ' Reduced'
    pylab.title(title)
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    a, b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a * pylab.array(forces) + b
    k = 1.0 / a
    pylab.plot(forces, predictedDistances,
               label='Displacements predicted by\n'
                     'linear fit, k = ' + str(round(k, 5)))
    pylab.legend(loc='best')
    pylab.text(1, .35, f'Line: y={round(a, 3)}x+{round(b, 3)}')
    # pylab.text(1, .3, f'r: y={round(a, 3)}x+{round(b, 3)}')
    pylab.savefig(f'{title.replace(" ", "")}.pdf')
    pylab.show()
    r_squared = rSquared(distances, predictedDistances)
    r = sqrt(r_squared)
    print('R: ', r)
    print('R-squared: ', rSquared(distances, predictedDistances))


if __name__ == '__main__':
    fitData('springData.txt', True)
    plotData('springData.txt', True)
