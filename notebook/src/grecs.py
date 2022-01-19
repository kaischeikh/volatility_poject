from sys import flags
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from tqdm.auto import tqdm
from pathlib import Path


def compute_alpha(a: float) -> float:
    return a + 1