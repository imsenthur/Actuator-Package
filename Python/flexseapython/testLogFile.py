import datetime, os

class TestLogFile:
	"""
	Use this class to create a log file
	"""
	def __init__(self, testname):
		print('\n>>>Input device serial number:')
		sn = input() 
		print('>>>Enter your initials:')
		operator = input()
		now = datetime.datetime.now()
		date = now.strftime("%Y%m%d")
		time = now.strftime("%H%M%S")
		nowstr = date + "_" + time

		filename = nowstr + "_SN" + sn + "_" + testname
		log_folder ='TestLogs'
		log_dir_path = os.path.join(os.path.expanduser('~'), log_folder)
		self.log_file_path = os.path.join(os.path.expanduser('~'), log_folder, filename)
		if not os.path.exists(log_dir_path):
			os.mkdir(log_dir_path)

		with open(self.log_file_path, "a") as log:
			log.write(f"Test: {testname}")
			log.write(f"\nSN: {sn}")
			log.write(f"\nDate: {date}")
			log.write(f"\nStart Time: {time}")
			log.write(f"\nOperator: {operator}")

	def write(self, text):
		with open(self.log_file_path, "a") as log:
			log.write(f"\n{datetime.datetime.now()}: ")
			log.write(text)
			log.close
