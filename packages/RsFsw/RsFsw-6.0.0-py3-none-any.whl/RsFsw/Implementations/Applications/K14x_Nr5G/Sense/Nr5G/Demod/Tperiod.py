from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TperiodCls:
	"""Tperiod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tperiod", core, parent)

	def set(self, state: enums.TperiodState) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:TPERiod \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.tperiod.set(state = enums.TperiodState.US10) \n
		Selects the time period of the transient. \n
			:param state: US2 | US4 | US7 | US10 Transient period in us. Available transient periods depend on the selected subcarrier spacing.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.TperiodState)
		self._core.io.write(f'SENSe:NR5G:DEMod:TPERiod {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TperiodState:
		"""SCPI: [SENSe]:NR5G:DEMod:TPERiod \n
		Snippet: value: enums.TperiodState = driver.applications.k14Xnr5G.sense.nr5G.demod.tperiod.get() \n
		Selects the time period of the transient. \n
			:return: state: US2 | US4 | US7 | US10 Transient period in us. Available transient periods depend on the selected subcarrier spacing."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:TPERiod?')
		return Conversions.str_to_scalar_enum(response, enums.TperiodState)
