from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

temp = sensor.get_temperature()

print("Hello Margotku. The temperature is: "
      + str(temp) + " Have a great day ;) ")
