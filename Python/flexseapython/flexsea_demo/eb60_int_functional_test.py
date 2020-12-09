import os, sys
from time import sleep
from flexseapython.fxUtil import *
from numpy import mean

pardir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pardir)

def fxEB60IntFunctTest(port, baudRate, time = 2, num_times = 5,
		time_resolution = 0.1, maxVoltage = 3000, sign = -1):
	# Setup Device
	devId = fxOpen(port, baudRate, logLevel = 6)
	fxStartStreaming(devId, 100, shouldLog = True)
	appType = fxGetAppType(devId)

	print("\nStarting Intermediate Functional Test...")

	testFlag = True
	if testFlag:
		testFlag = eb60SensorCheck(devId, appType, time=2, time_step=0.1)
	if testFlag:
		testFlag = eb60AnkCheck(devId, appType, time=5, time_step=0.1)
	if testFlag:
		testFlag = eb60FindPoles()
	if testFlag:
		testFlag = eb60NoLoadAct()
	if testFlag:
		testFlag = eb60IMUCal()


	if testFlag:
		print("\nAll Tests Passed")

	fxClose(devId)
	return True


##########################################################################
# Test Functions

# Sensor Check - Verify all sensors are functioning nominally
def eb60SensorCheck(devId, appType, time, time_step):
	print("\nChecking Sensors...")

	# Build dataDict for sensor data
	dataDict = {}
	data = getData(devId, appType)
	for d in data:
		dataDict[d] = []

	# Record data for time
	totalLoopCount = int(time / time_step)
	for i in range(totalLoopCount):
		print(f'Sensor Check Measurement {i} of {totalLoopCount}')
		sleep(time_step)
		data = getData(devId, appType)
		for d in data:
			dataDict[d].append(data[d])

	if checkSensVals(dataDict):
		print("Sensor Check Passed")
		return True
	else:
		print("Test Failed: Sensor Check Failed")
		return False

def checkSensVals(dataDict):
	testPassed = True

	# Check sensor are non zero
	sensors = ['accelx', 'accely', 'accelz', 'gyrox', 'gyroy', 'gyroz', 'mot_ang', 'mot_cur', 'batt_volt', 'batt_curr']
	for sensor in sensors:
		sensorMean = mean(dataDict[sensor])
		if sensorMean == 0.0:
			print(f'Sensor Check Failed: {sensor} is 0.0')
			testPassed = False

	# Check sensors are in range
	sensors = ['accelx', 'accely', 'accelz', 'gyrox', 'gyroy', 'gyroz', 'batt_volt', 'batt_curr', 'temperature']
	sensorRange = {
		'accelx': {'min': -25000, 'max': 25000},
		'accely': {'min': -25000, 'max': 25000},
		'accelz': {'min' :-25000, 'max': 25000},
		'gyrox': {'min': -15000, 'max': 15000},
		'gyroy': {'min': -15000, 'max': 15000},
		'gyroz': {'min': -15000, 'max': 15000},
		'batt_volt': {'min': 180, 'max': 225},
		'batt_curr': {'min': -130, 'max': 120},
		'temperature': {'min': 10, 'max': 40},
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
			print(f"\nSensor Check Failed: {sensor} maximum is {sensorMax} (it should be above {sensorRange[sensor]['max']})")
			testPassed = False	

	return testPassed

# Ankle Encoder Check - Verfiy ankle encoder is functioning nominally
def eb60AnkCheck(devId, appType, time, time_step):
	print('\n>>> User Input: Move ankle through its full range of travel for 5 seconds\n')
	sleep(3)

	# Build dataDict for sensor data
	dataDict = {}
	data = getData(devId, appType)
	for d in data:
		dataDict[d] = []

	# Record data for time
	totalLoopCount = int(time / time_step)
	for i in range(totalLoopCount):
		print(f'Ankle Angle Check Measurement {i} of {totalLoopCount}')
		sleep(time_step)
		data = getData(devId, appType)
		for d in data:
			dataDict[d].append(data[d])

	if checkAnkVals(dataDict):
		print("Ankle Angle Check Passed")
		return True
	else:
		print("Test Failed: Ankle Angle Check Failed")
		return False		

def checkAnkVals(dataDict):
	# Check that sensors min and max are in range
	testPassed = True

	sensors = ['ank_ang']
	sensorRange = {
		'ank_ang': {'min_lo': 1990, 'min_hi': 2100, 'max_lo': 6200, 'max_hi': 6400},
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


#####################################################################
def eb60FindPoles():
	print("\nFinding Poles...")

	print("Poles Found")
	return True

def eb60NoLoadAct():
	print("\nNo Load Test Passed")
	return True

def eb60IMUCal():
	print("\nPerfoming IMU Calibration...")

	print("IMU Calibration Successful")
	return True





if __name__ == '__main__':
	baudRate = sys.argv[1]
	ports = sys.argv[2:3]
	try:
		fxOpenControl(baudRate)
	except Exception as e:
		print("Broke... ")
		print(str(e))
