from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, instrument=repcap.Instrument.Default) -> None:
		"""SCPI: INPut:EATT<ant>:STATe \n
		Snippet: driver.applications.k10Xlte.inputPy.eatt.state.set(state = False, instrument = repcap.Instrument.Default) \n
		Turns the electronic attenuator on and off. Is available with the optional electronic attenuator, but not if you are
		using the optional digital baseband input. \n
			:param state: ON | OFF
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eatt')
		"""
		param = Conversions.bool_to_str(state)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		self._core.io.write(f'INPut:EATT{instrument_cmd_val}:STATe {param}')

	def get(self, instrument=repcap.Instrument.Default) -> bool:
		"""SCPI: INPut:EATT<ant>:STATe \n
		Snippet: value: bool = driver.applications.k10Xlte.inputPy.eatt.state.get(instrument = repcap.Instrument.Default) \n
		Turns the electronic attenuator on and off. Is available with the optional electronic attenuator, but not if you are
		using the optional digital baseband input. \n
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eatt')
			:return: state: ON | OFF"""
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		response = self._core.io.query_str(f'INPut:EATT{instrument_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
