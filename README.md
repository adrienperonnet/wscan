wscan
=====

This script try to guess the order of the filters of a firewall machine.

The idea of this tool is to send a train of packets on a given port, followed by an acceptable packet, then store the response time. Doing that with many ports, and ordering the response time should give a good idea of the ordering of the firewall rules.
