from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MagnitudeCls:
	"""Magnitude commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("magnitude", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	def set(self, ref_value: float, window=repcap.Window.Default, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: CALCulate<n>:PMETer<p>:RELative[:MAGNitude] \n
		Snippet: driver.applications.k14Xnr5G.calculate.pmeter.relative.magnitude.set(ref_value = 1.0, window = repcap.Window.Default, powerMeter = repcap.PowerMeter.Default) \n
		Defines the reference value for relative measurements. \n
			:param ref_value: Range: -200 dBm to 200 dBm, Unit: DBM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.decimal_value_to_str(ref_value)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'CALCulate{window_cmd_val}:PMETer{powerMeter_cmd_val}:RELative:MAGNitude {param}')

	def get(self, window=repcap.Window.Default, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: CALCulate<n>:PMETer<p>:RELative[:MAGNitude] \n
		Snippet: value: float = driver.applications.k14Xnr5G.calculate.pmeter.relative.magnitude.get(window = repcap.Window.Default, powerMeter = repcap.PowerMeter.Default) \n
		Defines the reference value for relative measurements. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: ref_value: Range: -200 dBm to 200 dBm, Unit: DBM"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PMETer{powerMeter_cmd_val}:RELative:MAGNitude?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'MagnitudeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MagnitudeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
