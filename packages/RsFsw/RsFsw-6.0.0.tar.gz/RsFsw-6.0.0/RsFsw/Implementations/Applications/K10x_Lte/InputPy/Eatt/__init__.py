from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EattCls:
	"""Eatt commands group definition. 3 total commands, 2 Subgroups, 1 group commands
	Repeated Capability: Instrument, default value after init: Instrument.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eatt", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_instrument_get', 'repcap_instrument_set', repcap.Instrument.Nr1)

	def repcap_instrument_set(self, instrument: repcap.Instrument) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Instrument.Default
		Default value after init: Instrument.Nr1"""
		self._cmd_group.set_repcap_enum_value(instrument)

	def repcap_instrument_get(self) -> repcap.Instrument:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def set(self, attenuation: float, instrument=repcap.Instrument.Default) -> None:
		"""SCPI: INPut:EATT<ant> \n
		Snippet: driver.applications.k10Xlte.inputPy.eatt.set(attenuation = 1.0, instrument = repcap.Instrument.Default) \n
		Defines the electronic attenuation level. If the current reference level is not compatible with an attenuation that has
		been set manually, the command also adjusts the reference level. Is available with the optional electronic attenuator,
		but not if you are using the optional digital baseband input. \n
			:param attenuation: Attenuation level in dB. Unit: dB
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eatt')
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		self._core.io.write(f'INPut:EATT{instrument_cmd_val} {param}')

	def get(self, instrument=repcap.Instrument.Default) -> float:
		"""SCPI: INPut:EATT<ant> \n
		Snippet: value: float = driver.applications.k10Xlte.inputPy.eatt.get(instrument = repcap.Instrument.Default) \n
		Defines the electronic attenuation level. If the current reference level is not compatible with an attenuation that has
		been set manually, the command also adjusts the reference level. Is available with the optional electronic attenuator,
		but not if you are using the optional digital baseband input. \n
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eatt')
			:return: attenuation: Attenuation level in dB. Unit: dB"""
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		response = self._core.io.query_str(f'INPut:EATT{instrument_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'EattCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EattCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
