#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Created Time : 一  3/ 9 14:52:11 2020
# File Name: day_1_getopt.py
# Description:
"""
import sys
import getopt
def usage():
    info = '''
    help info:
    -h hlep
    -i ip address
    -p port number
    '''

    print(info)

def main(argv):
    print('Test getopt')
    #print(getopt.__doc__)
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ['help', 'ip=', 'port='])
        for name, value in opts:
            if name in ('-h', '--help'):
                usage()
            elif name in ('-i', '--ip'):
                print('ip = ', value)
            elif name in ('-p', '--port'):
                print('port = ', value)

    except getopt.GetoptError:
        usage()


if __name__ == '__main__':
    main(sys.argv[1:])
