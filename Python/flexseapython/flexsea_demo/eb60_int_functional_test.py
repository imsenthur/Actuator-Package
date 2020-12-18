import os, sys
from time import sleep
import flexseapython.fxUtil as fxu
import flexseapython.pyFlexsea as fxp
import testLogFile as tlf
from numpy import mean

PARDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARDIR)

def fxEB60IntFunctTest(port, baudRate):
	"""
	Runs intermediate functional test designed for EB60
	"""
	# Setup Device
	devId = fxp.fxOpen(port, baudRate, logLevel = 6)
	fxp.fxStartStreaming(devId, 100, shouldLog = True)
	appType = fxp.fxGetAppType(devId)

	print("\nStarting Intermediate Functional Test...")

	logFile = tlf.TestLogFile('EB60_Intermediate_Functional_Test')

	# Run tests
	try:
		assert eb60SensorCheck(devId, appType, logFile), 'Sensor Check Failed'
		assert eb60AnkCheck(devId, appType, logFile), 'Ankle Check Failed'
		assert eb60FindPoles(devId, logFile), 'Find Poles Failed'
		# Close the reopen device after finding poles
		fxp.fxClose(devId)
		devId = fxp.fxOpen(port, baudRate, logLevel = 6)
		fxp.fxStartStreaming(devId, 100, shouldLog = True)
		assert eb60NoLoadAct(devId, appType, logFile), 'No Load Test Failed'
		print("\nAll Tests Passed")
		logFile.write("All tests passed")
	except AssertionError as err:
		print('Test Failed: {}'.format(err))

	# Close device
	fxp.fxClose(devId)
	return True

##########################################################################
# Test Functions

def eb60SensorCheck(devId, appType, logFile):
	"""
	Sensor Check - Verify all sensors are functioning nominally
	"""
	print("\nChecking Sensors...")
	logFile.write(f'Sensor check start')
	[time, time_step] = [2, 0.1]

	dataDict = fxu.recordData(devId, appType, time, time_step, showMsg=True)

	if checkSensVals(dataDict, logFile):
		print("\nSensor Check Passed")
		logFile.write(f'Sensor check end')
		logFile.write('Sensor Check Passed')
		return True
	else:
		logFile.write(f'Sensor check end')
		logFile.write('Sensor Check Failed')
		return False

def checkSensVals(dataDict, logFile):
	"""
	Verify that measured sensor values match expect values.
	Checks include:
	  - signals are non zero
	  - signals are in expected range
	 """
	testPassed = True
	# Check sensor are non zero
	sensors = ['accelx', 'accely', 'accelz', 'gyrox', 'gyroy', 'gyroz', 
				'mot_ang', 'mot_cur', 'batt_volt', 'batt_curr']
	for sensor in sensors:
		sensorMean = mean(dataDict[sensor])
		logFile.write(f'sensor = {sensor}, measured mean = {str(sensorMean)}, Acceptance criteria - not == 0.0')
		if sensorMean == 0.0:
			print(f'Sensor Check Failed: {sensor} is 0.0')
			testPassed = False

	# Check sensors are in range
	sensorRange = {
		'accelx': {'min': -25000, 'max': 25000},
		'accely': {'min': -25000, 'max': 25000},
		'accelz': {'min' :-25000, 'max': 25000},
		'gyrox': {'min': -15000, 'max': 15000},
		'gyroy': {'min': -15000, 'max': 15000},
		'gyroz': {'min': -15000, 'max': 15000},
		#'batt_volt': {'min': 180, 'max': 225},		# USB Voltage
		'batt_volt': {'min': 38000, 'max': 39000},	# Power Supply Voltage
		'batt_curr': {'min': -130, 'max': 231},
		'temperature': {'min': 10, 'max': 60}
		#'ank_ang': {'min': 2000, 'max': 6300},
		#'ank_vel': {'min': -500, 'max': 500}
		}
	for sensor in sensorRange:
		sensorMin = min(dataDict[sensor])
		sensorMax = max(dataDict[sensor])
		logFile.write(f"sensor = {sensor}, measured [minimum, maximum] = [{str(sensorMin)}, {str(sensorMax)}], limit [minimum, maximum] = [{str(sensorRange[sensor]['min'])}, {str(sensorRange[sensor]['max'])}]")
		if sensorMin < sensorRange[sensor]['min']:
			print(f"\nSensor Check Failed: {sensor} minimum is {sensorMin} (it should be above {sensorRange[sensor]['min']})")
			testPassed = False
		if sensorMax > sensorRange[sensor]['max']:
			print(f"\nSensor Check Failed: {sensor} maximum is {sensorMax} (it should be below {sensorRange[sensor]['max']})")
			testPassed = False	

	return testPassed

def eb60AnkCheck(devId, appType, logFile):
	"""
	Ankle Encoder Check - Verfiy ankle encoder is functioning nominally.
	This is done using the follow process:
	  - Operator rotates magnet over Habs
	  - Data is recorded during this operation
	  - Data is analyzed to verify nominal function
	"""
	logFile.write(f'Ankle angle check start')
	[time, time_step] = [5, 0.1]

	print(f'\n>>> User Input: Move ankle through its full range of travel for {time} seconds\n')
	sleep(3)
	print('Measuring Ankle Position...')
	dataDict = fxu.recordData(devId, appType, time, time_step, showMsg=True, msgFreq=5)

	if checkAnkVals(dataDict, logFile):
		print("\nAnkle Angle Check Passed")
		logFile.write('Ankle Angle Check Passed')
		logFile.write(f'Ankle angle check end')
		return True
	else:
		logFile.write('Ankle Angle Check Failed')
		logFile.write(f'Ankle angle check end')
		return False		

def checkAnkVals(dataDict, logFile):
	"""
	Check that measured min and max are in expected range
	"""
	testPassed = True

	sensorRange = {
		'ank_ang': {'min_lo': 1990, 'min_hi': 2100, 'max_lo': 6150, 'max_hi': 6400},
		}

	for sensor in sensorRange:
		sensorMin = min(dataDict[sensor])
		sensorMax = max(dataDict[sensor])
		logFile.write(f"sensor = {sensor}, measured minimum = {str(sensorMin)}, acceptable range = {str(sensorRange[sensor]['min_lo'])} to {str(sensorRange[sensor]['min_hi'])}")
		logFile.write(f"sensor = {sensor}, measured minimum = {str(sensorMax)}, acceptable range = {str(sensorRange[sensor]['max_lo'])} to {str(sensorRange[sensor]['max_hi'])}")
		if sensorMin < sensorRange[sensor]['min_lo'] or sensorMin > sensorRange[sensor]['min_hi']:
			text = f"\nSensor Check Failed: {sensor} minimum is {sensorMin} (it should be between {sensorRange[sensor]['min_lo']} and {sensorRange[sensor]['min_hi']})"
			print(text)
			logFile.write(text)
			testPassed = False
		if sensorMax < sensorRange[sensor]['max_lo'] or sensorMax > sensorRange[sensor]['max_hi']:
			text = f"\nSensor Check Failed: {sensor} maximum is {sensorMax} (it should be between {sensorRange[sensor]['max_lo']} and {sensorRange[sensor]['max_hi']})"
			print(text)
			logFile.write(text)
			testPassed = False

	return testPassed

def eb60FindPoles(devId, logFile):
	"""
	Run fxFindPoles and wait for completion
	"""
	print("\nFinding Poles...")
	logFile.write(f'Find poles start')
	time = 60.0
	time_step = 10.0
	
	fxp.fxFindPoles(devId)
	for i in range(int(time / time_step)):
		print(f"{int(time - i * time_step)} seconds remaining")
		sleep(time_step)
	print("0 seconds remaining")
	logFile.write(f'Find poles end')
	return True

def eb60NoLoadAct(devId, appType, logFile):
	"""
	Spin the motor and make sure it behaves nominally
	Tests include:
	  - no load ramp up - records voltage at which the motor overcomes static friction
	  - no load speed - measures the no load speed of the motor
	  - ramp down - safely stops the motor from spinning
	"""
	print("\nRunning No Load Test...")
	logFile.write(f'No load test start')
	# Test parameters
	[rampUpTime, rampUpTimeStep, mVmax] = [30, 0.1, 2000]
	[noLoadTime, noLoadTimeStep] = [5, 0.1]
	[rampDownTime, rampDownTimeStep] = [2, .01]
	# Pass criteria
	[mVcogLim, noLoadVelLim] = [766, 3700]

	testPassed = True
	sleep(2)
	fxp.fxSendMotorCommand(devId, fxp.FxVoltage, 0)
	try:
		# Ramp motor up and measure voltage to overcome friction
		mVcog = noLoadRampUp(devId, appType, rampUpTime, rampUpTimeStep, mVmax)
		# Let motor reach steady state and measure speed
		noLoadVel = measureNoLoadSpeed(devId, appType, noLoadTime, noLoadTimeStep, mVmax)
		noLoadRampDown(devId, appType, rampDownTime, rampDownTimeStep, mVmax)

		text = f"Motor cogging voltage: {int(mVcog)} mv    Acceptance criteria < {mVcogLim}"
		print('\n' + text)
		logFile.write(text)
		text = f"Motor no load speed at {mVmax} mv: {int(noLoadVel)}    Acceptance criteria > {noLoadVelLim}"
		print(text)
		logFile.write(text)

		# Check if test passed
		if mVcog > mVcogLim:
			text = f"No Load Test Failed. Measured cogging voltage was {int(mVcog)}, it should be be {mVcogLim}"
			print('\n' + text)
			logFile.write(text)
			testPassed = False
		if noLoadVel < noLoadVelLim:
			text = f"No Load Test Failed. Measured no load velocity was {int(noLoadVel)}, it should be above {noLoadVelLim}"
			print('\n' + text)
			logFile.write(text)
			testPassed = False

		logFile.write(f'No load test end')
		return testPassed

	except Exception as e:
		# Set motor voltage to 0 if error occurs
		fxp.fxSendMotorCommand(devId, fxp.FxVoltage, 0)
		text = "Error: problem in no load test - {}".format(e)
		print('\n' + text)
		logFile.write(text)
		testPassed = False
		return testPassed

def noLoadRampUp(devId, appType, time, time_step, mVmax):
	"""
	Slowly increase motor voltage and record when the motor starts spinning
	"""
	mV = 0
	mot_vel = 0
	dataDict = fxu.getData(devId, appType)
	mot_ang = dataDict['mot_ang']
	last_mot_ang = mot_ang
	[cogFlag, mVcog] = [True, -1]

	# Ramp up
	for i in range(int(time / time_step)):
		if (i * time_step) % 3 == 0:
			print(f"{int(time - i * time_step)} seconds remaining in ramp up")
		dataDict = fxu.getData(devId, appType)
		mot_ang = dataDict['mot_ang']
		mot_vel = (mot_ang - last_mot_ang)/time_step
		sleep(time_step)
		mV = int(mVmax * ((i + 1) * time_step/time))
		fxp.fxSendMotorCommand(devId, fxp.FxVoltage, mV)
		if mot_vel > 1000 and cogFlag:
			cogFlag = False
			mVcog = mV
		last_mot_ang = mot_ang
	print("0 seconds remaining in ramp up")

	return mVcog

def measureNoLoadSpeed(devId, appType, time, time_step, mV):
	"""
	Let the motor spin at a constant voltage and measure speed
	"""
	print("\nMeasuring no load speed...")
	fxp.fxSendMotorCommand(devId, fxp.FxVoltage, mV)
	# Let motor reach steady state and measure speed
	sleep(1)
	dataDict = fxu.recordData(devId, appType, time=5, time_step=0.1, showMsg=True, msgFreq=3)
	motVelList = list()
	for i in range(1, len(dataDict['mot_ang'])):
		motVelList.append(dataDict['mot_ang'][i] - dataDict['mot_ang'][i-1])
	noLoadVel = mean(motVelList)
	return noLoadVel

def noLoadRampDown(devId, appType, time, time_step, mV_start):
	"""
	Ramp the motor speed down
	"""
	mV = mV_start
	for i in range(int(time / time_step)):
		sleep(time_step)
		mV = int(mV - mV_start / (time / time_step))
		fxp.fxSendMotorCommand(devId, fxp.FxVoltage, mV)
	fxp.fxSendMotorCommand(devId, fxp.FxVoltage, 0)


def main():
	baudRate = sys.argv[1]
	ports = sys.argv[2:3]
	try:
		fxp.fxOpenControl(baudRate)
	except Exception as e:
		print("Broke... ")
		print(str(e))	

if __name__ == '__main__':
	main()
