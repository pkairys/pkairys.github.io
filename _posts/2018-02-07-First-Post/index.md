---
layout: default
description: "An initial post with some dummy code to test the post generation"
date: 2018-02-08
title: First Post
---

# This is an inital test post
Here I will make some plots to make sure that the site works. 


```python
# Imports
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
```

## KDE plots


```python
# Using a seaborn cubehelix kde example
sns.set(style="dark")
rs = np.random.RandomState(50)

# Set up the matplotlib figure
f, axes = plt.subplots(3, 3, figsize=(9, 9), sharex=True, sharey=True)

# Rotate the starting point around the cubehelix hue circle
for ax, s in zip(axes.flat, np.linspace(0, 3, 10)):

    # Create a cubehelix colormap to use with kdeplot
    cmap = sns.cubehelix_palette(start=s, light=1, as_cmap=True)

    # Generate and plot a random bivariate dataset
    x, y = rs.randn(2, 50)
    sns.kdeplot(x, y, cmap=cmap, shade=True, cut=5, ax=ax)
    ax.set(xlim=(-3, 3), ylim=(-3, 3))

f.tight_layout()
```


![png]({{ "/assets/2018-02-07-First-Post/First-Post_files/First-Post_3_0.png" | absolute_url }})


## Timeseries plots


```python
# Using seaborn timeseries example
gammas = sns.load_dataset("gammas")

# Plot the response with standard error
sns.tsplot(data=gammas, time="timepoint", unit="subject",
           condition="ROI", value="BOLD signal")
fig = plt.gcf()
fig.set_size_inches(8,8)
```


![png]({{ "/assets/2018-02-07-First-Post/First-Post_files/First-Post_5_0.png" | absolute_url }})


This is hopefully a successful post. :)
