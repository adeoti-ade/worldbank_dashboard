import wbdata
import pandas as pd
import matplotlib.pyplot as plt

# set up the countries I want
countries = ["CL", "UY", "HU"]

"""set up the indicator I want
(just build up the dict if you want more than one)
"""
indicators = {'NY.GNP.PCAP.CD': 'GNI per Capita'}

# grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)

"""df is "pivoted", pandas' unstack fucntion helps
reshape it into something plottable
"""
dfu = df.unstack(level=0)

# a simple matplotlib plot with legend, labels and a title
dfu.plot()
plt.legend(loc='best')
plt.title("GNI Per Capita ($USD, Atlas Method)")
plt.xlabel('Date')
plt.ylabel('GNI Per Capita ($USD, Atlas Method')
