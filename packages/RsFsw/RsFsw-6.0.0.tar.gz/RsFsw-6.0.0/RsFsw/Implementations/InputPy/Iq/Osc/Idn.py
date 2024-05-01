from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IdnCls:
	"""Idn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("idn", core, parent)

	def get(self) -> float:
		"""SCPI: INPut:IQ:OSC:IDN \n
		Snippet: value: float = driver.inputPy.iq.osc.idn.get() \n
		Returns the identification string of the oscilloscope connected to the FSW. \n
			:return: idn: string"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:IDN?')
		return Conversions.str_to_float(response)
