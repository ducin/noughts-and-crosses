#!/usr/bin/python

import config
import game
import socket

s = socket.socket()
s.bind((config.host, config.port))
s.listen(5)

print 'Server started!'
print 'Waiting for clients...'

c, addr = s.accept()
print 'Got connection from', addr
msg = ''
while msg != 'exit':
	msg = c.recv(1024)
	print addr, ' >> ', msg
	msg = raw_input(game.server_label)
	c.send(msg);
c.close()
print 'Connection closed'
