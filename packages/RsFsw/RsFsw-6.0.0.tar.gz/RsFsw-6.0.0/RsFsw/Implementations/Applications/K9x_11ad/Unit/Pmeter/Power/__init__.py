from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def ratio(self):
		"""ratio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ratio'):
			from .Ratio import RatioCls
			self._ratio = RatioCls(self._core, self._cmd_group)
		return self._ratio

	def set(self, arg_0: enums.PowerMeterUnit, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: UNIT:PMETer<p>:POWer \n
		Snippet: driver.applications.k9X11Ad.unit.pmeter.power.set(arg_0 = enums.PowerMeterUnit.DBM, powerMeter = repcap.PowerMeter.Default) \n
		Selects the unit for absolute power sensor measurements. \n
			:param arg_0: No help available
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.PowerMeterUnit)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'UNIT:PMETer{powerMeter_cmd_val}:POWer {param}')

	# noinspection PyTypeChecker
	def get(self, powerMeter=repcap.PowerMeter.Default) -> enums.PowerMeterUnit:
		"""SCPI: UNIT:PMETer<p>:POWer \n
		Snippet: value: enums.PowerMeterUnit = driver.applications.k9X11Ad.unit.pmeter.power.get(powerMeter = repcap.PowerMeter.Default) \n
		Selects the unit for absolute power sensor measurements. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: arg_0: No help available"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'UNIT:PMETer{powerMeter_cmd_val}:POWer?')
		return Conversions.str_to_scalar_enum(response, enums.PowerMeterUnit)

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
