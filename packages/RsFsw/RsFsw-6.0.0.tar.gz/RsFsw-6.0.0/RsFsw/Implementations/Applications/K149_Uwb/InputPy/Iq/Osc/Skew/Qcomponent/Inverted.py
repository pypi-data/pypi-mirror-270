from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InvertedCls:
	"""Inverted commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inverted", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: INPut:IQ:OSC:SKEW:Q:INVerted \n
		Snippet: driver.applications.k149Uwb.inputPy.iq.osc.skew.qcomponent.inverted.set(value = 1.0) \n
		Compensates for skewed values in the negative Q path, e.g. due to different input cables. \n
			:param value: Unit: S
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'INPut:IQ:OSC:SKEW:Q:INVerted {param}')

	def get(self) -> float:
		"""SCPI: INPut:IQ:OSC:SKEW:Q:INVerted \n
		Snippet: value: float = driver.applications.k149Uwb.inputPy.iq.osc.skew.qcomponent.inverted.get() \n
		Compensates for skewed values in the negative Q path, e.g. due to different input cables. \n
			:return: value: Unit: S"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:SKEW:Q:INVerted?')
		return Conversions.str_to_float(response)
