#! /usr/bin/env python
# *-* coding: UTF-8 *-*

import argparse

#Supress Warning message
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import IP,Ether,TCP,send,sr,conf
conf.verb=0

parser = argparse.ArgumentParser(description='Scan a firewall.',epilog="smoothy project")
parser.add_argument('host', metavar='host', type=str,help='Host to scan.')
parser.add_argument('cp', metavar='closed port', type=int,help='Port to test.')
parser.add_argument('-op', metavar='open port', type=int, nargs='?', default='80', help='Open port with an availible service.')
parser.add_argument('-pn', metavar='packets number', type=int, nargs='?', default='100', help='Number of packets to send.')

args = parser.parse_args()

class PacketTrain:
	def __init__(self,host,cp,op,pn):
		self.target=host
		default_packet=IP(dst=host)
		self.train_packets=default_packet/TCP(dport=cp)
		self.final_packet=default_packet/TCP(dport=op)
		self.send_time=0
		self.delta_time=0
	def __str__(self):
		print self.target
	def send(self):
		for i in range(1,args.pn):
			send(self.train_packets)
		ans,re=sr(self.final_packet,timeout=2)
		if ans == []:
			raise Exception("Timeout: The specified open port may be not open, try -op to change it")
		return ans[0][1].time-ans[0][0].sent_time

#We build the train of packet:
t1=PacketTrain(args.host,args.cp,args.op,args.pn)
#We send the train

print t1.send()

