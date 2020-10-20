# ./spec/spec_helper.rb
# ./test/test_helper.rb
# ..etc..
import unittest
import json
from flask import request, jsonify
from myservice import app 

app.testing = True

#TODO: Extend these component tests for the calc view 
#       and THEN implement all 4 operations!
# DO NOT REMOVE EXISTING TESTS!


class TestCalc(unittest.TestCase):

    def test_sum1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=3&n=5').get_json()
        self.assertEqual(reply['result'], '8')

    def test_div1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=3&n=0').get_json()
        self.assertEqual(reply['result'], 'DivisionByZeroError')

    def test_div2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=6&n=2').get_json()
        self.assertEqual(reply['result'], '3')

    def test_div3(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=-6&n=2').get_json()
        self.assertEqual(reply['result'], '-3')

    def test_div4(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=6&n=-2').get_json()
        self.assertEqual(reply['result'], '-3')

    def test_mul1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/mul?m=3&n=3').get_json()
        self.assertEqual(reply['result'], '9')

    def test_mul2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/mul?m=3&n=0').get_json()
        self.assertEqual(reply['result'], '0')

    def test_mul3(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/mul?m=-2&n=3').get_json()
        self.assertEqual(reply['result'], '-6')

    def test_sub1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=3&n=0').get_json()
        self.assertEqual(reply['result'], '3')

    def test_sub2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=2&n=-3').get_json()
        self.assertEqual(reply['result'], '5')

    def test_sub3(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=-3&n=1').get_json()
        self.assertEqual(reply['result'], '-4')

    
        

