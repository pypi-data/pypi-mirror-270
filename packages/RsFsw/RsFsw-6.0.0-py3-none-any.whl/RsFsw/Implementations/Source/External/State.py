from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, externalGen=repcap.ExternalGen.Nr1) -> None:
		"""SCPI: SOURce:EXTernal<gen>[:STATe] \n
		Snippet: driver.source.external.state.set(state = False, externalGen = repcap.ExternalGen.Nr1) \n
		Activates or deactivates the connected external generator. Is only valid if External Generator Control (R&S FSW-B10) is
		installed and active. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param externalGen: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.bool_to_str(state)
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		self._core.io.write(f'SOURce:EXTernal{externalGen_cmd_val}:STATe {param}')

	def get(self, externalGen=repcap.ExternalGen.Nr1) -> bool:
		"""SCPI: SOURce:EXTernal<gen>[:STATe] \n
		Snippet: value: bool = driver.source.external.state.get(externalGen = repcap.ExternalGen.Nr1) \n
		Activates or deactivates the connected external generator. Is only valid if External Generator Control (R&S FSW-B10) is
		installed and active. \n
			:param externalGen: optional repeated capability selector. Default value: Nr1
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		response = self._core.io.query_str(f'SOURce:EXTernal{externalGen_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
