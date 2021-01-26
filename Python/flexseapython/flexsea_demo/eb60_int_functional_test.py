import os, sys
from time import sleep
import flexseapython.fxUtil as fxu
import flexseapython.pyFlexsea as fxp
import flexseapython.eb60_test_util as ebu
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
		assert ebu.eb60SensorCheck(devId, appType, logFile), 'Sensor Check Failed'
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
	mVmax = 2000
	[rampUpTime, rampUpTimeStep] = [10, 0.1]
	[noLoadTime, noLoadTimeStep] = [5, 0.1]
	[rampDownTime, rampDownTimeStep] = [10, .1]
	# Pass criteria
	[mVfrictLim, noLoadVelLim] = [766, 3700]

	testPassed = True
	sleep(2)
	fxp.fxSendMotorCommand(devId, fxp.FxVoltage, 0)
	try:
		directions = [1, -1]
		for direction in directions:
			mVmaxLocal = mVmax * direction
			# Ramp motor up and measure voltage to overcome friction
			rampUpResult = noLoadRamp(devId, appType, 0, mVmaxLocal, rampUpTime, rampUpTimeStep, logFile=logFile, measMotStart=True)
			# Let motor reach steady state and measure speed
			noLoadVel = measureNoLoadSpeed(devId, appType, noLoadTime, noLoadTimeStep, mVmaxLocal)
			# Ramp motor down and measure speed
			rampDownResult = noLoadRamp(devId, appType, mVmaxLocal, 0, rampDownTime, rampDownTimeStep, logFile=logFile, measMotStop=True)

			text = f"Motor starting voltage: {rampUpResult['motStartmV']} mv    Acceptance criteria < {mVfrictLim}"
			print('\n' + text)
			logFile.write(text)
			text = f"Motor no load speed at {mVmaxLocal} mv: {int(noLoadVel)}    Acceptance criteria > {noLoadVelLim}"
			print(text)
			logFile.write(text)
			text = f"Motor stop voltage: {rampDownResult['motStopmV']} mv"
			print(text)
			logFile.write(text)
			# Check if test passed
			if rampUpResult['motStartmV'] > mVfrictLim:
				text = f"No Load Test Failed. Measured starting voltage was {rampUpResult['motStartmV']}, it should be be {mVfrictLim}"
				print('\n' + text)
				logFile.write(text)
				testPassed = False
			if abs(noLoadVel) < noLoadVelLim:
				text = f"No Load Test Failed. Measured no load velocity was {int(noLoadVel)}, it should be above {noLoadVelLim}"
				print('\n' + text)
				logFile.write(text)
				testPassed = False

		logFile.write('No load test end')
		return testPassed

	except Exception as e:
		# Set motor voltage to 0 if error occurs
		fxp.fxSendMotorCommand(devId, fxp.FxVoltage, 0)
		text = "Error: problem in no load test - {}".format(e)
		print('\n' + text)
		logFile.write(text)
		testPassed = False
		return testPassed

def noLoadRamp(devId, appType, mVstart, mVstop, rampTime, timeStep, logFile=False, measMotStart=False, measMotStop=False):
	"""
	Ramp the motor voltage from mVstart to mVstop.
	measMotStart allows you to measure at what mV the motor starts turning
	measMotStop allows you to measure at what mV the motor stops turning
	"""
	print(f'\nRamping Motor Voltage from {mVstart} mV to {mVstop} mV...')
	if logFile:
		logFile.write(f'Motor Voltage ramp - starting voltage = {mVstart} mV, stopping voltage = {mVstop} mV, ramp time = {rampTime} s, time step = {timeStep} s')
	[motStartSpeed, motStopSpeed] = [1000, 1000]
	[motStartFlag, motStopFlag] = [0, 0]
	motmVdict = {'motStartmV': float('inf'), 'motStopmV': 0}


	steps = rampTime/timeStep
	mVstep = (mVstop - mVstart)/steps

	dataDict = fxu.getData(devId, appType)
	mot_ang = dataDict['mot_ang']
	last_mot_ang = mot_ang
	idx = 0

	for mV in range(int(mVstart), int(mVstop), int(mVstep)):
		fxp.fxSendMotorCommand(devId, fxp.FxVoltage, mV)
		sleep(timeStep)
		dataDict = fxu.getData(devId, appType)
		mot_ang = dataDict['mot_ang']
		mot_vel = (mot_ang - last_mot_ang)/timeStep
		last_mot_ang = mot_ang
		
		if measMotStart and abs(mot_vel) > motStartSpeed and not motStartFlag:
			motmVdict['motStartmV'] = mV
			motStartFlag = 1

		if measMotStop and abs(mot_vel) < motStopSpeed and not motStopFlag:
			motmVdict['motStopmV'] = mV
			motStopFlag = 1

		# Update user
		if idx % 10 == 0:
			print(f'Curent Voltage: {mV} mV, Stop Voltage: {mVstop} mV')
		idx += 1

	print(f'Curent Voltage: {mV} mV, Stop Voltage: {mVstop} mV')
	fxp.fxSendMotorCommand(devId, fxp.FxVoltage, mVstop)

	return motmVdict

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
