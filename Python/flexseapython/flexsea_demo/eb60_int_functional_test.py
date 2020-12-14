import os, sys
from time import sleep
from flexseapython.fxUtil import *
from numpy import mean

pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pardir)

def fxEB60IntFunctTest(port, baudRate):
	# Setup Device
	devId = fxOpen(port, baudRate, logLevel = 6)
	fxStartStreaming(devId, 100, shouldLog = True)
	appType = fxGetAppType(devId)

	print("\nStarting Intermediate Functional Test...")
	#file1 = open("MyFile.txt","a") 


	testFlag = True
	if testFlag:
		testFlag = eb60SensorCheck(devId, appType)
	if testFlag:
		testFlag = eb60AnkCheck(devId, appType)
	if testFlag:
		testFlag = eb60FindPoles(devId)
		# Close the reopen device
		fxClose(devId)
		devId = fxOpen(port, baudRate, logLevel = 6)
		fxStartStreaming(devId, 100, shouldLog = True)
	if testFlag:
		testFlag = eb60NoLoadAct(devId, appType)
	if testFlag:
		print("\nAll Tests Passed")


	# Close device
	fxClose(devId)
	return True


##########################################################################
# Test Functions

# Sensor Check - Verify all sensors are functioning nominally
def eb60SensorCheck(devId, appType):
	print("\nChecking Sensors...")
	[time, time_step] = [2, 0.1]

	dataDict = recordData(devId, appType, time, time_step, showMsg=True)

	if checkSensVals(dataDict):
		print("\nSensor Check Passed")
		return True
	else:
		print("\nTest Failed: Sensor Check Failed")
		return False

def checkSensVals(dataDict):
	testPassed = True
	# Check sensor are non zero
	sensors = ['accelx', 'accely', 'accelz', 'gyrox', 'gyroy', 'gyroz', 
				'mot_ang', 'mot_cur', 'batt_volt', 'batt_curr']
	for sensor in sensors:
		sensorMean = mean(dataDict[sensor])
		if sensorMean == 0.0:
			print(f'Sensor Check Failed: {sensor} is 0.0')
			testPassed = False

	# Check sensors are in range
	sensors = ['accelx', 'accely', 'accelz', 'gyrox', 'gyroy', 'gyroz', 
				'batt_volt', 'batt_curr', 'temperature']
	sensorRange = {
		'accelx': {'min': -25000, 'max': 25000},
		'accely': {'min': -25000, 'max': 25000},
		'accelz': {'min' :-25000, 'max': 25000},
		'gyrox': {'min': -15000, 'max': 15000},
		'gyroy': {'min': -15000, 'max': 15000},
		'gyroz': {'min': -15000, 'max': 15000},
		#'batt_volt': {'min': 180, 'max': 225},		# USB Voltage
		'batt_volt': {'min': 38000, 'max': 39000},	# Power Supply Voltage
		'batt_curr': {'min': -130, 'max': 228},
		'temperature': {'min': 10, 'max': 60},
		'ank_ang': {'min': 2000, 'max': 6300},
		'ank_vel': {'min': -500, 'max': 500}
		}
	for sensor in sensors:
		sensorMin = min(dataDict[sensor])
		sensorMax = max(dataDict[sensor])
		if sensorMin < sensorRange[sensor]['min']:
			print(f"\nSensor Check Failed: {sensor} minimum is {sensorMin} (it should be above {sensorRange[sensor]['min']})")
			testPassed = False
		if sensorMax > sensorRange[sensor]['max']:
			print(f"\nSensor Check Failed: {sensor} maximum is {sensorMax} (it should be below {sensorRange[sensor]['max']})")
			testPassed = False	

	return testPassed

# Ankle Encoder Check - Verfiy ankle encoder is functioning nominally
def eb60AnkCheck(devId, appType):
	[time, time_step] = [5, 0.1]

	print(f'\n>>> User Input: Move ankle through its full range of travel for {time} seconds\n')
	sleep(3)
	print('Measuring Ankle Position...')
	dataDict = recordData(devId, appType, time, time_step, showMsg=True, msgFreq=5)

	if checkAnkVals(dataDict):
		print("\nAnkle Angle Check Passed")
		return True
	else:
		print("\nTest Failed: Ankle Angle Check Failed")
		return False		

def checkAnkVals(dataDict):
	# Check that sensors min and max are in range
	testPassed = True

	sensors = ['ank_ang']
	sensorRange = {
		'ank_ang': {'min_lo': 1990, 'min_hi': 2100, 'max_lo': 6150, 'max_hi': 6400},
		}

	for sensor in sensors:
		sensorMin = min(dataDict[sensor])
		sensorMax = max(dataDict[sensor])
		if sensorMin < sensorRange[sensor]['min_lo'] or sensorMin > sensorRange[sensor]['min_hi']:
			print(f"\nSensor Check Failed: {sensor} minimum is {sensorMin} (it should be between {sensorRange[sensor]['min_lo']} and {sensorRange[sensor]['min_hi']})")
			testPassed = False
		if sensorMax < sensorRange[sensor]['max_lo'] or sensorMax > sensorRange[sensor]['max_hi']:
			print(f"\nSensor Check Failed: {sensor} maximum is {sensorMax} (it should be between {sensorRange[sensor]['max_lo']} and {sensorRange[sensor]['max_hi']})")
			testPassed = False

	return testPassed

def eb60FindPoles(devId):
	print("\nFinding Poles...")
	time = 60.0
	time_step = 10.0
	
	fxFindPoles(devId)
	for i in range(int(time / time_step)):
		print(f"{int(time - i * time_step)} seconds remaining")
		sleep(time_step)
	print("0 seconds remaining")
	return True

def eb60NoLoadAct(devId, appType):
	print("\nRunning No Load Test...")
	# Test parameters
	[rampUpTime, rampUpTimeStep, mVmax] = [30, 0.1, 2000]
	[noLoadTime, noLoadTimeStep] = [5, 0.1]
	[rampDownTime, rampDownTimeStep] = [2, .01]
	# Pass criteria
	[mVcogLim, noLoadVelLim] = [766, 3700]

	testPassed = True
	sleep(2)
	fxSendMotorCommand(devId, FxVoltage, 0)
	try:
		# Ramp motor up and measure voltage to overcome friction
		mVcog = noLoadRampUp(devId, appType, rampUpTime, rampUpTimeStep, mVmax)

		# Let motor reach steady state and measure speed
		noLoadVel = measureNoLoadSpeed(devId, appType, noLoadTime, noLoadTimeStep, mVmax)

		# Ramp down
		noLoadRampDown(devId, appType, rampDownTime, rampDownTimeStep, mVmax)

		print(f"\nMotor cogging voltage: {int(mVcog)} mv    Motor no load speed at {mVmax} mv: {int(noLoadVel)}")

		# Check if test passed
		if mVcog > mVcogLim:
			print(f"\nNo Load Test Failed. Measured cogging voltage was {int(mVcog)}, it should be be {mVcogLim}")
			testPassed = False
		if noLoadVel < noLoadVelLim:
			print(f"\nNo Load Test Failed. Measured no load velocity was {int(noLoadVel)}, it should be above {noLoadVelLim}")
			testPassed = False
		return testPassed

	except:
		# Set motor voltage to 0 if error occurs
		fxSendMotorCommand(devId, FxVoltage, 0)
		print("\nError: problem in no load test")
		testPassed = False
		return testPassed

def noLoadRampUp(devId, appType, time, time_step, mVmax):
		# Measure cogging voltage
		mV = 0
		mot_vel = 0
		dataDict = getData(devId, appType)
		mot_ang = dataDict['mot_ang']
		last_mot_ang = mot_ang
		[cogFlag, mVcog] = [True, -1]

		# Ramp up
		for i in range(int(time / time_step)):
			if (i * time_step) % 3 == 0:
				print(f"{int(time - i * time_step)} seconds remaining in ramp up")
			dataDict = getData(devId, appType)
			mot_ang = dataDict['mot_ang']
			mot_vel = (mot_ang - last_mot_ang)/time_step
			sleep(time_step)
			mV = int(mVmax * ((i + 1) * time_step/time))
			fxSendMotorCommand(devId, FxVoltage, mV)
			if mot_vel > 1000 and cogFlag:
				cogFlag = False
				mVcog = mV
			last_mot_ang = mot_ang
		print("0 seconds remaining in ramp up")

		return mVcog

def measureNoLoadSpeed(devId, appType, time, time_step, mV):
	# Let motor reach steady state and measure speed
	print("\nMeasuring no load speed...")
	fxSendMotorCommand(devId, FxVoltage, mV)
	sleep(1)
	dataDict = recordData(devId, appType, time=5, time_step=0.1, showMsg=True, msgFreq=3)
	motVelList = []
	for i in range(1, len(dataDict['mot_ang'])):
		motVelList.append(dataDict['mot_ang'][i] - dataDict['mot_ang'][i-1])
	noLoadVel = mean(motVelList)
	return noLoadVel

def noLoadRampDown(devId, appType, time, time_step, mV_start):
		# Ramp down
		mV = mV_start
		for i in range(int(time / time_step)):
			sleep(time_step)
			mV = int(mV - mV_start / (time / time_step))
			fxSendMotorCommand(devId, FxVoltage, mV)
		fxSendMotorCommand(devId, FxVoltage, 0)


if __name__ == '__main__':
	baudRate = sys.argv[1]
	ports = sys.argv[2:3]
	try:
		fxOpenControl(baudRate)
	except Exception as e:
		print("Broke... ")
		print(str(e))
