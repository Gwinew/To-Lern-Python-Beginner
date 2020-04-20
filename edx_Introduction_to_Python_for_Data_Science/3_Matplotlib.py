# Data Visualization
#
# - Very import in data analysis
#   - Explore data
#   - Report insights

import matplotlib.pyplot as plt

year = [1958, 1970, 1990, 2010]

pop = [2.519, 3.692, 5.263, 6.972]

#plt.plot(year, pop)            # If we added this syntax than get a line between points
#plt.show()


# Scatter plot
plt.scatter(year, pop)
plt.show()



## Histogram

# - Explore dataset
# - Get idea about distribution

import matplotlib.pyplot as plt

# help(plt.hist)

values = [9,8.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins=3)
plt.show()

#
# Data Visualization
#
# - Science & Art
# - Many options
#   - Different plot types
#   - Many costumizations
# - Chioce depends on:
#   - Data
#   - Story you want to tell

import matplotlib.pyplot as plt

year = [1958, 1970, 1990, 2010]

pop = [2.519, 3.692, 5.263, 6.972]
year = [1800,1858,1900]+year
pop=[1.8,1.262,1.650]+pop

#plt.plot(year, pop)

plt.fill_between(year,pop, 0,color='green')

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Pupulation Projections')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B', '8B', '10B'])

plt.show()
