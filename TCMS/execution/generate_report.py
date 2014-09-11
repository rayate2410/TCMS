from __future__ import division
import sys
from models import TestPlan, ExecutionHistory, ExecutionTask
from project.models import Project, Category, Build, Browser, ClientDevice
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from testcase.models import TestCase, TestcaseHistory
import time
from testcase.models import TestCase
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4

print "hello"