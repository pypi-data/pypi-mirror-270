from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	def set(self, limit: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:BURSt:TRISe[:AVERage] \n
		Snippet: driver.applications.k91Wlan.calculate.limit.burst.trise.average.set(limit = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Sets or queries the average or maximum rise time limit for the data carrier determined by the default WLAN measurement.
		For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:param limit: Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(limit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:BURSt:TRISe:AVERage {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:BURSt:TRISe[:AVERage] \n
		Snippet: value: float = driver.applications.k91Wlan.calculate.limit.burst.trise.average.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Sets or queries the average or maximum rise time limit for the data carrier determined by the default WLAN measurement.
		For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limit: Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:BURSt:TRISe:AVERage?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'AverageCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AverageCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
