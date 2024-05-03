
## HIgher National Diploma in Science in Computing (Data Analytics)
## Principles of Data Analytics (8634: 2024-2024)
## Project Title: Analysis of the Palmer Archipelago Penguins Dataset with Python
### Author: Ebelechukwu Chidimma Igwagu


### Project Description

This repository contains my analysis of the popular [Palmer Archipelago penguins dataset](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv).  This project demonstrated analytical tools and processes involved in sourcing, investigating, exploring and visualizing data to provide valuable insights. All analysis was performed with the Anaconda (Python 3.11.5) interprter.

### Overview
The [Palmer penguins dataset](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv) is a popular dataset that is made available by [Dr Kirsten Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php) and the [Palmer Station Antarctica Long term ecological research network](https://pallter.marine.rutgers.edu/). Seven measurements from 344 male and female penguins make up this dataset and every row represent an individual penguin. The dataset's three species of penguins reside on three different islands. The penguin species, Adelie, Gentoo, and Chinstrap are found in the Biscoe, Dream, and Torgerson Islands in the Palmer Archipelago, Antarctica. the measured variables were species, island, sex, bill length, bill depth, flipper length and body mass. The dataset can be accessed [here](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv) and was analysed using python.


### Installation
- Clone the URL [here](https://github.com/Gtalen/data-analytics.git).

```
- Install Anaconda python Interpreter

- Install Visual studio code

```
### USAGE

### Libraries/Prerequisites


The libraries used for this project Pandas, Numpy, matplotlib_pyplot, Seaborn and Sciplot.stats and these packages are available on the Anaconda installation package. Any additional package can be installed using pip install. Pandas was used for exploring the dataframe, Numpy - numerical arrays was utilized for data analysis while Matplotlib and seaborn was used for plotting data. These can be imported into the jupyter notebook with the command below;

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
```

### Loading the dataset

Once the prerequisites are installed and dependencies imported, the dataset can be accessed [here](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv).

```
# Importing the raw data 

palmer_penguins = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
palmer_penguins

```
### Statistical Models
Follow along with the project and you will be able to test all of the models;

1 **Descriptivee statistics**
- Barcharts
- Histograms 
- Boxplot:

2 **Correlation Analysis**  
-  Scatterplots
- Heatmap correlation matrix
- Pairplots

3 **Regression Analysis

### Analysis Steps 
Basic analysis applied

- Data Exploration
- Data Manipulation
- Data Visualization
- Statistical testing
- Data findings 


 ### Conclusion
The Palmer penguin dataset was used to demonstrate how raw data can be sourced, explored, manipulated, modelled and visulaized in  order to provide meaningful insights. 


### Contributors
- Ebelechukwu Chidimma Igwagu

- Eager to contribute? his project is open to external contribution.

### License
This project is available under the MIT, GNU license.

