import numpy as np
import time
import matplotlib.pyplot as plt
from numba import jit

# standard python sum function
@jit
def sum_python(arr):
    result = 0
    for num in arr:
        result += num
    return result

#numpy sum function
def sum_numpy(arr):
    return np.sum(arr)

# Array sizes from 10 to 100,000,000
array_sizes = [10**i for i in range(1, 9)] 
python_times = []
numpy_times = []

for size in array_sizes:
    arr = np.random.rand(size)

    # Standard python 
    start_time = time.perf_counter()
    sum_python(arr)
    python_time = time.perf_counter() - start_time
    python_times.append(python_time)

    # numpy
    start_time = time.perf_counter()
    sum_numpy(arr)
    numpy_time = time.perf_counter() - start_time
    numpy_times.append(numpy_time)


# Plotting:

# Chart colours from the Catppuccin Mocha Colour Palette
background_color = '#1e1e2e'# Dark background
text_color = '#cdd6f4'      # Text for text
axes_color = '#f2cdcd'      # Flamingo for axes  
numpy_color = '#fab387'     # Peach for NumPy
python_color = '#f38ba8'    # Red for Python

plt.figure(figsize=(6, 10), facecolor=background_color)
plt.rcParams['axes.facecolor'] = background_color

plt.plot(array_sizes, python_times, marker='o', color=python_color, label='Python')
plt.plot(array_sizes, numpy_times, marker='s', color=numpy_color, label='NumPy')

# Set scales
plt.xscale('log')
plt.yscale('log')

# Axis labels
plt.xlabel('Array Size', fontsize=12, color=text_color)
plt.ylabel('Time (seconds)', fontsize=12, color=text_color)
plt.title('Performance Comparison: NumPy vs JIT Python', fontsize=14, color=text_color)

# Annotations
for i, size in enumerate(array_sizes):
    plt.text(size, python_times[i], f'{python_times[i]:.2e}', fontsize=12, ha='right', va='bottom', color=python_color)
    plt.text(size, numpy_times[i], f'{numpy_times[i]:.2e}', fontsize=12, ha='right', va='top', color=numpy_color)

# Annotate where the two switch
plt.annotate('Switching Point', xy=(array_sizes[3], python_times[3]), xytext=(array_sizes[3], python_times[3]*10),
             arrowprops=dict(facecolor=text_color, shrink=0.05), fontsize=10, ha='center', color=text_color)

# Legend
legend = plt.legend(fontsize=12, loc='upper center')
for text in legend.get_texts():
    text.set_color(text_color)

#Set chart outline or "spine" colours
plt.gca().spines['bottom'].set_color(axes_color)
plt.gca().spines['left'].set_color(axes_color)
plt.gca().spines['top'].set_color(axes_color)
plt.gca().spines['right'].set_color(axes_color)

plt.tick_params(axis='x', colors=axes_color)
plt.tick_params(axis='y', colors=axes_color)

# Save the plot
plt.tight_layout()
plt.savefig('numpy_vs_jit.png')
plt.close() 