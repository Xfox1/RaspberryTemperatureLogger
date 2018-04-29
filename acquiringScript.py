import Adafruit_DHT
import time
import datetime
import configparser
import sqlite3
#import sys

#sys.path.append("./configuration")
#import databaseManager

from configuration.databaseManager import DBM

print "Script running..."

config = configparser.ConfigParser()
config.read("./configuration/configuration.cfg");

DBM = DBM(config['defaultConfiguration']['DBName']) #passing DB Name


if(not DBM.dbExists()):
	DBM.createDB()

while True:
	#Acquiring variable
	now = datetime.datetime.now()
	hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

	print "[%s] Temp: %.1f \tHumidity: %.1f" % (now.strftime("%Y-%m-%d %H:%M:%S"), temp, hum)

	DBM.insertRecord(temp, hum, int(time.time()))
	time.sleep(int(config['defaultConfiguration']['interval']) * 60)