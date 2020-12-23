import os, sys
from time import sleep
import flexseapython.fxUtil as fxu
import flexseapython.pyFlexsea as fxp
import flexseapython.eb60_test_util as ebu
import testLogFile as tlf
from numpy import mean

PARDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PARDIR)

def fxEB60FinalFunctTest(port, baudRate):
	"""
	Runs intermediate functional test designed for EB60
	"""
	# Setup Device
	devId = fxp.fxOpen(port, baudRate, logLevel = 6)
	fxp.fxStartStreaming(devId, 100, shouldLog = True)
	appType = fxp.fxGetAppType(devId)

	print("\nStarting Intermediate Functional Test...")

	#logFile = tlf.TestLogFile('EB60_Final_Functional_Test')

	# Run tests
	try:
		assert ebu.main(devId), 'Bummer...'

	except AssertionError as err:
		print('Test Failed: {}'.format(err))

	# Close device
	fxp.fxClose(devId)
	return True

##########################################################################
# Test Functions





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
