from .main import dataExport


def detect_outliers(data):
    """Detect outliers in a dataset using statistical methods."""
    # Implement your outlier detection algorithm here
    pass

def impute_missing_values(data):
    """Impute missing values in a dataset using advanced techniques."""
    # Implement your advanced imputation techniques here
    pass

def feature_scaling(data):
    """Perform feature scaling on numerical features."""
    # Implement your custom feature scaling methods here
    pass

def text_preprocessing(text_data):
    """Preprocess text data for NLP tasks."""
    # Implement your unique text preprocessing techniques here
    pass

def anomaly_detection(data):
    """Detect anomalies in time-series data."""
    # Implement your anomaly detection algorithm here
    pass

def dimensionality_reduction(data):
    """Reduce dimensionality of data using advanced techniques."""
    # Implement your advanced dimensionality reduction methods here
    pass

def cluster_analysis(data):
    """Perform cluster analysis on a dataset."""
    # Implement your custom clustering algorithms here
    pass

def time_series_forecasting(data):
    """Forecast future values in a time-series dataset."""
    # Implement your time series forecasting algorithm here
    pass

def recommendation_system(data):
    """Build a recommendation system using collaborative filtering."""
    # Implement your recommendation system algorithm here
    pass

def network_analysis(graph_data):
    """Analyze networks and graphs for insights."""
    # Implement your network analysis algorithms here
    pass

def topic_modeling(text_data):
    """Extract topics from text data using topic modeling."""
    # Implement your topic modeling algorithm here
    pass

def graph_embedding(graph_data):
    """Embed graphs into lower-dimensional vector spaces."""
    # Implement your graph embedding algorithms here
    pass

def anomaly_explanation(anomaly_data):
    """Explain detected anomalies and their causes."""
    # Implement your anomaly explanation methods here
    pass

def time_series_segmentation(data):
    """Segment time-series data into meaningful patterns."""
    # Implement your time series segmentation algorithm here
    pass

def graph_clustering(graph_data):
    """Cluster nodes in a graph to identify communities."""
    # Implement your graph clustering algorithms here
    pass

def text_summarization(text_data):
    """Generate summaries from text data."""
    # Implement your text summarization algorithms here
    pass

def interpret_ml_models(model, data):
    """Interpret machine learning models to understand predictions."""
    # Implement your model interpretation techniques here
    pass

def feature_importance(data, target):
    """Calculate feature importance for predictive modeling."""
    # Implement your feature importance calculation methods here
    pass

def time_series_similarity(data):
    """Measure similarity between time-series data."""
    # Implement your time series similarity measurement methods here
    pass

def graph_similarity(graph_data):
    """Measure similarity between graphs."""
    # Implement your graph similarity measurement methods here
    pass



"""
NumPy  for data science
=====

Provides
  1. An array object of arbitrary homogeneous items
  2. Fast mathematical operations over arrays
  3. Linear Algebra, Fourier Transforms, Random Number Generation

How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the NumPy homepage <https://numpy.org>`_.

We recommend exploring the docstrings using
`IPython <https://ipython.org>`_, an advanced Python shell with
TAB-completion and introspection capabilities.  See below for further
instructions.

The docstring examples assume that `numpy` has been imported as ``np``::

  >>> import numpy as np

Code snippets are indicated by three greater-than signs::

  >>> x = 42
  >>> x = x + 1

Use the built-in ``help`` function to view a function's docstring::

  >>> help(np.sort)
  ... # doctest: +SKIP

For some objects, ``np.info(obj)`` may provide additional help.  This is
particularly true if you see the line "Help on ufunc object:" at the top
of the help() page.  Ufuncs are implemented in C, not Python, for speed.
The native Python help() does not know how to view their help, but our
np.info() function does.

To search for documents containing a keyword, do::

  >>> np.lookfor('keyword')
  ... # doctest: +SKIP

General-purpose documents like a glossary and help on the basic concepts
of numpy are available under the ``doc`` sub-module::

  >>> from numpy import doc
  >>> help(doc)
  ... # doctest: +SKIP

Available subpackages
---------------------
lib
    Basic functions used by several sub-packages.
random
    Core Random Tools
linalg
    Core Linear Algebra Tools
fft
    Core FFT routines
polynomial
    Polynomial tools
testing
    NumPy testing tools
distutils
    Enhancements to distutils with support for
    Fortran compilers support and more  (for Python <= 3.11).

Utilities
---------
test
    Run numpy unittests
show_config
    Show numpy build configuration
matlib
    Make everything matrices.
__version__
    NumPy version string

Viewing documentation using IPython
-----------------------------------

-----------------------------------
### 1
```
import pandas as pd
import math

# Read dataset from CSV file
# [181.2531410377505, 166.41004448430627, 182.2060809704614]
df = pd.read_csv('/content/descriptive_and_inferential_statistics.csv') 

# Assuming your dataset has a column named 'values'
numbers = df['Height'].tolist()
print(numbers)

# Calculate Mean
mean = sum(numbers) / len(numbers)

# Calculate Median
def calculate_median(numbers):
    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)
    if n % 2 == 0:
        median = (numbers_sorted[n // 2 - 1] + numbers_sorted[n // 2]) / 2
    else:
        median = numbers_sorted[n // 2]
    return median

median = calculate_median(numbers)

# Calculate Mode
def calculate_mode(numbers):
    freq_dict = {}
    for num in numbers:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    mode = max(freq_dict, key=freq_dict.get)
    return mode

mode = calculate_mode(numbers)

# Calculate Variance
mean_squared_diff = sum((x - mean) ** 2 for x in numbers) / len(numbers)
variance = mean_squared_diff

# Calculate Standard Deviation
standard_deviation = math.sqrt(variance)

print(f"Given data = {numbers}")
print(f"Mean = {mean}")
print(f"Median is = {median}")
print(f"Mode = {mode}")
print(f"Variance = {variance}")
print(f"Standard Deviation = {standard_deviation}")
```
--------------------------------------

## 2
```
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("/content/cars_data.csv")
df.head()

print(df)

print("Size of the data : ", df.shape)

# remove whitespaces
df["CarName"].str.replace(' ', '')
df["fueltype"].str.replace(' ', '')

# Drop irrelavent feat
df = df.drop(["peakrpm"],axis=1)
df.head()

# drop duplicates
print("length Before Removing Duplicates is",len(df))
df1=df.drop_duplicates(subset=df.columns[1:])
print("length After Removing Duplicates is",len(df1))

# fill missing values
print("length Before Filling Missing Values is",len(df1))
df1.fillna(0)
print("length After Filling Missing Values is",len(df1))

# delete outliers
from scipy import stats
import numpy as np
z = np.abs(stats.zscore(df1['wheelbase']))
print(z)
```


-----------------------------------

## 4

```
import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("/content/customer_shoppingcsv.csv")
# printing the top 10 rows
display(data.head(10))

## Scatter

plt.scatter(data['gender'], data['age'])
# Adding Title to the Plot
plt.title("Scatter Plot")
# Setting the X and Y labels
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()

## Line chart

plt.plot(data['age'])
plt.plot(data['price'])
# Adding Title to the Plot
plt.title("Line Chart")
# Setting the X and Y labels
plt.xlabel('Age')
plt.ylabel('Money Spent')
plt.show()

## Bar chart

plt.bar(data['age'], data['price'])
plt.title("Bar Chart")
# Setting the X and Y labels
plt.xlabel('age')
plt.ylabel('price')
# Adding the legends
plt.show()

## Histogram

plt.hist(data['payment_method'])
plt.title("Histogram")
plt.show()

## box plot

plt.figure(figsize=(8, 6))
plt.boxplot(data['age'])
plt.title('Box Plot')
plt.ylabel('Age')
plt.show()

## bubble chart

plt.figure(figsize=(10, 6))
plt.scatter(data['age'], data['gender'], s=data['price']*10, alpha=0.5)
plt.title('Bubble Chart of Age vs. Annual Income')
plt.xlabel('Age')
plt.ylabel('Annual Income (k$)')
plt.grid(True)
plt.show()
```



---------------------------------------------

## 6
```
import numpy as np
import pandas as pd

# reading data into dataframe
cars_df = pd.read_csv("/content/Cars93.csv")

# printing top 5 rows
cars_df.head()


cars_df['MPG.city'].hist(figsize = (8,10))

Step1 Decide N(Sample Size): N = 50

Step2: Select N point from Datasset

Step3: Calculate mean of sample

Step4: Add the mean to a list

Step5: Step 2,3,4 100 times. (100 means: Sampling Distribution )

Step6: Verify if sampling distribution follows Normal Curve.

len(cars_df['MPG.city'])

index = np.random.randint(0, len(cars_df['MPG.city']), 50)
print(index)
len(index)

sampling_distribution = []

sample1 = cars_df['MPG.city'][index]
print(sample1)
mean1 = sample1.mean()
print(mean1)

sampling_distribution.append(mean1)
sampling_distribution

Central Limit Theorem

sampling_distribution = []
for i in range(500):
  # generate 50 integers indexes between 0:len(series)
  N = 50
  sample_ind = np.random.randint(0,len(cars_df['MPG.city']), N)

  # extract sample of size 50 using indexes generated in prev step
  sample = cars_df['MPG.city'][sample_ind]

  # calculate sample mean
  sample_mean = sample.mean()

  #add sample mean to sampling distribution
  sampling_distribution.append(sample_mean)

print(sampling_distribution)
print(len(sampling_distribution))

pd.Series(sampling_distribution).hist(figsize = (10,6), bins = 20)

We can observe thst sampling distribution is following Bell Curve

**The Central Limit Theorem** states that the sampling distribution of the sample means approaches a normal distribution as the sample size gets larger - no matter what the shape of the population distribution. ​
```

---------------------------------------------

## 7

```
import numpy as np
import pandas as pd
from scipy.stats import chi2

def chi_square_test(observed, expected):
    # Ensure observed and expected are numpy arrays
    observed = np.asarray(observed)
    expected = np.asarray(expected)

    # If observed or expected is 1D, convert them to 2D arrays with one column
    if observed.ndim == 1:
        observed = observed.reshape(-1, 1)
    if expected.ndim == 1:
        expected = expected.reshape(-1, 1)

    # Calculate the Chi-Square statistic
    chi2_stat = np.sum((observed - expected)**2 / expected)

    # Calculate the degrees of freedom
    dof = (observed.shape[0] - 1) * (observed.shape[1] - 1)

    # Calculate the p-value
    p_val = 1 - chi2.cdf(chi2_stat, dof)

    return chi2_stat, p_val, dof

# Read CSV file
df = pd.read_csv('/content/dataofoe.csv')

# Extract observed and expected values
observed = df['observed'].values
expected = df['expected'].values

# Perform chi-square test
chi2_stat, p_val, dof = chi_square_test(observed, expected)

print("Chi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-value: {p_val}")
print(f"Degrees of Freedom: {dof}")

# Set significance level
alpha = 0.05  # You can adjust this as needed

# Determine conclusion based on p-value
if p_val < alpha:
    print("Reject the null hypothesis.")
    print("There is evidence to suggest that observed and expected frequencies are significantly different.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is no significant difference between observed and expected frequencies.")



### Sample starts from here

import numpy as np
import pandas as pd
from scipy.stats import norm

def z_test(sample, population_mean, population_stddev, n):
    # Calculate the sample mean and standard error
    sample_mean = np.mean(sample)
    standard_error = population_stddev / np.sqrt(n)

    # Calculate the Z-statistic
    z_stat = (sample_mean - population_mean) / standard_error

    # Calculate the p-value
    p_val = 2 * (1 - norm.cdf(np.abs(z_stat)))

    return z_stat, p_val

# Example usage:
# sample =  [1.5, 1.6, 1.7, 1.8, 1.9]

sample = [1.65, 1.7, 1.72, 1.68, 1.69, 1.71, 1.73, 1.75, 1.78, 1.68]

population_mean = 1.7  # Replace with the population mean
population_stddev = 0.1  # Replace with the population standard deviation
n = len(sample)
z_stat, p_val = z_test(sample, population_mean, population_stddev, n)
print("Z-test Results:")
print(f"Z-statistic: {z_stat}")
print(f"P-value: {p_val}")


alpha = 0.05

# Output message
print("Z-test Results:")
print(f"Z-score: {z_stat}")
print(f"P-value: {p_val}")

# Determine conclusion based on p-value and significance level
if p_val > alpha:
    print("The p-value is greater than the significance level.")
    print("We fail to reject the null hypothesis.")
    print("There is no significant difference between the sample mean and the population mean at the 5% significance level.")
else:
    print("The p-value is less than or equal to the significance level.")
    print("We reject the null hypothesis.")
    print("There is a significant difference between the sample mean and the population mean at the 5% significance level.")
```


---------------------------------------------


## 8
```
import pandas as pd
import math

# using csv dataset
df = pd.read_csv('/content/Book1.csv')

df = pd.DataFrame(df)
print(df)

# # Assuming your dataset has 'actual' and 'predicted' columns
actual_values = df['actual_values']
predicted_values = df['predicted_values']


# without using dataset
# actual_values = [10, 20, 30, 40, 50]  # Actual #values
# predicted_values = [12, 18, 33, 41, 49]  # Predicted values



# Root Mean Squared Error (RMSE)
def rmse(actual, predicted):
    n = len(actual)
    squared_error = sum((actual[i] - predicted[i]) ** 2 for i in range(n))
    return math.sqrt(squared_error / n)

# Mean Absolute Error (MAE)
def mae(actual, predicted):
    n = len(actual)
    absolute_error = sum(abs(actual[i] - predicted[i]) for i in range(n))
    return absolute_error / n

# Mean Absolute Percentage Error (MAPE)
def mape(actual, predicted):
    n = len(actual)
    percentage_error = sum(abs((actual[i] - predicted[i]) / actual[i]) for i in range(n))
    return (percentage_error / n) * 100

# Mean Squared Error (MSE)
def mse(actual, predicted):
    n = len(actual)
    squared_error = sum((actual[i] - predicted[i]) ** 2 for i in range(n))
    return squared_error / n

# Mean Absolute Scale Error (MASE)
def mase(actual, predicted):
    n = len(actual)
    mae_value = mae(actual, predicted)
    naive_forecast_error = sum(abs(actual[i] - actual[i-1]) for i in range(1, n))
    naive_forecast_error /= (n - 1) if n > 1 else 1  # Adjust for the length of the series
    return mae_value / naive_forecast_error

# Calculate evaluation parameters
rmse_value = rmse(actual_values, predicted_values)
mae_value = mae(actual_values, predicted_values)
mape_value = mape(actual_values, predicted_values)
mse_value = mse(actual_values, predicted_values)
mase_value = mase(actual_values, predicted_values)

# Display evaluation parameters
print("Evaluation Parameters:")
print(f"Root Mean Squared Error (RMSE): {rmse_value:.2f}")
print(f"Mean Absolute Error (MAE): {mae_value:.2f}")
print(f"Mean Absolute Percentage Error (MAPE): {mape_value:.2f}%")
print(f"Mean Squared Error (MSE): {mse_value:.2f}")
print(f"Mean Absolute Scale Error (MASE): {mase_value:.2f}")
```

----------------------------------
## 9
```
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/content/forcastData.csv")
temp = df["temp"]

print(temp)

def moving_average(data, window_size):
    moving_averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        average = sum(window) / window_size
        moving_averages.append(average)
    return moving_averages

# Define window size
window_size = 3

# Calculate moving average
predicted_values = moving_average(temp, window_size)

# Extend the predictions for future values
future_predictions = []
for i in range(window_size - 1):
    future_predictions.append(None)
for i in range(len(temp) - window_size + 1, len(temp)):
    window = temp[i:]
    future_predictions.append(sum(window) / len(window))

# Plot original data, moving average predictions, and future predictions
plt.plot(temp, label='Original Data')
plt.plot(range(window_size - 1, len(temp)), predicted_values, label='Moving Average Predictions')

plt.xlabel('Months')
plt.ylabel('Temperature')
plt.title('Temperature Data and Predictions')
plt.legend()
plt.show()

print("Moving Average Predictions:", predicted_values)
print("Future Predictions:", future_predictions)
```


-----------------------------------

Start IPython and import `numpy` usually under the alias ``np``: `import
numpy as np`.  Then, directly past or use the ``%cpaste`` magic to paste
examples into the shell.  To see which functions are available in `numpy`,
type ``np.<TAB>`` (where ``<TAB>`` refers to the TAB key), or use
``np.*cos*?<ENTER>`` (where ``<ENTER>`` refers to the ENTER key) to narrow
down the list.  To view the docstring for a function, use
``np.cos?<ENTER>`` (to view the docstring) and ``np.cos??<ENTER>`` (to view
the source code).

Copies vs. in-place operation
-----------------------------
Most of the functions in `numpy` return a copy of the array argument
(e.g., `np.sort`).  In-place versions of these functions are often
available as array methods, i.e. ``x = np.array([1,2,3]); x.sort()``.
Exceptions to this rule are documented.

"""

def dataExport():
    return 1