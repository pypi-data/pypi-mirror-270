from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, auto_mode: bool) -> None:
		"""SCPI: INPut:IQ:OSC:FULLscale:AUTO \n
		Snippet: driver.applications.k149Uwb.inputPy.iq.osc.fullscale.auto.set(auto_mode = False) \n
		No command help available \n
			:param auto_mode: No help available
		"""
		param = Conversions.bool_to_str(auto_mode)
		self._core.io.write(f'INPut:IQ:OSC:FULLscale:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: INPut:IQ:OSC:FULLscale:AUTO \n
		Snippet: value: bool = driver.applications.k149Uwb.inputPy.iq.osc.fullscale.auto.get() \n
		No command help available \n
			:return: auto_mode: No help available"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:FULLscale:AUTO?')
		return Conversions.str_to_bool(response)
