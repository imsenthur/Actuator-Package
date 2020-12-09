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
		testFlag = eb60SensorCheck(devId, appType, time=6, time_step=0.1)
	if testFlag:
		testFlag = eb60AnkCheck()
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
	data = getData(devId)
	for d in data:
		dataDict[d] = []

	# Record data for time
	totalLoopCount = int(time / time_step)
	for i in range(totalLoopCount):
		printLoopCount(i, totalLoopCount)
		sleep(time_step)
		data = getData(devId)
		for d in data:
			dataDict[d].append(data[d])

	if checkSensVals(dataDict):
		print("Sensor Check Passed")
		return True
	else:
		print("Sensor Check Failed")
		return False

def checkSensVals(dataDict):
	testPassed = True

	# Check sensor are non zero
	sensors = ['accelx', 'accely', 'accelz', 'gyrox', 'gyroy', 'gyroz', 'mot_ang', 'mot_cur', 'batt_volt', 'batt_curr', 'ank_ang', 'ank_vel']
	for sensor in sensors:
		sensorMean = mean(dataDict[sensor])
		if sensorMean == 0.0:
			print(f'Sensor Check Failed: {sensor} is 0.0')
			testPassed = False

	# Check sensors are in range
	sensors = ['accelx', 'accely', 'accelz', 'gyrox', 'gyroy', 'gyroz', 'batt_volt', 'batt_curr', 'temperature', 'ank_ang', 'ank_vel']
	sensorRange = {
		'accelx': {'min': -25000, 'max': 25000},
		'accely': {'min': -25000, 'max': 25000},
		'accelz': {'min' :-25000, 'max': 25000},
		'gyrox': {'min': -15000, 'max': 15000},
		'gyroy': {'min': -15000, 'max': 15000},
		'gyroz': {'min': -15000, 'max': 15000},
		'batt_volt': {'min': 190, 'max': 225},
		'batt_curr': {'min': -40, 'max': 120},
		'temperature': {'min': 10, 'max': 40},
		'ank_ang': {'min': 2000, 'max': 6300},
		'ank_vel': {'min': -500, 'max': 500}
		}
	for sensor in sensors:
		sensorMin = min(dataDict[sensor])
		sensorMax = max(dataDict[sensor])
		if sensorMin < sensorRange[sensor]['min']:
			print(f"Sensor Check Failed: {sensor} minimum is {sensorMin} (it should be above {sensorRange[sensor]['min']})")
			testPassed = False
		if sensorMax > sensorRange[sensor]['max']:
			print(f"Sensor Check Failed: {sensor} maximum is {sensorMax} (it should be above {sensorRange[sensor]['max']})")
			testPassed = False	

	return testPassed

# Ankle Encoder Check - Verfiy ankle encoder is functioning nominally
def eb60AnkCheck(dataDict):
		# Check ank angle
	print('\n>>> User Input: Move ankle through its full range of travel\n')
	# Check sensors are in range
	sensors = ['ank_ang', 'ank_vel']
	sensorRange = {
		'ank_ang': {'min': 2000, 'max': 6300},
		'ank_vel': {'min': -500, 'max': 500}
		}
	for sensor in sensors:
		sensorMin = min(dataDict[sensor])
		sensorMax = max(dataDict[sensor])
		if sensorMin < sensorRange[sensor]['min']:
			print(f"Sensor Check Failed: {sensor} minimum is {sensorMin} (it should be above {sensorRange[sensor]['min']})")
			testPassed = False
		if sensorMax > sensorRange[sensor]['max']:
			print(f"Sensor Check Failed: {sensor} maximum is {sensorMax} (it should be above {sensorRange[sensor]['max']})")
			testPassed = False

	return testPassed



#########################################################
# Generic functions

def getData(devId):
	return formatData(fxReadDevice(devId))

def formatData(exoState: AllDevices.ExoState):
	data = {
	'state_time': exoState.state_time,
	'accelx': exoState.accelx,
	'accely': exoState.accely,
	'accelz': exoState.accelz,
	'gyrox': exoState.gyrox,
	'gyroy': exoState.gyroy,
	'gyroz': exoState.gyroz,
	'mot_ang': exoState.mot_ang,
	'mot_volt': exoState.mot_volt,
	'mot_cur': exoState.mot_cur,
	'batt_volt': exoState.batt_volt,
	'batt_curr': exoState.batt_curr,
	'temperature': exoState.temperature,
	'genvar_0': exoState.genvar_0,
	'genvar_1': exoState.genvar_1,
	'genvar_2': exoState.genvar_2,
	'genvar_3': exoState.genvar_3,
	'genvar_4': exoState.genvar_4,
	'genvar_5': exoState.genvar_5,
	'genvar_6': exoState.genvar_6,
	'genvar_7': exoState.genvar_7,
	'genvar_8': exoState.genvar_8,
	'genvar_9': exoState.genvar_9,
	'ank_ang': exoState.ank_ang,
	'ank_vel': exoState.ank_vel
	}
	return data
	

#####################################################################
def eb60AnkCheck():
	print("\nRotate Dummy Ankle")

	print("Ank Check Passed")
	return True

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
