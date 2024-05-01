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
		"""SCPI: [SENSe]:SWEep:TIME:AUTO \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.time.auto.set(state = False) \n
		Couples and decouples the sweep time to the span and the resolution and video bandwidths. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:TIME:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:TIME:AUTO \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.sweep.time.auto.get() \n
		Couples and decouples the sweep time to the span and the resolution and video bandwidths. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'SENSe:SWEep:TIME:AUTO?')
		return Conversions.str_to_bool(response)
