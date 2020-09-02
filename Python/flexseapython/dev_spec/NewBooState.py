"""
Please note that this file is generated by a script!
Please do not make any changes to this file!
"""
from ctypes import Structure, c_int

class NewBooState(Structure):
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
		("status_Mn", c_int),
		("status_Ex", c_int),
		("status_Re", c_int),
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
		("shank_ang", c_int),
		("shank_vel", c_int),
		("global_shank_ang", c_int),
		("ank_pos_x", c_int),
		("ank_pos_y", c_int),
		("ank_pos_z", c_int),
		("ank_linear_vel_x", c_int),
		("ank_linear_vel_y", c_int),
		("ank_linear_vel_z", c_int),
		("ank_torque", c_int),
		("step_energy", c_int),
		("step_time", c_int),
		("gait_state", c_int),
		("intermediate_state", c_int),
		("movement", c_int),
		("SystemTime", c_int)]
