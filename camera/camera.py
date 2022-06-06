#!/usr/bin/python3
import picamera
import time
import config

def take_picture(file_datetime):
	picturepath=config.picture_path + file_datetime + ".jpg"
	cam = picamera.PiCamera()
	cam.capture(picturepath) 
	return picturepath
