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
		"""SCPI: [SENSe]:BWIDth:VIDeo:AUTO \n
		Snippet: driver.applications.k10Xlte.sense.bandwidth.video.auto.set(state = False) \n
		Couples and decouples the video bandwidth to the resolution bandwidth. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:BWIDth:VIDeo:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:BWIDth:VIDeo:AUTO \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.bandwidth.video.auto.get() \n
		Couples and decouples the video bandwidth to the resolution bandwidth. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'SENSe:BWIDth:VIDeo:AUTO?')
		return Conversions.str_to_bool(response)
