#!/usr/bin/python

import os
os.chdir("D:\libsvm-3.16\python")
from svmutil import *
y,x = svm_read_problem()
