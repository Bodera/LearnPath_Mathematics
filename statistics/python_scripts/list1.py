# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# storing the raw data into a pd.Series
ages_series = pd.Series([  0,  1,  1,  1,  2,  2,  2,  3,  3,  4,  4,
                    4,  5,  5,  5,  6,  6,  6,  6,  7,  7,  8,
                    8,  9,  10,  10,  10,  11,  11,  11,  12,  12,  13,
                    15,  16,  16,  17,  17,  21,  21,  22,  23,  24,  25,
                    25,  26,  27,  27,  28,  28,  29,  30,  31,  31,  32,
                    32,  33,  33,  34,  36,  39,  41,  42,  45,  46,  47,
                    48,  49,  50,  50,  51,  52,  53,  54,  55,  56,  63]
                    )

print(ages_series)

# creating the frequency distribution table
frq_dist = {'Midpoint (x^)': [5.5, 16.5, 27.5, 38.5, 49.5, 60.5],
            'Age (x)': ['0|---11', '11|---22', '22|---33', '33|---44', '44|---55', '55|---66'],
            'Absolute frequency (f)': [27, 13, 16, 7, 11, 3],
            'Cumulative frequency (F)': [27, 40, 56, 63, 74, 77]
           }

frq_dist_frame = pd.DataFrame(data=frq_dist)
print(frq_dist_frame)

# plotting the frequency distribution histogram

plt.bar(frq_dist_frame['Age (x)'], frq_dist_frame['Absolute frequency (f)'],
        width=1.0, linewidth=2.0, edgecolor='#781955')
plt.title('Frequency distribution histogram')

plt.show()
