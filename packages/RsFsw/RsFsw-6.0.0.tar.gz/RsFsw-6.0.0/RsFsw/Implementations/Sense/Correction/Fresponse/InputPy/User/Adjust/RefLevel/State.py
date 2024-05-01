from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:ADJust:RLEVel:STATe \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.adjust.refLevel.state.set(state = False, inputIx = repcap.InputIx.Default) \n
		Activates or deactivates the automatic adjustment of the reference level to the active filter calculation configuration.
		The offset is the mean of the filter calculation. For details and restrictions see 'Adjust Ref Level'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:ADJust:RLEVel:STATe {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:ADJust:RLEVel:STATe \n
		Snippet: value: bool = driver.sense.correction.fresponse.inputPy.user.adjust.refLevel.state.get(inputIx = repcap.InputIx.Default) \n
		Activates or deactivates the automatic adjustment of the reference level to the active filter calculation configuration.
		The offset is the mean of the filter calculation. For details and restrictions see 'Adjust Ref Level'. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:ADJust:RLEVel:STATe?')
		return Conversions.str_to_bool(response)
