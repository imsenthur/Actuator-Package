#ifndef NEWBOO_STRUCT_H
#define NEWBOO_STRUCT_H

/*
 * newboo_struct.h
 *
 * AUTOGENERATED FILE! ONLY EDIT IF YOU ARE A MACHINE!
 * CORE:ade73c292230f7720965b48f18d4861e57330197
 * BUILD:3f143a9a401d81bb7cd63145fed40924cc32010f
 *
 *
 * Specification File Created on: 2020-11-24 15:20:38
 * Author: Dephy, Inc.
 *
 */

#include "NewBoo_device_spec.h"
#include <stdio.h> 
#include <time.h> 
#include <string.h> 
#include <stdint.h> 

#include <stdbool.h> 

#define NEWBOO_SYSTEM_TIME_POS 53
#define NEWBOO_STRUCT_DEVICE_FIELD_COUNT 54
#define NEWBOO_LABEL_MAX_CHAR_LENGTH 19

//This is The Device fields*10 + deviceField+1. Ten is the max string length of 2^32 in decimal separated from commas
#define NEWBOO_DATA_STRING_LENGTH 595

#ifdef __cplusplus
extern "C"
{
#endif

#pragma pack(1)

struct NewBooState
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

	//the system time
	int systemTime;
};

#pragma pack()

/// \brief Assigns the data in the buffer to the correct struct parameters
///
///@param NewBoo is the struct with the data to be set
///
///@param _deviceStateBuffer is the buffer containing the data to be assigned to the struct
///
///@param systemStartTime the time the system started. If unknown, use 0.
///
void NewBooSetData(struct NewBooState *newboo, uint32_t _deviceStateBuffer[], int systemStartTime);

/// \brief takes all data and places it into single, comma separated string
///
///@param NewBoo is the struct with the data to be placed in the string
///
///@param dataString is where the new string wll be placed 
///
void NewBooDataToString(struct NewBooState *newboo, char dataString[NEWBOO_DATA_STRING_LENGTH]);

/// \brief retrieves the string equivalent of all parameter names
///
///@param labels is the array of labels containing the parameter names
///
void NewBooGetLabels(char labels[NEWBOO_STRUCT_DEVICE_FIELD_COUNT][NEWBOO_LABEL_MAX_CHAR_LENGTH]);

/// \brief retrieves the string equivalent of parameter names starting with state time.  Parameters 
/// prior to state time, such as id,  are not included. 
///
///@param labels is the array of labels containing the parameter names
///
int NewBooGetLabelsForLog(char labels[NEWBOO_STRUCT_DEVICE_FIELD_COUNT][NEWBOO_LABEL_MAX_CHAR_LENGTH]);

/// \brief Places data from struct into an array.
///
///@param actpack the data to be converte to an array
///
///@param actpackDataArray the array in which to place the data
///
void NewBooStructToDataArray(struct NewBooState newboo, int32_t newbooDataArray[NEWBOO_STRUCT_DEVICE_FIELD_COUNT]);

/// \brief Get data based on data position from device communication.
///
///@param actpack the data to access
///
///@param dataPosition the position of data to access
///
///@param dataValid return false if requested data position is invalid
///
int GetNewBooDataByDataPosition( struct NewBooState newboo, int dataPosition);

#ifdef __cplusplus
}//extern "C"
#endif

#endif ////ACTPACK_STRUCT_H
