# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:40:25 2019

@author: Kerri Norton
"""

# -*- coding: utf-8 -*-

import pylab

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


def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline()
    for line in dataFile:
        d, m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)


masses, distances = getData('springData.txt')
print('masses: ', masses)
print('distances: ', distances)


def plotData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = masses * 9.81
    pylab.plot(forces, distances, 'bo',
               label='Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')


plotData('springData.txt')


def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    forces = pylab.array(masses) * 9.81
    pylab.plot(forces, distances, 'ko',
               label='Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    a, b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a * pylab.array(forces) + b
    k = 1.0 / a
    pylab.plot(forces, predictedDistances,
               label='Displacements predicted by\nlinear fit, k = '
                     + str(round(k, 5)))
    pylab.legend(loc='best')
    print('R-squared: ', rSquared(distances, predictedDistances))


fitData('springData.txt')


def rSquared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
               predicted a one-dimensional array of predicted values
       Returns coefficient of determination"""
    estimateError = ((predicted - measured) ** 2).sum()
    meanOfMeasured = measured.sum() / len(measured)
    variability = ((measured - meanOfMeasured) ** 2).sum()
    return 1 - estimateError / variability
