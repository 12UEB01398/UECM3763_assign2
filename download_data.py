from pandas.io.data import DataReader as DR
from datetime import datetime as dt

import pandas as pd
import pylab as p

start = dt(2012,6,1) #Starting date
end = dt(2015,5,31) # Ending date
data = DR("4197.KL", 'yahoo', start, end) #Use DataReader to read the data of Sime Darby from yahoo!finance
print('3 years of daily data for 4197,Sime Darby')
print(data)

# Plot 5-day moving average for Sime Darby
SD = DR("4197.KL",'yahoo',start,end)['Close'] # Use DataReader to read the close price
moving_avg = pd.rolling_mean(SD,5) #Calculate the moving average
p.plot(moving_avg)
p.xlabel('Days')
p.ylabel('Stock price,$RM$')
p.title('5-days moving average plot for Sime Darby from 1/6/2012 to 31/5/2015')
p.show()   

# Downlaod FTSEKLCI daily data
KLCI = DR("^KLSE",'yahoo',start,end)
print('FTSEKLCI Daily Data')
print(KLCI)

# Combine data of Sime Darby and KLSE
combine = ["4197.KL","^KLSE"]
data1 = DR(combine,'yahoo',start,end)['Close']

# Calcualte correlation between Sime Darby and KLCI
correlation = data1.corr()
print('Correlation between Sime Darby and FTSEKLCI \n',correlation)
