from contextlib import ContextDecorator, contextmanager
import datetime
import os
import time
from time import perf_counter
from datetime import timedelta
 
class LogFile(ContextDecorator):

	def __enter__(self):
		start_time = time.time()
		elapsed = (time.time() - start_time)
		running_time = str(timedelta(seconds=elapsed))
		my_file = "./ContextDecorator"
		log_file = open(my_file, 'w+')
		current_time = datetime.datetime.now()
		log_file.write(str(current_time))
		log_file.write(str(running_time))
		log_file.write("An error occured: ")
		log_file.close()
	
	def __exit__(self):
		print(f"Start: {current_time} | Run: {running_time} | An error occured: {None}")

