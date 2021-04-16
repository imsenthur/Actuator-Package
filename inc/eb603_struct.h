#ifndef EB603_STRUCT_H
#define EB603_STRUCT_H

/*
 * eb603_struct.h
 *
 * AUTOGENERATED FILE! ONLY EDIT IF YOU ARE A MACHINE!
 * CORE:c726adf5d71babe8825d488ec890eea467fcd46a
 * BUILD:3977b4bdcb1d0f012da936cf08ae5e518585b7f6
 *
 *
 * Specification File Created on: 2021-01-27 10:42:38
 * Author: Dephy, Inc.
 *
 */

#include "EB603_device_spec.h"
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#define EB603_SYSTEM_TIME_POS 58
#define EB603_STRUCT_DEVICE_FIELD_COUNT 59
#define EB603_LABEL_MAX_CHAR_LENGTH 19

//This is The Device fields * 10 + deviceField + 1. Ten is the max string length of 2^32 in decimal separated from commas
#define EB603_DATA_STRING_LENGTH 650

#ifdef __cplusplus
extern "C"
{
#endif

#pragma pack(1)

struct EB603State
{
	int rigid;
	int id;
	int state_time;
	int accelx;
	int accely;
	int accelz;
	int gyrox;
	int gyroy;
	int gyroz;
	int mot_ang;
	int mot_vel;
	int mot_acc;
	int mot_cur;
	int mot_volt;
	int batt_volt;
	int batt_curr;
	int temperature;
	int status_mn;
	int status_ex;
	int status_re;
	int genvar_0;
	int genvar_1;
	int genvar_2;
	int genvar_3;
	int genvar_4;
	int genvar_5;
	int genvar_6;
	int genvar_7;
	int genvar_8;
	int genvar_9;
	int genvar_10;
	int genvar_11;
	int genvar_12;
	int genvar_13;
	int genvar_14;
	int ank_ang;
	int ank_vel;
	int shank_ang;
	int shank_vel;
	int global_shank_ang;
	int ank_pos_x;
	int ank_pos_y;
	int ank_pos_z;
	int ank_linear_vel_x;
	int ank_linear_vel_y;
	int ank_linear_vel_z;
	int mot_from_ank;
	int ank_from_mot;
	int trans_ratio;
	int ank_torque;
	int peak_ank_torque;
	int step_energy;
	int step_time;
	int gait_state;
	int intermediate_state;
	int movement;
	int speed;
	int incline;

	//System time:
	int systemTime;
};

#pragma pack()

/// \brief Assigns the data in the buffer to the correct struct parameters
///
///@param EB603 is the struct with the data to be set
///
///@param _deviceStateBuffer is the buffer containing the data to be assigned to the struct
///
///@param systemStartTime the time the system started. If unknown, use 0.
///
void EB603SetData(struct EB603State *eb603, uint32_t _deviceStateBuffer[], int systemStartTime);

/// \brief takes all data and places it into single, comma separated string
///
///@param EB603 is the struct with the data to be placed in the string
///
///@param dataString is where the new string wll be placed 
///
void EB603DataToString(struct EB603State *eb603, char dataString[EB603_DATA_STRING_LENGTH]);

/// \brief retrieves the string equivalent of all parameter names
///
///@param labels is the array of labels containing the parameter names
///
void EB603GetLabels(char labels[EB603_STRUCT_DEVICE_FIELD_COUNT][EB603_LABEL_MAX_CHAR_LENGTH]);

/// \brief retrieves the string equivalent of parameter names starting with state time.  Parameters 
/// prior to state time, such as id,  are not included. 
///
///@param labels is the array of labels containing the parameter names
///
int EB603GetLabelsForLog(char labels[EB603_STRUCT_DEVICE_FIELD_COUNT][EB603_LABEL_MAX_CHAR_LENGTH]);

/// \brief Places data from struct into an array.
///
///@param actpack the data to be converte to an array
///
///@param actpackDataArray the array in which to place the data
///
void EB603StructToDataArray(struct EB603State eb603, int32_t eb603DataArray[EB603_STRUCT_DEVICE_FIELD_COUNT]);

/// \brief Get data based on data position from device communication.
///
///@param actpack the data to access
///
///@param dataPosition the position of data to access
///
///@param dataValid return false if requested data position is invalid
///
int GetEB603DataByDataPosition( struct EB603State eb603, int dataPosition);

#ifdef __cplusplus
}//extern "C"
#endif

#endif //ACTPACK_STRUCT_H
