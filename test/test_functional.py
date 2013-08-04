#!/usr/bin/python

import unittest
import thread
import subprocess
import time
import os

class TestGame(unittest.TestCase):

    FILES = {'o': ['input.os', 'output.os'], 'x': ['input.xs', 'output.xs']}

    def test_play(self):
        print 'start server inside a new thread'
        # start server inside a new thread
        thread.start_new_thread( self.server, () )
        print 'make sure the client starts later than the server'
        # make sure the client starts later than the server
        time.sleep(0.1)
        print 'start client inside another new thread'
        # start client inside another new thread
        thread.start_new_thread( self.client, () )
        print 'make sure they both finish the play before the main script continues'
        # make sure they both finish the play before the main script continues
        time.sleep(1)
        print 'finished'
        fo = open(self.FILES['o'][1],'r')
        fx = open(self.FILES['x'][1],'r')
        self.assertEqual(fo.readlines()[-2].strip(), 'O has won!')
        self.assertEqual(fx.readlines()[-2].strip(), 'O has won!')
        os.remove(self.FILES['o'][1])
        os.remove(self.FILES['x'][1])

    def client(self):
        print 'calling client'
        subprocess.call('../nac/client.py', stdin=open(self.FILES['o'][0],'r'), stdout=open(self.FILES['o'][1],'w'))
        print 'client finished'

    def server(self):
        print 'calling server'
        subprocess.call('../nac/server.py', stdin=open(self.FILES['x'][0],'r'), stdout=open(self.FILES['x'][1],'w'))
        print 'server finished'
