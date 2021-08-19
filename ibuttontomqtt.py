#!/usr/bin/python
###########################################
# RasbperryPi KeyTag iButton read to MQTT #
# Author : JmmyGun                        #
# Date   : 19/08/2021                     #
###########################################

import time
import os
import RPi.GPIO as GPIO
from paho.mqtt import client as mqtt_client

broker = '127.0.0.1'
port = 1883
topic = "ibutton"
client_id ='ibutton'
#uncomment the following 2 lines for set your "username" and "password"
#username = 'YOUR_USER'
#password = 'YOUR_PASS'

os.system('modprobe wire timeout=1 slave_ttl=5')

os.system('modprobe w1-gpio')
os.system('modprobe w1-smem')

os.system('chmod a+w /sys/devices/w1_bus_master1/w1_master_slaves')
os.system('chmod a+w /sys/devices/w1_bus_master1/w1_master_remove')
os.system('chmod a+w /sys/devices/w1_bus_master1/w1_master_search')

base_dir = '/sys/devices/w1_bus_master1/w1_master_slaves'
delete_dir = '/sys/devices/w1_bus_master1/w1_master_remove'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #uncomment the following line if you set "username" and "password"
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):

  while True:

    # Probe read
    dir = open(base_dir, "r")
    TAG = dir.read()
    dir.close()
    if TAG != 'not found.\n':
        print(TAG)
        msg = (TAG)
        client.publish(topic, msg)
        act = open(delete_dir, "w")
        act.write(TAG)
    else:
        time.sleep(0.001)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':

  try:
    run()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
