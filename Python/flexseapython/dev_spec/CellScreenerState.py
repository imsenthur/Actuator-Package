"""
Please note that this file is generated by a script!
Please do not make any changes to this file!
"""
from ctypes import Structure, c_int

class CellScreenerState(Structure):
	_pack_ = 1
	_fields_ = [
		("cellscreener", c_int),
		("id", c_int),
		("state_time", c_int),
		("current", c_int),
		("voltage", c_int),
		("fsm_state", c_int),
		("button", c_int),
		("leds", c_int),
		("genVar_0", c_int),
		("genVar_1", c_int),
		("genVar_2", c_int),
		("genVar_3", c_int),
		("status", c_int),
		("p_timestamp", c_int),
		("p_current", c_int),
		("p_open_voltage", c_int),
		("p_voltage", c_int),
		("p_dV", c_int),
		("p_esr", c_int),
		("p_bin", c_int),
		("SystemTime", c_int)]
