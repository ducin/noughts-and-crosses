#!/usr/bin/python

import socket
import config
from game import Game

s = socket.socket()
s.bind((config.host, config.port))
s.listen(5)

print 'Noughts and crosses, v1.0'
print 'Server started! Waiting for clients...'

c, addr = s.accept()
print 'Got connection from', addr

game = Game()
game.display()
while game.continues():
	my_move = raw_input('Your move: ')
	while not game.set(int(my_move)):
		print 'This field cannot be marked.'
		my_move = raw_input('Your move: ')
	game.display()
	c.send(my_move)
	if not game.continues():
		break
	print 'Waiting for opponent move'
	his_move = c.recv(1024)
	print 'Opponent >> ', his_move
	game.set(int(his_move))
	game.display()
print game.winner if game.winner else 'Nobody', 'has won!'
c.close()
print 'Connection closed'
