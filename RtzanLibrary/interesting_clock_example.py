#!/usr/bin/env python
import unittest
import os
from datetime import datetime, timedelta

__author__ = 'Marius Cornescu'
__email__ = 'marius_cornescu@yahoo.com'
__copyright__ = '2019'
##########################################################################################################


##########################################################################################################
#
def get_interesting_time_count(start_time_str, end_time_str):
	print('')
	interesting_count = 0
	
	start_time = datetime.strptime(start_time_str, '%H:%M:%S')
	end_time = datetime.strptime(end_time_str, '%H:%M:%S')
	
	current_time = start_time
	one_second = timedelta(seconds=1)
	
	while current_time <= end_time:
		#print('[current_time = %s] [end_time = %s]' % (current_time, end_time))
		
		timestamp = current_time.time().strftime('%H:%M:%S')
		
		if is_interesting_time(timestamp):
			print('!! [timestamp = %s]' % (timestamp))
			interesting_count += 1
		#
		
		current_time += one_second
	#
	
	return interesting_count
	
def is_interesting_time(timestamp):
	#print('>> [timestamp = %s]' % (timestamp))
	
	clean_stamp = timestamp.replace(':', '')
	
	return get_unique_char_count(clean_stamp) <= 2
	
def get_unique_char_count(text):
	return len(set(text))
#
##########################################################################################################


##########################################################################################################

#***************************************************************************************
class Test(unittest.TestCase):
	
	def test_00_00_00_is_interesting(self):
		
		# Given
		stamp = '00:00:00'
		
		# When
		is_interesting = is_interesting_time(stamp)
		
		# Then
		self.assertTrue(is_interesting)
		
	def test_10_00_01_is_interesting(self):
		
		# Given
		stamp = '10:00:01'
		
		# When
		is_interesting = is_interesting_time(stamp)
		
		# Then
		self.assertTrue(is_interesting)
		
	def test_12_34_56_not_interesting(self):
		
		# Given
		stamp = '12:34:56'
		
		# When
		is_interesting = is_interesting_time(stamp)
		
		# Then
		self.assertFalse(is_interesting)
		
	def test_interesting_count_00_00_00_to_05_01_00_range(self):
		
		# Given
		start_stamp = '00:00:00'
		end_stamp = '05:01:00'
		
		# When
		interesting_cnt = get_interesting_time_count(start_stamp, end_stamp)
		
		# Then
		self.assertEqual(156, interesting_cnt)
		
	def test_interesting_count_00_00_00_to_23_59_59_range(self):
		
		# Given
		start_stamp = '00:00:00'
		end_stamp = '23:59:59'
		
		# When
		interesting_cnt = get_interesting_time_count(start_stamp, end_stamp)
		
		# Then
		self.assertEqual(504, interesting_cnt)

#***************************************************************************************

if __name__ == '__main__':
	unittest.main()
