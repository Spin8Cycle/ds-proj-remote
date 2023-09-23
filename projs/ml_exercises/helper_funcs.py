import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_single_digit(img, x=28, y=28):
    """Plot image data"""

    img = img.reshape(x, y)
    plt.imshow(img, cmap="binary")
    plt.axis("off")


def plot_multiple_digits(feature, sample_size=100, figsize=(9, 9)):
    plt.figure(figsize=figsize)
    for idx, img in enumerate(feature[:sample_size]):
        plt.subplot(10, 10, idx + 1)
        plot_single_digit(img)
    plt.subplots_adjust(wspace=0, hspace=0)
