#!/usr/bin/python

import config
import game
import socket

print 'Connecting to ', config.host, config.port
s = socket.socket()
s.connect((config.host, config.port))

msg = ''
while msg != 'exit':
	msg = raw_input(game.client_label)
	s.send(msg)
	msg = s.recv(1024)
	print game.server_label, msg
s.close
print 'Connection closed'
