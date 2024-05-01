from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer[:STATe][:ALL] \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.filterPy.state.all.set(state = False) \n
		Turns the weighting filters for all channels on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:STATe:ALL {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer[:STATe][:ALL] \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.power.achannel.filterPy.state.all.get() \n
		Turns the weighting filters for all channels on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:STATe:ALL?')
		return Conversions.str_to_bool(response)
