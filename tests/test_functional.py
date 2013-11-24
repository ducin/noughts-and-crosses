#!/usr/bin/python

import unittest
import thread
import subprocess
import time
import os
DIR = os.path.abspath(__file__ + "/..")

class TestGame(unittest.TestCase):

    FILES = {'o': [DIR + '/input.os', DIR + '/output.os', DIR + '/../nac/client.py'], 'x': [DIR + '/input.xs', DIR + '/output.xs', DIR + '/../nac/server.py']}

    def test_play(self):
        # start server inside a new thread
        thread.start_new_thread( self.server, () )
        # make sure the client starts later than the server
        time.sleep(1)
        # start client inside another new thread
        thread.start_new_thread( self.client, () )
        # make sure they both finish the play before the main script continues
        time.sleep(1)
        fo = open(self.FILES['o'][1],'r')
        fx = open(self.FILES['x'][1],'r')
        fol = fo.readlines()
        fxl = fx.readlines()
        print fol
        print fxl
        self.assertEqual(fol[-2].strip(), 'O has won!')
        self.assertEqual(fxl[-2].strip(), 'O has won!')
        fo.close()
        fx.close()
        os.remove(self.FILES['o'][1])
        os.remove(self.FILES['x'][1])

    def client(self):
        subprocess.call(self.FILES['o'][2], stdin=open(self.FILES['o'][0],'r'), stdout=open(self.FILES['o'][1],'w'))

    def server(self):
        subprocess.call(self.FILES['x'][2], stdin=open(self.FILES['x'][0],'r'), stdout=open(self.FILES['x'][1],'w'))
