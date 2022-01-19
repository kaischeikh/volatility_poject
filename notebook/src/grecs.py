from sys import flags
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from tqdm.auto import tqdm
from pathlib import Path


def compute_theta(
    df: pd.DataFrame,
    col_name: str = "ouv",
) -> pd.Series:
    """
        compute theta based on dataframe df.
    """
    theta = df[col_name].diff()[1:]
    delta_t = (df.index[1:] -  df.index[:-1]).days
    delta_t = delta_t.map({1:1, 3:1})

    return theta / delta_t
