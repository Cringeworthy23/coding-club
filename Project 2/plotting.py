from audioop import mul
import matplotlib.pyplot as plt

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]




def single_plot_plotting():
    # Classic connect-the-dots plot
    plt.plot(list1, list2, ':', 'r')

    # Args for plot: 
    """
    linewidth = 1
    '-' = solid line
    '--' = dashed line
    '-.' = dash-dot line
    ':' = dotted line
    color: 
    'b' = blue
    'g' = green
    'r' = red
    'c' = cyan
    'm' = magenta
    'y' = yellow
    'k' = black
    'w' = white
    ALSO accepts hex colors

    ALSO accepts np.array(), pandas dataframe, etc.

    Markers:
    '.' = point
    ',' = pixel
    'o' = circle
    'v' = triangle down
    '^' = triangle up
    '<' = triangle left
    '>' = triangle right
    '1' = triangle down
    '2' = triangle up
    '3' = triangle left
    '4' = triangle right
    's' = square
    'p' = pentagon
    '*' = star
    'h' = hexagon
    'H' = hexagon
    '+' = plus
    'x' = x
    'D' = diamond
    'd' = thin_diamond
    '|' = vertical line
    '_' = horizontal line
    """
    # plt.scatter() will plot a scatterplot
    # plt.bar() will plot a bar chart

    # BETWEEN EVERY LINE, RUN plt.show() TO SEE THE PLOT
    plt.ylabel('list2')
    plt.xlabel('list1')

    # xleft, xright, ybottom, ytop
    plt.axis([0, 10, 0, 10])
    plt.show()


def multi_plot():
    # Plotting multiple different charts
    plt.subplot(131)
    plt.plot(list1, list2)
    plt.subplot(132)
    plt.scatter(list1, list2)
    plt.subplot(133)
    plt.bar(list1, list2)
    plt.suptitle('Multiple Plots')
    plt.show()


single_plot_plotting()