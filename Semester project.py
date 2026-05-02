import BTC_Data as bd
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from matplotlib.animation import FuncAnimation

#style
plt.style.use('seaborn-v0_8')

#x: datetime y: price
x_vals = []
y_vals = []

#animate function
def animate(i):
    x_vals.append(datetime.now())
    y_vals.append(bd.get_btc_price())

    #titles
    plt.title('Bitcoin Price Live Plotting')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')

    #plotting
    plt.plot(x_vals,y_vals, linestyle='solid', ms=0)
    plt.tight_layout()

#call animate function
animate= FuncAnimation(plt.gcf(),animate,interval=1000)

#show plot
plt.show()