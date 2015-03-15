#!/usr/bin/python
import sys, time
import MySQLdb
from chirp import Chirp

addr = 0x20
chirp = Chirp(1, addr)

print "Moisture: " + chirp.cap_sense() + ", Temperature: " + chirp.temp() + ", Light: " + chirp.light()

db = MySQLdb.connect(host="192.163.248.4" ,
			user="raspisen_raspi",
			passwd="112131",
			db="raspisen_raspi")


cur = db.cursor()

cur.execute("INSERT INTO soil(cap,temp,light) VALUES("+chirp.cap_sense()+","+chirp.temp()+","+chirp.light()+")")
db.commit()

time.sleep(1000)
