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
		"""SCPI: [SENSe]:BWIDth[:RESolution]:AUTO \n
		Snippet: driver.applications.k14Xnr5G.sense.bandwidth.resolution.auto.set(state = False) \n
		If enabled, the resolution bandwidth is selected automatically, depending on the current frequency of the sweep point, as
		defined in the frequency table (see 'Using a frequency table') .
		If disabled, the RBW defined by [SENSe:]BANDwidth[:RESolution] is used. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:BWIDth:RESolution:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:AUTO \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.bandwidth.resolution.auto.get() \n
		If enabled, the resolution bandwidth is selected automatically, depending on the current frequency of the sweep point, as
		defined in the frequency table (see 'Using a frequency table') .
		If disabled, the RBW defined by [SENSe:]BANDwidth[:RESolution] is used. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:BWIDth:RESolution:AUTO?')
		return Conversions.str_to_bool(response)
