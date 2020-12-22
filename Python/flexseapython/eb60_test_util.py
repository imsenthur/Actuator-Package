import numpy as np
from scipy.signal import chirp, sweep_poly
import matplotlib.pyplot as plt
import time

class GenSineSweep:
	def __init__(self, start_freq, end_freq, amplitude, run_time, time_step, offset=0, show_plot=False):
		self.run_time = run_time
		self.time_step = time_step

		steps = int(run_time/time_step)
		time = list(np.linspace(0, run_time, steps + 1))
		val = list(amplitude * chirp(time, f0=start_freq, f1=end_freq, t1=run_time, method='linear'))

		self.profile = {'time': time, 'val': val}
		
		if show_plot: 
			make_plot(time, val) 

	def get_profile(self):
		return self.profile

	def get_run_time(self):
		return self.run_time

	def get_time_step(self):
		return self.time_step

def make_plot(time, val):
	fig, ax = plt.subplots()
	line1, = ax.plot(time, val)
	ax.legend()
	plt.draw()


def run_position_profile(profile):
	run_time = profile.get_run_time()
	
	time_list = profile.get_profile()['time']
	m_voltage_list = profile.get_profile()['val']
	start_time = time.time()

	[elapsed_time, last_time] = [0.0, 0.0]
	[set_time, set_m_voltage] = [[], []]
	while elapsed_time < run_time:
		elapsed_time = time.time() - start_time
		time_step = elapsed_time - last_time

		time.sleep(0.001)

		while elapsed_time > time_list[0] - profile.get_time_step():
				time_list.pop(0)
				m_voltage_list.pop(0)


		print(f'time_list[0]: {time_list[0]:.3f}, m_voltage_list[0]: {m_voltage_list[0]:.3f}, elapsed_time: {elapsed_time:.3f}, time_step: {time_step:.3f}')

		set_time.append(time_list[0])
		set_m_voltage.append(m_voltage_list[0])


		last_time = elapsed_time

	return [set_time, set_m_voltage]

if __name__ == '__main__':
	profile = GenSineSweep(start_freq=0.01, end_freq=5, amplitude=10, run_time=5, time_step=.01, offset=0) 
	data = run_position_profile(profile)
	make_plot(data[0], data[1])

