import numpy as np

x = np.array([2, 3, 4, 6, 7, 8])
y = np.array([1, 5, 3, 6, 5, 10])

# Calculate the slope and intercept of the linear regression model
slope, intercept = np.polyfit(x, y, 1)

# Calculate the means of x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate the deviations from the means
x_deviation = x - x_mean
y_deviation = y - y_mean

# Calculate the sum of squares of the deviations
ss_total = np.sum(y_deviation**2)

# Calculate the residuals
residuals = y - (x * slope + intercept)

# Calculate the sum of squares of the residuals
ss_residual = np.sum(residuals**2)

# Calculate the proportion of variance (R-squared)
r_squared = 1 - (ss_residual / ss_total)

print("Proportion of Variance (R-squared):", r_squared)