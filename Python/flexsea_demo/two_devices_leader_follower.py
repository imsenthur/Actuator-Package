#!/usr/bin/env python3

"""
FlexSEA Two Devices Leader Follower demo
"""

import traceback
from time import sleep
from flexsea import fxUtils as fxu  # pylint: disable=no-name-in-module
from flexsea import fxEnums as fxe  # pylint: disable=no-name-in-module
from flexsea import flexsea as flex


def leader_follower(
	fxs, ports, baud_rate, timeout=10
):  # pylint: disable=too-many-locals
	"""
	lead the motion of an ActPack by manually moving another one
	"""

	leader_id = fxs.open(ports[0], baud_rate, 6)  # Leader
	follower_id = fxs.open(ports[1], baud_rate, 6)  # Follower

	fxs.start_streaming(leader_id, 200, False)
	fxs.start_streaming(follower_id, 200, False)

	sleep(0.2)

	act_pack_state_0 = fxs.read_device(leader_id)
	act_pack_state_1 = fxs.read_device(follower_id)

	initial_angle_0 = act_pack_state_0.mot_ang
	initial_angle_1 = act_pack_state_1.mot_ang

	# Set first device to current controller with 0 current (0 torque)
	fxs.set_gains(leader_id, 40, 400, 0, 0, 0, 128)
	fxs.send_motor_command(leader_id, fxe.FX_CURRENT, 0)

	# Set position controller for second device
	fxs.set_gains(follower_id, 100, 1, 0, 0, 0, 0)
	fxs.send_motor_command(follower_id, fxe.FX_POSITION, initial_angle_1)

	loop_delay = 0.05  # second
	loop_count = int(timeout / loop_delay)

	try:
		for i in range(loop_count):
			sleep(loop_delay)
			fxu.clear_terminal()
			leader_data = fxs.read_device(leader_id)
			follower_data = fxs.read_device(follower_id)
			angle0 = leader_data.mot_ang
			diff = angle0 - initial_angle_0
			fxs.send_motor_command(follower_id, fxe.FX_POSITION, initial_angle_1 + diff)
			print(f"Device {follower_id} following device {leader_id}\n")
			fxu.print_device(follower_data, fxe.FX_ACT_PACK)
			print("")  # Empty line
			fxu.print_device(leader_data, fxe.FX_ACT_PACK)
			fxu.print_loop_count(i, loop_count)

	except Exception as err:  # pylint: disable=broad-except
		print(f"Problem encountered: {err}")
		print(traceback.format_exc())

	print("Turning off position control...")
	fxs.set_gains(leader_id, 0, 0, 0, 0, 0, 0)
	fxs.set_gains(follower_id, 0, 0, 0, 0, 0, 0)
	fxs.send_motor_command(follower_id, fxe.FX_NONE, 0)
	fxs.send_motor_command(leader_id, fxe.FX_NONE, 0)
	sleep(0.5)
	fxs.close(leader_id)
	fxs.close(follower_id)


def main():
	"""
	Standalone two-device position control execution
	"""
	# pylint: disable=import-outside-toplevel
	import argparse

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		"ports", metavar="Ports", type=str, nargs="+", help="Your devices' serial ports."
	)
	parser.add_argument(
		"-b",
		"--baud",
		metavar="B",
		dest="baud_rate",
		type=int,
		default=230400,
		help="Serial communication baud rate.",
	)
	parser.add_argument(
		"-t",
		"--timeout",
		metavar="T",
		dest="timeout",
		type=int,
		default=10,
		help="How many seconds to run for",
	)
	args = parser.parse_args()
	leader_follower(flex.FlexSEA(), args.ports, args.baud_rate, args.timeout)


if __name__ == "__main__":
	main()
