# Raspberry-Pi-iButton-key-tag-to-mqtt

Python script for read and publish via MQTT the keytag of iButton DS1990A, DS1985-F5+, DS1971+F5 with OneWire BUS of the Raspberry Pi

![IMG_20210819_020156_1](https://user-images.githubusercontent.com/36232136/129987418-19666668-17d4-4b4a-b78a-11c0cbee3886.jpg)

![IMG_20210819_020208](https://user-images.githubusercontent.com/36232136/129987502-d426c512-4ee0-4e40-aae3-fb69e1d0ab9f.jpg)


When using long wires (200mt max), and 3.3V power, a pullup resistor in the 1K to 2.7K range may be required. Check the diagram

![circuit](https://user-images.githubusercontent.com/36232136/129983994-c69dcd84-fa48-4b4c-aa10-7e9862c1820b.png)


First of all, update Raspbian. At boot, the OneWire BUS is disabled by default. To enable it, use “Raspberry Pi Configuration”. 
This is found under : Menu > Preferences > Raspberry Pi Configuration, and reboot.

![1](https://user-images.githubusercontent.com/36232136/129983373-c948e120-e51e-40f5-bd15-20c02da70d78.png)

![2](https://user-images.githubusercontent.com/36232136/129983798-757d4a81-8559-455d-bfa1-500a8cc023b6.png)

![3](https://user-images.githubusercontent.com/36232136/129983830-f61e5b6c-1115-4244-bc7f-b37de963cfb7.png)

![4](https://user-images.githubusercontent.com/36232136/129983842-1b9d6235-6d6a-4b07-bb09-4fdeb910bc7c.png)

This script require `eclipse/mosquitto`, and `eclipse/paho.mqtt.python`.

To install the required components, follow the instructions in the links below:

  * [eclipse/mosquitto](https://github.com/eclipse/mosquitto)
  * [eclipse/paho.mqtt.python](https://github.com/eclipse/paho.mqtt.python) 


This script can run only with `sudo`

  `sudo python ibuttontomqtt.py`
