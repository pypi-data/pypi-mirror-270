from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScaptureCls:
	"""Scapture commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scapture", core, parent)

	def set(self, state: enums.SweepMode) -> None:
		"""SCPI: [SENSe]:NR5G:FRAMe:SCAPture \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.frame.scapture.set(state = enums.SweepMode.AUTO) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.enum_scalar_to_str(state, enums.SweepMode)
		self._core.io.write(f'SENSe:NR5G:FRAMe:SCAPture {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepMode:
		"""SCPI: [SENSe]:NR5G:FRAMe:SCAPture \n
		Snippet: value: enums.SweepMode = driver.applications.k14Xnr5G.sense.nr5G.frame.scapture.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:FRAMe:SCAPture?')
		return Conversions.str_to_scalar_enum(response, enums.SweepMode)
