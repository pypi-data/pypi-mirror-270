from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VfirmwareCls:
	"""Vfirmware commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vfirmware", core, parent)

	def get(self) -> float:
		"""SCPI: INPut:IQ:OSC:VFIRmware \n
		Snippet: value: float = driver.applications.k149Uwb.inputPy.iq.osc.vfirmware.get() \n
		Queries whether the firmware on the connected oscilloscope is supported for Oscilloscope Baseband Input. For details see
		the specifications document. \n
			:return: firmware_state: ON | OFF | 0 | 1 OFF | 0 Firmware is not supported ON | 1 Firmware is supported"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:VFIRmware?')
		return Conversions.str_to_float(response)
