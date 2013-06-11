#!/usr/bin/python

import socket
import sys

import config
from game import Game

def main(args):
	print 'Noughts and crosses, v1.0'
	print 'Connecting to', config.host, config.port
	s = socket.socket()
	try:
		s.connect((config.host, config.port))

		game = Game()
		game.display()
		while game.continues():
			print 'Waiting for opponent move'
			his_move = s.recv(1)
			print 'Opponent >>', his_move
			game.set(int(his_move))
			game.display()
			if not game.continues():
				break
			my_move = raw_input('Your move: ')
			while not game.set(int(my_move)):
				'This field cannot be marked.'
				my_move = raw_input('Your move: ')
			game.display()
			s.send(my_move)
		print game.winner if game.winner else 'Nobody', 'has won!'
	finally:
		s.close()
		print 'Connection closed'

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
