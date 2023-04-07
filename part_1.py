from readcsv import load_data
import pylab


def plot_scatter(x, y, title, xLabel, yLabel):
    years = [y for y in range(2000, 2010)]
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)

    pylab.scatter(x, y)
    pylab.savefig(f'{title.replace(" ", "")}.pdf')
    pylab.show()


if __name__ == '__main__':
    data = load_data('springData.txt')
    x = [row[0] for row in data]
    y = [row[1] for row in data]

    pass
