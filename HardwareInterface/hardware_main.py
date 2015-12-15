#!/usr/bin/env python

import collections, pika, sys
if sys.path[0] != '../Controller': sys.path.insert(0, '../Controller')
import controller

class VRHardware():
	
	def __init__(self):	
		self.controller = None
	
		#TODO any way to make this constant?	
		self.LEAP_ID = 1
		self.MYO_ID = 2
		self.KINECT_ID = 3
		self.TABLET_ID = 4
	
		# variables used for Leap control		
		self.cache = collections.deque(list(), 200)
		self.called_press = False	

		# initialize RabbitMq communication		
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		self.channel = connection.channel()
		self.channel.queue_declare(queue='hello')
		
		print ' [*] Waiting for messages. To exit please press CTRL+C'
		# user_id:position_x,position_y,position_z:hand_type:gesture

		self.channel.basic_consume(callback, queue='hello', no_ack=True)
		self.channel.start_consuming()


	def callback(ch, method, properties, body):
		if body:
			#split the body string
			bodyParts = body.split(':')
			user_id = bodyParts[0]
			pos = bodyParts[1]
			hand_type = bodyParts[2]
			gesture = bodyParts[3]
			
			is_left = False
			if hand_type == 'L':
				is_left = True
	
			# LEAP
			if user_id.startswith(LEAP_ID):
				
				# MOVE
				move(pos, user_id, is_left)
	
				# Store the last 200 frames
				self.cache.append(gesture)
	
				# PRESS
				if gesture == "grab":
					self.called_press = True
					press(pos, user_id, is_left)
	
				# RELEASE
				# If press() has been called but released() has not been called yet and the current gesture does not equal 	grab
				elif called_press:
					release(pos, user_id, is_left)
					self.called_press = False
	
	
				# ZOOM
				elif gesture == "circle_clockwise" or gesture == "circle_counterclockwise":
					# Iterate over last n gestures
					false_alarm = False
					n = 10 #TODO probably too small for leap
					for element in self.cache[-n:]:
						# If the circle does not occur at least n times in a row, it will be interpreted as false 	alarm
						if element != gesture:
							false_alarm = True
	
					if not false_alarm:
						if gesture == "circle_clockwise":
							zoom(1)
						elif gesture == "circle_counterclockwise":
							zoom(-1)
	
			# MYO
			elif id.startswith(MYO_ID):
				# myo has some additional info
				posSplit = pos.split(";")
				box = posSplit[1]
				rot = posSplit[2]			
				pos = posSplit[0] #x,y,z
				
				
				gesSplit = gesture.split(";")
				edge = gesSplit[1]
				gesture = gesSplit[0]
	
				# MOVE
				#TODO normalize position on 0, 1 -> in myo client
				move(pos, user_id, is_left)
	
				#PRESS
				if gesture == "fist" and edge == "on":
					press(pos, user_id, is_left)
	
				elif gesture == "fist" and edge == "off":
					release(pos, user_id, is_left)
				
				#ZOOM
				elif gesture == "fingersSpread":
					#TODO figure out how quaternions work on myo
					if rotX > 0:
						rot(1)
					else:
						rot(-1)	
				
	

