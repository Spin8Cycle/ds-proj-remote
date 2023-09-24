import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import shift


def custom_info(df):
    info_df = pd.DataFrame(
        index=df.columns,
        columns=[
            "Data Type",
            "Non-Null Count",
            "Null Count",
            "% Missing",
            "Distinct Values",
        ],
    )

    for i in info_df.index:
        info_df.loc[i, "Data Type"] = df[i].dtype
        info_df.loc[i, "Non-Null Count"] = df[i].value_counts().sum()
        info_df.loc[i, "Null Count"] = df[i].isnull().sum()
        info_df.loc[i, "% Missing"] = round((df[i].isnull().sum() / len(df)) * 100, 2)
        info_df.loc[i, "Distinct Values"] = df[i].nunique()

    return info_df


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


def image_shift(img, dx, dy):
    image = img.reshape((28, 28))
    shifted_image = shift(image, [dy, dx], cval=0, mode="constant")
    return shifted_image.reshape([-1])
