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

	testFlag = True
	if testFlag:
		testFlag = eb60SensorCheck(devId, appType, time=2, time_step=0.1)
	if testFlag:
		testFlag = eb60AnkCheck(devId, appType, time=2, time_step=0.1)
	#if testFlag:
	#	testFlag = eb60FindPoles(devId)
	if testFlag:
		testFlag = eb60NoLoadAct(devId, appType, time=10, time_step=0.1)
	if testFlag:
		print("\nAll Tests Passed")

	fxClose(devId)
	return True


##########################################################################
# Test Functions

# Sensor Check - Verify all sensors are functioning nominally
def eb60SensorCheck(devId, appType, time, time_step):
	print("\nChecking Sensors...")

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
		'temperature': {'min': 10, 'max': 53},
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
def eb60AnkCheck(devId, appType, time, time_step):
	print('\n>>> User Input: Move ankle through its full range of travel for 5 seconds\n')
	sleep(3)

	print('Measuring Ankle Position...')
	dataDict = recordData(devId, appType, time, time_step, showMsg=True)

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
	fxFindPoles(devId)
	time = 60.0
	time_step = 10.0
	for i in range(int(time / time_step)):
		print(f"{int(time - i * time_step)} seconds remaining")
		sleep(time_step)
	print("0 seconds remaining")
	return True

def eb60NoLoadAct(devId, appType, time, time_step):
	print("\nRunning No Load Test...")
	testPassed = True
	fxSendMotorCommand(devId, FxVoltage, 0)
	sleep(1)
	try:
		# Measure cogging voltage
		[time, time_step] = [30, 0.1]
		[mV, mVmax] = [0, 2000]
		mot_vel = 0
		dataDict = getData(devId, appType)
		mot_ang = dataDict['mot_ang']
		last_mot_ang = mot_ang
		[cogFlag, mVcog] = [True, -1]

		# Ramp up
		for i in range(int(time / time_step)):
			if (i * time_step) % 1 == 0:
				print(f"{int(time - i * time_step)} seconds remaining")
			dataDict = getData(devId, appType)
			mot_ang = dataDict['mot_ang']
			mot_vel = (mot_ang - last_mot_ang)/time_step
			sleep(time_step)
			mV = int(mVmax * ((i + 1) * time_step/time))
			print(i, mV)
			fxSendMotorCommand(devId, FxVoltage, mV)
			if mot_vel > 1000 and cogFlag:
				cogFlag = False
				mVcog = mV
			last_mot_ang = mot_ang
		print("0 seconds remaining")

		# Let motor reach steady state and measure speed
		print("\nMeasuring no load speed...")
		sleep(1)
		dataDict = recordData(devId, appType, time=3, time_step=0.1, showMsg=True)
		motVelList = []
		last_mot_ang = 0
		for ang in dataDict['mot_ang']:
			motVelList.append(ang - last_mot_ang)
		noLoadVel = mean(motVelList)
		motVelList.pop(0)
		noLoadVel = mean(motVelList)

		# Ramp down
		[time, time_step] = [2, .01]
		for i in range(int(time / time_step)):
			sleep(time_step)
			mV = int(mV - mVmax / (time / time_step))
			fxSendMotorCommand(devId, FxVoltage, mV)
		fxSendMotorCommand(devId, FxVoltage, 0)

		print(f"\nMotor cogging voltage: {int(mVcog)} mv    Motor no load speed at {mVmax} mv: {int(noLoadVel)}")

		[mVcogLim, noLoadVelLim] = [766, 520000]
		if mVcog > mVcogLim:
			print(f"\nNo Load Test Failed. Measured cogging voltage was {mVcog}, it should be be {mVcogLim}")
			testPassed = False
		if noLoadVel < noLoadVelLim:
			print(f"\nNo Load Test Failed. Measured no load velocity was {noLoadVel}, it should be above {noLoadVelLim}")
			testPassed = False

		return testPassed

	except:
		print("\nError: problem in no load test")
		# Set motor voltage to 0 if error occurs
		fxSendMotorCommand(devId, FxVoltage, 0)
		testPassed = False
		return testPassed


if __name__ == '__main__':
	baudRate = sys.argv[1]
	ports = sys.argv[2:3]
	try:
		fxOpenControl(baudRate)
	except Exception as e:
		print("Broke... ")
		print(str(e))
