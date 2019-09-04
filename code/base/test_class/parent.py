#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:
    parentAttr = 100
    def __init__(self):
        print "Parent __init__"
    def parentMethod(self):
        print "Parent parentMethod"
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print "Parent getAttr", Parent.parentAttr

class Child(Parent):
    def __init__(self):
        print "Child __init__"
    def childeMethod(self):
        print "Child childeMethod"

c = Child()
c.childeMethod()
c.parentMethod()
c.setAttr(1011)
c.getAttr()

