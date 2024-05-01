from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VdeviceCls:
	"""Vdevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vdevice", core, parent)

	def get(self) -> float:
		"""SCPI: INPut:IQ:OSC:VDEVice \n
		Snippet: value: float = driver.inputPy.iq.osc.vdevice.get() \n
		Queries whether the connected instrument is supported for Oscilloscope Baseband Input. For details see the specifications
		document. \n
			:return: device: ON | OFF | 0 | 1 OFF | 0 Instrument is not supported. ON | 1 Instrument is supported"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:VDEVice?')
		return Conversions.str_to_float(response)
