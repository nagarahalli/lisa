#!/usr/bin/python
"""Small functions to help with plots"""

from matplotlib import pyplot as plt

GOLDEN_RATIO = 1.618034

def set_plot_size(width, height):
    """Set the plot size.

    This has to be called before calls to .plot()
    """
    if height is None:
        if width is None:
            height = 6
            width = 10
        else:
            height = width / GOLDEN_RATIO
    else:
        if width is None:
            width = height * GOLDEN_RATIO

    plt.figure(figsize=(width, height))

def normalize_title(title, opt_title):
    """
    Return a string with that contains the title and opt_title if it's not the empty string

    See test_normalize_title() for usage
    """
    if opt_title is not "":
        title = opt_title + " - " + title

    return title

def pre_plot_setup(width=None, height=None):
    """initialize a figure

    width and height are numbers, ylim is a tuple with min and max
    values for the y axis.  This function should be called before
    any calls to plot()
    """

    set_plot_size(width, height)

    _, ax = plt.subplots()

    return ax

def post_plot_setup(ax, title="", xlabel=None, xlim=None, ylim=None):
    """Set xlabel, title, xlim adn ylim of the plot

    This has to be called after calls to .plot()
    """

    if xlabel is None:
        xlabel = "Time"
    plt.xlabel(xlabel)

    if title:
        plt.title(title)

    if not ylim:
        cur_ylim = ax.get_ylim()
        ylim = (cur_ylim[0] - 0.1 * (cur_ylim[1] - cur_ylim[0]),
                cur_ylim[1] + 0.1 * (cur_ylim[1] - cur_ylim[0]))

    ax.set_ylim(ylim[0], ylim[1])

    if xlim:
        ax.set_xlim(xlim[0], xlim[1])

def plot_allfreqs(in_power, out_power, map_label, title="", width=None, height=None):
    """Do allfreqs plots similar to those of CompareRuns"""
    import power

    all_freqs = power.get_all_freqs_data(in_power, out_power, map_label)

    for label, dfr in all_freqs.iteritems():
        this_title = normalize_title("allfreqs " + label, title)

        ax = pre_plot_setup(width=width, height=height)
        dfr.plot(ax=ax)
        post_plot_setup(ax, title=this_title)
