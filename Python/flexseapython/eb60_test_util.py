import numpy as np
from scipy.signal import chirp, sweep_poly
import matplotlib.pyplot as pyplt
import time
import flexseapython.pyFlexsea as fxp


class GenSineSweep:
	"""
	This class creates a sine sweep profile.
	"""
	def __init__(self, start_freq, end_freq, amplitude, run_time, time_step, offset=0, show_plot=False):
		self.run_time = run_time
		self.time_step = time_step

		steps = int(run_time/time_step)
		time = list(np.linspace(0, run_time, steps + 1))
		val = list(amplitude * chirp(time, f0=start_freq, f1=end_freq, t1=run_time, method='linear', phi=90))

		self.profile = {'time': time, 'val': val}
		
		if show_plot: 
			make_plot(time, val) 

	def get_profile(self):
		return self.profile

	def get_run_time(self):
		return self.run_time

	def get_time_step(self):
		return self.time_step

def make_plot(time, val, x_label=False, y_label=False, legend=False):
	"""
	This function makes a plot.
	Add pyplt.show() when you want to show plot. Note that this function is blocking.
	"""
	fig, ax = pyplt.subplots()
	line1, = ax.plot(time, val)
	if x_label:
		pyplt.xlabel(x_label)
	if y_label:
		pyplt.ylabel(y_label) 
	pyplt.draw()


def run_position_profile(devId, profile):
	"""
	This function takes a profile object and commands the actpack to execute the profile.
	"""
	run_time = profile.get_run_time()
	
	time_list = profile.get_profile()['time']
	m_voltage_list = profile.get_profile()['val']
	start_time = time.time()

	try:
		[elapsed_time, last_time] = [0.0, 0.0]
		[set_time, set_m_voltage] = [[], []]
		text = ""
		while elapsed_time < run_time:
			elapsed_time = time.time() - start_time
			time_step = elapsed_time - last_time

			while (elapsed_time > time_list[0] + profile.get_time_step()) and (len(time_list) > 1):
					time_list.pop(0)
					m_voltage_list.pop(0)

			set_time.append(time_list[0])
			set_m_voltage.append(m_voltage_list[0])

			fxp.fxSendMotorCommand(devId, fxp.FxVoltage, m_voltage_list[0])

			time.sleep(profile.get_time_step())
			#print(f'time_list[0]: {time_list[0]:.3f}, m_voltage_list[0]: {m_voltage_list[0]:.3f}, elapsed_time: {elapsed_time:.3f}, time_step: {time_step:.3f}')
			#print(f'time_list[0]: {time_list[0]:.3f}, elapsed_time: {elapsed_time:.3f}, time_step: {time_step:.3f}')
			#print(f'm_voltage_list[0]: {m_voltage_list[0]:.3f}, elapsed_time: {elapsed_time:.3f}, time_step: {time_step:.3f}')
			text = text + (f'\nm_voltage_list[0]: {m_voltage_list[0]:.3f}, elapsed_time: {elapsed_time:.3f}, time_step: {time_step:.3f}')


			last_time = elapsed_time

		print(text)
		return [set_time, set_m_voltage]


	except Exception as e:
		# Set motor voltage to 0 if error occurs
		fxp.fxSendMotorCommand(devId, fxp.FxVoltage, 0)
		text = "Error: problem in no load test - {}".format(e)
		print('\n' + text)
		#logFile.write(text)

		return None


def main(devId):
	"""
	Do stuff here
	"""
	profile = GenSineSweep(start_freq=0.01, end_freq=5, amplitude=3000, run_time=20, time_step=0.001, offset=0) 
	data = run_position_profile(devId, profile)
	fxp.fxSendMotorCommand(devId, fxp.FxVoltage, 0)
	make_plot(data[0], data[1], x_label='time (s)', y_label='Voltage (mV)')
	pyplt.show()
	return True


if __name__ == '__main__':
	main(devId)


