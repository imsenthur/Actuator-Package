"""/*
 * OPORPState.py
 *
 * AUTOGENERATED FILE! ONLY EDIT IF YOU ARE A MACHINE!
 * CORE:ecdab88c05df58d9ba18cb5e4d6e41c2f32b3e85
 * BUILD:065ba7c027caf247c3a01011370de5bc31a467f7
 *
 *
 * Specification File Created on: 2020-10-20 16:18:08
 * Author: Dephy, Inc.
 *
 */
"""
from ctypes import Structure, c_int

class OPORPState(Structure):
	_pack_ = 1
	_fields_ = [
		("rigid", c_int),
		("id", c_int),
		("state_time", c_int),
		("accelx", c_int),
		("accely", c_int),
		("accelz", c_int),
		("gyrox", c_int),
		("gyroy", c_int),
		("gyroz", c_int),
		("mot_ang", c_int),
		("mot_vel", c_int),
		("mot_acc", c_int),
		("mot_cur", c_int),
		("mot_volt", c_int),
		("batt_volt", c_int),
		("batt_curr", c_int),
		("temperature", c_int),
		("status_mn", c_int),
		("status_ex", c_int),
		("status_re", c_int),
		("genvar_0", c_int),
		("genvar_1", c_int),
		("genvar_2", c_int),
		("genvar_3", c_int),
		("genvar_4", c_int),
		("genvar_5", c_int),
		("genvar_6", c_int),
		("genvar_7", c_int),
		("genvar_8", c_int),
		("genvar_9", c_int),
		("ank_ang", c_int),
		("ank_vel", c_int),
		("SystemTime", c_int)]