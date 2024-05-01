from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:DIQ:SRATe:AUTO \n
		Snippet: driver.applications.k10Xlte.inputPy.diq.symbolRate.auto.set(state = False) \n
		If enabled, the sample rate of the digital I/Q input signal is set automatically by the connected device.
		Is only available if the optional 'Digital Baseband' interface is installed. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:DIQ:SRATe:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: INPut:DIQ:SRATe:AUTO \n
		Snippet: value: bool = driver.applications.k10Xlte.inputPy.diq.symbolRate.auto.get() \n
		If enabled, the sample rate of the digital I/Q input signal is set automatically by the connected device.
		Is only available if the optional 'Digital Baseband' interface is installed. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'INPut:DIQ:SRATe:AUTO?')
		return Conversions.str_to_bool(response)
