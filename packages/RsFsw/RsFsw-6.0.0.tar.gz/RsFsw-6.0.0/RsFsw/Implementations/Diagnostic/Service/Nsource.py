from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NsourceCls:
	"""Nsource commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsource", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: DIAGnostic:SERVice:NSOurce \n
		Snippet: driver.diagnostic.service.nsource.set(state = False) \n
		Turns the 28 V supply of the BNC connector labeled [noise source control] on the FSW on and off. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DIAGnostic:SERVice:NSOurce {param}')

	def get(self) -> bool:
		"""SCPI: DIAGnostic:SERVice:NSOurce \n
		Snippet: value: bool = driver.diagnostic.service.nsource.get() \n
		Turns the 28 V supply of the BNC connector labeled [noise source control] on the FSW on and off. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:NSOurce?')
		return Conversions.str_to_bool(response)
