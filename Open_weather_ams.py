##### A python script to download data from OpenWeatherMap and show live data using Matplotlib.

import time
import requests
from pprint import pprint
import matplotlib.pyplot as plt
from datetime import datetime

###########  Settings  ############
plt.rcParams['animation.html'] ='jshtml'

settings = {
    'api_key':"ac37f4337bdc07b0642d027ee1313660",
    'city':'Amsterdam',
    'temp_unit':'metric'} #unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&q={1}&units={2}"

###########  Define the plot and subplots  ############
fig = plt.figure()
plt.title('Weerdata Amsterdam')

ax1 = fig.add_subplot(211) #upper figure
ax2 = fig.add_subplot(212) # lover figure
fig.show()

i =0
x,y1,y2 = [],[],[]


###########  Run the script to draw the graphs  ############
while True:
    final_url = BASE_URL.format(settings["api_key"],settings["city"],settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    #pprint(weather_data)
    temperature = weather_data['main']['temp']
    pressure = weather_data['main']['pressure']
    pressure_kwik = pressure /13,3322 #  1 mmHg = 133,322 Pa =   13,3322 millibar  (1 Pa = 0,01 millibar)
    unix_tijd = weather_data['dt']
    tijd= datetime.fromtimestamp(unix_tijd)
    x.append(i)
    y1.append(temperature)
    y2.append(pressure)
    
    ax1.plot(x,y1, 'bo:')
    ax2.plot(x,y2, 'ro:')
    fig.canvas.draw()
    
    #print(tijd, temperature)
    #plt.plot(tijd, temperature)
    time.sleep(60) #get new data every minute seconds
    i += 1
