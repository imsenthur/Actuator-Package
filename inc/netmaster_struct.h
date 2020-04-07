#ifndef NETMASTER_STRUCT_H
#define NETMASTER_STRUCT_H
/*
 * netmaster_struct.h
 *
 * AUTOGENERATED FILE! ONLY EDIT IF YOU ARE A MACHINE!
 *
 *
 *  Created on: 2020-04-06 21:10:55.582858
 *      Author: Dephy Inc
 */

#include "NetMaster_device_spec.h "
#include <sstream> 
#include <stdio.h> 
#include <string> 

#include <ctime> 

#define NETMASTER_SYSTEM_TIME_POS 72
#define NETMASTER_STRUCT_DEVICE_FIELD_COUNT 73

struct NetMasterState 
 { 

	int netmaster_netmaster;
	int netmaster_id;
	int netmaster_state_time;
	int netmaster_genvar_0;
	int netmaster_genvar_1;
	int netmaster_genvar_2;
	int netmaster_genvar_3;
	int netmaster_status;
	int netmaster_a_accelx;
	int netmaster_a_accely;
	int netmaster_a_accelz;
	int netmaster_a_gyrox;
	int netmaster_a_gyroy;
	int netmaster_a_gyroz;
	int netmaster_a_pressure;
	int netmaster_a_status;
	int netmaster_b_accelx;
	int netmaster_b_accely;
	int netmaster_b_accelz;
	int netmaster_b_gyrox;
	int netmaster_b_gyroy;
	int netmaster_b_gyroz;
	int netmaster_b_pressure;
	int netmaster_b_status;
	int netmaster_c_accelx;
	int netmaster_c_accely;
	int netmaster_c_accelz;
	int netmaster_c_gyrox;
	int netmaster_c_gyroy;
	int netmaster_c_gyroz;
	int netmaster_c_pressure;
	int netmaster_c_status;
	int netmaster_d_accelx;
	int netmaster_d_accely;
	int netmaster_d_accelz;
	int netmaster_d_gyrox;
	int netmaster_d_gyroy;
	int netmaster_d_gyroz;
	int netmaster_d_pressure;
	int netmaster_d_status;
	int netmaster_e_accelx;
	int netmaster_e_accely;
	int netmaster_e_accelz;
	int netmaster_e_gyrox;
	int netmaster_e_gyroy;
	int netmaster_e_gyroz;
	int netmaster_e_pressure;
	int netmaster_e_status;
	int netmaster_f_accelx;
	int netmaster_f_accely;
	int netmaster_f_accelz;
	int netmaster_f_gyrox;
	int netmaster_f_gyroy;
	int netmaster_f_gyroz;
	int netmaster_f_pressure;
	int netmaster_f_status;
	int netmaster_g_accelx;
	int netmaster_g_accely;
	int netmaster_g_accelz;
	int netmaster_g_gyrox;
	int netmaster_g_gyroy;
	int netmaster_g_gyroz;
	int netmaster_g_pressure;
	int netmaster_g_status;
	int netmaster_h_accelx;
	int netmaster_h_accely;
	int netmaster_h_accelz;
	int netmaster_h_gyrox;
	int netmaster_h_gyroy;
	int netmaster_h_gyroz;
	int netmaster_h_pressure;
	int netmaster_h_status;
	//the system time
	clock_t systemTime;
	uint32_t deviceData[NETMASTER_STRUCT_DEVICE_FIELD_COUNT];

	// sets the data.  Requires system start time.  If unavailable, set to 0
	void setData(uint32_t _deviceStateBuffer[], clock_t systemStartTime) 
 	{
		netmaster_netmaster=_deviceStateBuffer[NETMASTER_NETMASTER_POS ];
		deviceData[NETMASTER_NETMASTER_POS ]=_deviceStateBuffer[NETMASTER_NETMASTER_POS ];
		netmaster_id=_deviceStateBuffer[NETMASTER_ID_POS ];
		deviceData[NETMASTER_ID_POS ]=_deviceStateBuffer[NETMASTER_ID_POS ];
		netmaster_state_time=_deviceStateBuffer[NETMASTER_STATE_TIME_POS ];
		deviceData[NETMASTER_STATE_TIME_POS ]=_deviceStateBuffer[NETMASTER_STATE_TIME_POS ];
		netmaster_genvar_0=_deviceStateBuffer[NETMASTER_GENVAR_0_POS ];
		deviceData[NETMASTER_GENVAR_0_POS ]=_deviceStateBuffer[NETMASTER_GENVAR_0_POS ];
		netmaster_genvar_1=_deviceStateBuffer[NETMASTER_GENVAR_1_POS ];
		deviceData[NETMASTER_GENVAR_1_POS ]=_deviceStateBuffer[NETMASTER_GENVAR_1_POS ];
		netmaster_genvar_2=_deviceStateBuffer[NETMASTER_GENVAR_2_POS ];
		deviceData[NETMASTER_GENVAR_2_POS ]=_deviceStateBuffer[NETMASTER_GENVAR_2_POS ];
		netmaster_genvar_3=_deviceStateBuffer[NETMASTER_GENVAR_3_POS ];
		deviceData[NETMASTER_GENVAR_3_POS ]=_deviceStateBuffer[NETMASTER_GENVAR_3_POS ];
		netmaster_status=_deviceStateBuffer[NETMASTER_STATUS_POS ];
		deviceData[NETMASTER_STATUS_POS ]=_deviceStateBuffer[NETMASTER_STATUS_POS ];
		netmaster_a_accelx=_deviceStateBuffer[NETMASTER_A_ACCELX_POS ];
		deviceData[NETMASTER_A_ACCELX_POS ]=_deviceStateBuffer[NETMASTER_A_ACCELX_POS ];
		netmaster_a_accely=_deviceStateBuffer[NETMASTER_A_ACCELY_POS ];
		deviceData[NETMASTER_A_ACCELY_POS ]=_deviceStateBuffer[NETMASTER_A_ACCELY_POS ];
		netmaster_a_accelz=_deviceStateBuffer[NETMASTER_A_ACCELZ_POS ];
		deviceData[NETMASTER_A_ACCELZ_POS ]=_deviceStateBuffer[NETMASTER_A_ACCELZ_POS ];
		netmaster_a_gyrox=_deviceStateBuffer[NETMASTER_A_GYROX_POS ];
		deviceData[NETMASTER_A_GYROX_POS ]=_deviceStateBuffer[NETMASTER_A_GYROX_POS ];
		netmaster_a_gyroy=_deviceStateBuffer[NETMASTER_A_GYROY_POS ];
		deviceData[NETMASTER_A_GYROY_POS ]=_deviceStateBuffer[NETMASTER_A_GYROY_POS ];
		netmaster_a_gyroz=_deviceStateBuffer[NETMASTER_A_GYROZ_POS ];
		deviceData[NETMASTER_A_GYROZ_POS ]=_deviceStateBuffer[NETMASTER_A_GYROZ_POS ];
		netmaster_a_pressure=_deviceStateBuffer[NETMASTER_A_PRESSURE_POS ];
		deviceData[NETMASTER_A_PRESSURE_POS ]=_deviceStateBuffer[NETMASTER_A_PRESSURE_POS ];
		netmaster_a_status=_deviceStateBuffer[NETMASTER_A_STATUS_POS ];
		deviceData[NETMASTER_A_STATUS_POS ]=_deviceStateBuffer[NETMASTER_A_STATUS_POS ];
		netmaster_b_accelx=_deviceStateBuffer[NETMASTER_B_ACCELX_POS ];
		deviceData[NETMASTER_B_ACCELX_POS ]=_deviceStateBuffer[NETMASTER_B_ACCELX_POS ];
		netmaster_b_accely=_deviceStateBuffer[NETMASTER_B_ACCELY_POS ];
		deviceData[NETMASTER_B_ACCELY_POS ]=_deviceStateBuffer[NETMASTER_B_ACCELY_POS ];
		netmaster_b_accelz=_deviceStateBuffer[NETMASTER_B_ACCELZ_POS ];
		deviceData[NETMASTER_B_ACCELZ_POS ]=_deviceStateBuffer[NETMASTER_B_ACCELZ_POS ];
		netmaster_b_gyrox=_deviceStateBuffer[NETMASTER_B_GYROX_POS ];
		deviceData[NETMASTER_B_GYROX_POS ]=_deviceStateBuffer[NETMASTER_B_GYROX_POS ];
		netmaster_b_gyroy=_deviceStateBuffer[NETMASTER_B_GYROY_POS ];
		deviceData[NETMASTER_B_GYROY_POS ]=_deviceStateBuffer[NETMASTER_B_GYROY_POS ];
		netmaster_b_gyroz=_deviceStateBuffer[NETMASTER_B_GYROZ_POS ];
		deviceData[NETMASTER_B_GYROZ_POS ]=_deviceStateBuffer[NETMASTER_B_GYROZ_POS ];
		netmaster_b_pressure=_deviceStateBuffer[NETMASTER_B_PRESSURE_POS ];
		deviceData[NETMASTER_B_PRESSURE_POS ]=_deviceStateBuffer[NETMASTER_B_PRESSURE_POS ];
		netmaster_b_status=_deviceStateBuffer[NETMASTER_B_STATUS_POS ];
		deviceData[NETMASTER_B_STATUS_POS ]=_deviceStateBuffer[NETMASTER_B_STATUS_POS ];
		netmaster_c_accelx=_deviceStateBuffer[NETMASTER_C_ACCELX_POS ];
		deviceData[NETMASTER_C_ACCELX_POS ]=_deviceStateBuffer[NETMASTER_C_ACCELX_POS ];
		netmaster_c_accely=_deviceStateBuffer[NETMASTER_C_ACCELY_POS ];
		deviceData[NETMASTER_C_ACCELY_POS ]=_deviceStateBuffer[NETMASTER_C_ACCELY_POS ];
		netmaster_c_accelz=_deviceStateBuffer[NETMASTER_C_ACCELZ_POS ];
		deviceData[NETMASTER_C_ACCELZ_POS ]=_deviceStateBuffer[NETMASTER_C_ACCELZ_POS ];
		netmaster_c_gyrox=_deviceStateBuffer[NETMASTER_C_GYROX_POS ];
		deviceData[NETMASTER_C_GYROX_POS ]=_deviceStateBuffer[NETMASTER_C_GYROX_POS ];
		netmaster_c_gyroy=_deviceStateBuffer[NETMASTER_C_GYROY_POS ];
		deviceData[NETMASTER_C_GYROY_POS ]=_deviceStateBuffer[NETMASTER_C_GYROY_POS ];
		netmaster_c_gyroz=_deviceStateBuffer[NETMASTER_C_GYROZ_POS ];
		deviceData[NETMASTER_C_GYROZ_POS ]=_deviceStateBuffer[NETMASTER_C_GYROZ_POS ];
		netmaster_c_pressure=_deviceStateBuffer[NETMASTER_C_PRESSURE_POS ];
		deviceData[NETMASTER_C_PRESSURE_POS ]=_deviceStateBuffer[NETMASTER_C_PRESSURE_POS ];
		netmaster_c_status=_deviceStateBuffer[NETMASTER_C_STATUS_POS ];
		deviceData[NETMASTER_C_STATUS_POS ]=_deviceStateBuffer[NETMASTER_C_STATUS_POS ];
		netmaster_d_accelx=_deviceStateBuffer[NETMASTER_D_ACCELX_POS ];
		deviceData[NETMASTER_D_ACCELX_POS ]=_deviceStateBuffer[NETMASTER_D_ACCELX_POS ];
		netmaster_d_accely=_deviceStateBuffer[NETMASTER_D_ACCELY_POS ];
		deviceData[NETMASTER_D_ACCELY_POS ]=_deviceStateBuffer[NETMASTER_D_ACCELY_POS ];
		netmaster_d_accelz=_deviceStateBuffer[NETMASTER_D_ACCELZ_POS ];
		deviceData[NETMASTER_D_ACCELZ_POS ]=_deviceStateBuffer[NETMASTER_D_ACCELZ_POS ];
		netmaster_d_gyrox=_deviceStateBuffer[NETMASTER_D_GYROX_POS ];
		deviceData[NETMASTER_D_GYROX_POS ]=_deviceStateBuffer[NETMASTER_D_GYROX_POS ];
		netmaster_d_gyroy=_deviceStateBuffer[NETMASTER_D_GYROY_POS ];
		deviceData[NETMASTER_D_GYROY_POS ]=_deviceStateBuffer[NETMASTER_D_GYROY_POS ];
		netmaster_d_gyroz=_deviceStateBuffer[NETMASTER_D_GYROZ_POS ];
		deviceData[NETMASTER_D_GYROZ_POS ]=_deviceStateBuffer[NETMASTER_D_GYROZ_POS ];
		netmaster_d_pressure=_deviceStateBuffer[NETMASTER_D_PRESSURE_POS ];
		deviceData[NETMASTER_D_PRESSURE_POS ]=_deviceStateBuffer[NETMASTER_D_PRESSURE_POS ];
		netmaster_d_status=_deviceStateBuffer[NETMASTER_D_STATUS_POS ];
		deviceData[NETMASTER_D_STATUS_POS ]=_deviceStateBuffer[NETMASTER_D_STATUS_POS ];
		netmaster_e_accelx=_deviceStateBuffer[NETMASTER_E_ACCELX_POS ];
		deviceData[NETMASTER_E_ACCELX_POS ]=_deviceStateBuffer[NETMASTER_E_ACCELX_POS ];
		netmaster_e_accely=_deviceStateBuffer[NETMASTER_E_ACCELY_POS ];
		deviceData[NETMASTER_E_ACCELY_POS ]=_deviceStateBuffer[NETMASTER_E_ACCELY_POS ];
		netmaster_e_accelz=_deviceStateBuffer[NETMASTER_E_ACCELZ_POS ];
		deviceData[NETMASTER_E_ACCELZ_POS ]=_deviceStateBuffer[NETMASTER_E_ACCELZ_POS ];
		netmaster_e_gyrox=_deviceStateBuffer[NETMASTER_E_GYROX_POS ];
		deviceData[NETMASTER_E_GYROX_POS ]=_deviceStateBuffer[NETMASTER_E_GYROX_POS ];
		netmaster_e_gyroy=_deviceStateBuffer[NETMASTER_E_GYROY_POS ];
		deviceData[NETMASTER_E_GYROY_POS ]=_deviceStateBuffer[NETMASTER_E_GYROY_POS ];
		netmaster_e_gyroz=_deviceStateBuffer[NETMASTER_E_GYROZ_POS ];
		deviceData[NETMASTER_E_GYROZ_POS ]=_deviceStateBuffer[NETMASTER_E_GYROZ_POS ];
		netmaster_e_pressure=_deviceStateBuffer[NETMASTER_E_PRESSURE_POS ];
		deviceData[NETMASTER_E_PRESSURE_POS ]=_deviceStateBuffer[NETMASTER_E_PRESSURE_POS ];
		netmaster_e_status=_deviceStateBuffer[NETMASTER_E_STATUS_POS ];
		deviceData[NETMASTER_E_STATUS_POS ]=_deviceStateBuffer[NETMASTER_E_STATUS_POS ];
		netmaster_f_accelx=_deviceStateBuffer[NETMASTER_F_ACCELX_POS ];
		deviceData[NETMASTER_F_ACCELX_POS ]=_deviceStateBuffer[NETMASTER_F_ACCELX_POS ];
		netmaster_f_accely=_deviceStateBuffer[NETMASTER_F_ACCELY_POS ];
		deviceData[NETMASTER_F_ACCELY_POS ]=_deviceStateBuffer[NETMASTER_F_ACCELY_POS ];
		netmaster_f_accelz=_deviceStateBuffer[NETMASTER_F_ACCELZ_POS ];
		deviceData[NETMASTER_F_ACCELZ_POS ]=_deviceStateBuffer[NETMASTER_F_ACCELZ_POS ];
		netmaster_f_gyrox=_deviceStateBuffer[NETMASTER_F_GYROX_POS ];
		deviceData[NETMASTER_F_GYROX_POS ]=_deviceStateBuffer[NETMASTER_F_GYROX_POS ];
		netmaster_f_gyroy=_deviceStateBuffer[NETMASTER_F_GYROY_POS ];
		deviceData[NETMASTER_F_GYROY_POS ]=_deviceStateBuffer[NETMASTER_F_GYROY_POS ];
		netmaster_f_gyroz=_deviceStateBuffer[NETMASTER_F_GYROZ_POS ];
		deviceData[NETMASTER_F_GYROZ_POS ]=_deviceStateBuffer[NETMASTER_F_GYROZ_POS ];
		netmaster_f_pressure=_deviceStateBuffer[NETMASTER_F_PRESSURE_POS ];
		deviceData[NETMASTER_F_PRESSURE_POS ]=_deviceStateBuffer[NETMASTER_F_PRESSURE_POS ];
		netmaster_f_status=_deviceStateBuffer[NETMASTER_F_STATUS_POS ];
		deviceData[NETMASTER_F_STATUS_POS ]=_deviceStateBuffer[NETMASTER_F_STATUS_POS ];
		netmaster_g_accelx=_deviceStateBuffer[NETMASTER_G_ACCELX_POS ];
		deviceData[NETMASTER_G_ACCELX_POS ]=_deviceStateBuffer[NETMASTER_G_ACCELX_POS ];
		netmaster_g_accely=_deviceStateBuffer[NETMASTER_G_ACCELY_POS ];
		deviceData[NETMASTER_G_ACCELY_POS ]=_deviceStateBuffer[NETMASTER_G_ACCELY_POS ];
		netmaster_g_accelz=_deviceStateBuffer[NETMASTER_G_ACCELZ_POS ];
		deviceData[NETMASTER_G_ACCELZ_POS ]=_deviceStateBuffer[NETMASTER_G_ACCELZ_POS ];
		netmaster_g_gyrox=_deviceStateBuffer[NETMASTER_G_GYROX_POS ];
		deviceData[NETMASTER_G_GYROX_POS ]=_deviceStateBuffer[NETMASTER_G_GYROX_POS ];
		netmaster_g_gyroy=_deviceStateBuffer[NETMASTER_G_GYROY_POS ];
		deviceData[NETMASTER_G_GYROY_POS ]=_deviceStateBuffer[NETMASTER_G_GYROY_POS ];
		netmaster_g_gyroz=_deviceStateBuffer[NETMASTER_G_GYROZ_POS ];
		deviceData[NETMASTER_G_GYROZ_POS ]=_deviceStateBuffer[NETMASTER_G_GYROZ_POS ];
		netmaster_g_pressure=_deviceStateBuffer[NETMASTER_G_PRESSURE_POS ];
		deviceData[NETMASTER_G_PRESSURE_POS ]=_deviceStateBuffer[NETMASTER_G_PRESSURE_POS ];
		netmaster_g_status=_deviceStateBuffer[NETMASTER_G_STATUS_POS ];
		deviceData[NETMASTER_G_STATUS_POS ]=_deviceStateBuffer[NETMASTER_G_STATUS_POS ];
		netmaster_h_accelx=_deviceStateBuffer[NETMASTER_H_ACCELX_POS ];
		deviceData[NETMASTER_H_ACCELX_POS ]=_deviceStateBuffer[NETMASTER_H_ACCELX_POS ];
		netmaster_h_accely=_deviceStateBuffer[NETMASTER_H_ACCELY_POS ];
		deviceData[NETMASTER_H_ACCELY_POS ]=_deviceStateBuffer[NETMASTER_H_ACCELY_POS ];
		netmaster_h_accelz=_deviceStateBuffer[NETMASTER_H_ACCELZ_POS ];
		deviceData[NETMASTER_H_ACCELZ_POS ]=_deviceStateBuffer[NETMASTER_H_ACCELZ_POS ];
		netmaster_h_gyrox=_deviceStateBuffer[NETMASTER_H_GYROX_POS ];
		deviceData[NETMASTER_H_GYROX_POS ]=_deviceStateBuffer[NETMASTER_H_GYROX_POS ];
		netmaster_h_gyroy=_deviceStateBuffer[NETMASTER_H_GYROY_POS ];
		deviceData[NETMASTER_H_GYROY_POS ]=_deviceStateBuffer[NETMASTER_H_GYROY_POS ];
		netmaster_h_gyroz=_deviceStateBuffer[NETMASTER_H_GYROZ_POS ];
		deviceData[NETMASTER_H_GYROZ_POS ]=_deviceStateBuffer[NETMASTER_H_GYROZ_POS ];
		netmaster_h_pressure=_deviceStateBuffer[NETMASTER_H_PRESSURE_POS ];
		deviceData[NETMASTER_H_PRESSURE_POS ]=_deviceStateBuffer[NETMASTER_H_PRESSURE_POS ];
		netmaster_h_status=_deviceStateBuffer[NETMASTER_H_STATUS_POS ];
		deviceData[NETMASTER_H_STATUS_POS ]=_deviceStateBuffer[NETMASTER_H_STATUS_POS ];

		systemTime= systemStartTime-clock();
		deviceData[NETMASTER_SYSTEM_TIME_POS]=systemTime;
	};

	void sendToStream(std::stringstream &ss) 
 	{
		ss << netmaster_netmaster <<",";
		ss << netmaster_id <<",";
		ss << netmaster_state_time <<",";
		ss << netmaster_genvar_0 <<",";
		ss << netmaster_genvar_1 <<",";
		ss << netmaster_genvar_2 <<",";
		ss << netmaster_genvar_3 <<",";
		ss << netmaster_status <<",";
		ss << netmaster_a_accelx <<",";
		ss << netmaster_a_accely <<",";
		ss << netmaster_a_accelz <<",";
		ss << netmaster_a_gyrox <<",";
		ss << netmaster_a_gyroy <<",";
		ss << netmaster_a_gyroz <<",";
		ss << netmaster_a_pressure <<",";
		ss << netmaster_a_status <<",";
		ss << netmaster_b_accelx <<",";
		ss << netmaster_b_accely <<",";
		ss << netmaster_b_accelz <<",";
		ss << netmaster_b_gyrox <<",";
		ss << netmaster_b_gyroy <<",";
		ss << netmaster_b_gyroz <<",";
		ss << netmaster_b_pressure <<",";
		ss << netmaster_b_status <<",";
		ss << netmaster_c_accelx <<",";
		ss << netmaster_c_accely <<",";
		ss << netmaster_c_accelz <<",";
		ss << netmaster_c_gyrox <<",";
		ss << netmaster_c_gyroy <<",";
		ss << netmaster_c_gyroz <<",";
		ss << netmaster_c_pressure <<",";
		ss << netmaster_c_status <<",";
		ss << netmaster_d_accelx <<",";
		ss << netmaster_d_accely <<",";
		ss << netmaster_d_accelz <<",";
		ss << netmaster_d_gyrox <<",";
		ss << netmaster_d_gyroy <<",";
		ss << netmaster_d_gyroz <<",";
		ss << netmaster_d_pressure <<",";
		ss << netmaster_d_status <<",";
		ss << netmaster_e_accelx <<",";
		ss << netmaster_e_accely <<",";
		ss << netmaster_e_accelz <<",";
		ss << netmaster_e_gyrox <<",";
		ss << netmaster_e_gyroy <<",";
		ss << netmaster_e_gyroz <<",";
		ss << netmaster_e_pressure <<",";
		ss << netmaster_e_status <<",";
		ss << netmaster_f_accelx <<",";
		ss << netmaster_f_accely <<",";
		ss << netmaster_f_accelz <<",";
		ss << netmaster_f_gyrox <<",";
		ss << netmaster_f_gyroy <<",";
		ss << netmaster_f_gyroz <<",";
		ss << netmaster_f_pressure <<",";
		ss << netmaster_f_status <<",";
		ss << netmaster_g_accelx <<",";
		ss << netmaster_g_accely <<",";
		ss << netmaster_g_accelz <<",";
		ss << netmaster_g_gyrox <<",";
		ss << netmaster_g_gyroy <<",";
		ss << netmaster_g_gyroz <<",";
		ss << netmaster_g_pressure <<",";
		ss << netmaster_g_status <<",";
		ss << netmaster_h_accelx <<",";
		ss << netmaster_h_accely <<",";
		ss << netmaster_h_accelz <<",";
		ss << netmaster_h_gyrox <<",";
		ss << netmaster_h_gyroy <<",";
		ss << netmaster_h_gyroz <<",";
		ss << netmaster_h_pressure <<",";
		ss << netmaster_h_status <<",";
		ss<<systemTime<<",";
	};

	 static void GetLabels(std::string *labels) 
 	{
		labels[NETMASTER_NETMASTER_POS]= "netmaster";
		labels[NETMASTER_ID_POS]= "id";
		labels[NETMASTER_STATE_TIME_POS]= "state_time";
		labels[NETMASTER_GENVAR_0_POS]= "genVar_0";
		labels[NETMASTER_GENVAR_1_POS]= "genVar_1";
		labels[NETMASTER_GENVAR_2_POS]= "genVar_2";
		labels[NETMASTER_GENVAR_3_POS]= "genVar_3";
		labels[NETMASTER_STATUS_POS]= "status";
		labels[NETMASTER_A_ACCELX_POS]= "A_accelx";
		labels[NETMASTER_A_ACCELY_POS]= "A_accely";
		labels[NETMASTER_A_ACCELZ_POS]= "A_accelz";
		labels[NETMASTER_A_GYROX_POS]= "A_gyrox";
		labels[NETMASTER_A_GYROY_POS]= "A_gyroy";
		labels[NETMASTER_A_GYROZ_POS]= "A_gyroz";
		labels[NETMASTER_A_PRESSURE_POS]= "A_pressure";
		labels[NETMASTER_A_STATUS_POS]= "A_status";
		labels[NETMASTER_B_ACCELX_POS]= "B_accelx";
		labels[NETMASTER_B_ACCELY_POS]= "B_accely";
		labels[NETMASTER_B_ACCELZ_POS]= "B_accelz";
		labels[NETMASTER_B_GYROX_POS]= "B_gyrox";
		labels[NETMASTER_B_GYROY_POS]= "B_gyroy";
		labels[NETMASTER_B_GYROZ_POS]= "B_gyroz";
		labels[NETMASTER_B_PRESSURE_POS]= "B_pressure";
		labels[NETMASTER_B_STATUS_POS]= "B_status";
		labels[NETMASTER_C_ACCELX_POS]= "C_accelx";
		labels[NETMASTER_C_ACCELY_POS]= "C_accely";
		labels[NETMASTER_C_ACCELZ_POS]= "C_accelz";
		labels[NETMASTER_C_GYROX_POS]= "C_gyrox";
		labels[NETMASTER_C_GYROY_POS]= "C_gyroy";
		labels[NETMASTER_C_GYROZ_POS]= "C_gyroz";
		labels[NETMASTER_C_PRESSURE_POS]= "C_pressure";
		labels[NETMASTER_C_STATUS_POS]= "C_status";
		labels[NETMASTER_D_ACCELX_POS]= "D_accelx";
		labels[NETMASTER_D_ACCELY_POS]= "D_accely";
		labels[NETMASTER_D_ACCELZ_POS]= "D_accelz";
		labels[NETMASTER_D_GYROX_POS]= "D_gyrox";
		labels[NETMASTER_D_GYROY_POS]= "D_gyroy";
		labels[NETMASTER_D_GYROZ_POS]= "D_gyroz";
		labels[NETMASTER_D_PRESSURE_POS]= "D_pressure";
		labels[NETMASTER_D_STATUS_POS]= "D_status";
		labels[NETMASTER_E_ACCELX_POS]= "E_accelx";
		labels[NETMASTER_E_ACCELY_POS]= "E_accely";
		labels[NETMASTER_E_ACCELZ_POS]= "E_accelz";
		labels[NETMASTER_E_GYROX_POS]= "E_gyrox";
		labels[NETMASTER_E_GYROY_POS]= "E_gyroy";
		labels[NETMASTER_E_GYROZ_POS]= "E_gyroz";
		labels[NETMASTER_E_PRESSURE_POS]= "E_pressure";
		labels[NETMASTER_E_STATUS_POS]= "E_status";
		labels[NETMASTER_F_ACCELX_POS]= "F_accelx";
		labels[NETMASTER_F_ACCELY_POS]= "F_accely";
		labels[NETMASTER_F_ACCELZ_POS]= "F_accelz";
		labels[NETMASTER_F_GYROX_POS]= "F_gyrox";
		labels[NETMASTER_F_GYROY_POS]= "F_gyroy";
		labels[NETMASTER_F_GYROZ_POS]= "F_gyroz";
		labels[NETMASTER_F_PRESSURE_POS]= "F_pressure";
		labels[NETMASTER_F_STATUS_POS]= "F_status";
		labels[NETMASTER_G_ACCELX_POS]= "G_accelx";
		labels[NETMASTER_G_ACCELY_POS]= "G_accely";
		labels[NETMASTER_G_ACCELZ_POS]= "G_accelz";
		labels[NETMASTER_G_GYROX_POS]= "G_gyrox";
		labels[NETMASTER_G_GYROY_POS]= "G_gyroy";
		labels[NETMASTER_G_GYROZ_POS]= "G_gyroz";
		labels[NETMASTER_G_PRESSURE_POS]= "G_pressure";
		labels[NETMASTER_G_STATUS_POS]= "G_status";
		labels[NETMASTER_H_ACCELX_POS]= "H_accelx";
		labels[NETMASTER_H_ACCELY_POS]= "H_accely";
		labels[NETMASTER_H_ACCELZ_POS]= "H_accelz";
		labels[NETMASTER_H_GYROX_POS]= "H_gyrox";
		labels[NETMASTER_H_GYROY_POS]= "H_gyroy";
		labels[NETMASTER_H_GYROZ_POS]= "H_gyroz";
		labels[NETMASTER_H_PRESSURE_POS]= "H_pressure";
		labels[NETMASTER_H_STATUS_POS]= "H_status";
		labels[NETMASTER_SYSTEM_TIME_POS]="sys_time";
	};
}; 
#endif ////NETMASTER_STRUCT_H
