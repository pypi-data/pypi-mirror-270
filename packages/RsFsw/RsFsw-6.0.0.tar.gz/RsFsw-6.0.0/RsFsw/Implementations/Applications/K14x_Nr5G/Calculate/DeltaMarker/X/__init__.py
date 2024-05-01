from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XCls:
	"""X commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import RelativeCls
			self._relative = RelativeCls(self._core, self._cmd_group)
		return self._relative

	def set(self, position: float, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:X \n
		Snippet: driver.applications.k14Xnr5G.calculate.deltaMarker.x.set(position = 1.0, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Moves a delta marker to a particular coordinate on the x-axis. If necessary, the command activates the delta marker and
		positions a reference marker to the peak power. \n
			:param position: Numeric value that defines the marker position on the x-axis. The position is relative to the reference marker. To select an absolute position you have to change the delta marker mode with method RsFsw.Calculate.DeltaMarker.Mode.set. A query returns the absolute position of the delta marker. Range: The value range and unit depend on the measurement and scale of the x-axis. , Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.decimal_value_to_str(position)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:X {param}')

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> float:
		"""SCPI: CALCulate<n>:DELTamarker<m>:X \n
		Snippet: value: float = driver.applications.k14Xnr5G.calculate.deltaMarker.x.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Moves a delta marker to a particular coordinate on the x-axis. If necessary, the command activates the delta marker and
		positions a reference marker to the peak power. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: position: Numeric value that defines the marker position on the x-axis. The position is relative to the reference marker. To select an absolute position you have to change the delta marker mode with method RsFsw.Calculate.DeltaMarker.Mode.set. A query returns the absolute position of the delta marker. Range: The value range and unit depend on the measurement and scale of the x-axis. , Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:X?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'XCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = XCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
