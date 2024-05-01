from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XcorrelationCls:
	"""Xcorrelation commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xcorrelation", core, parent)

	@property
	def margin(self):
		"""margin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_margin'):
			from .Margin import MarginCls
			self._margin = MarginCls(self._core, self._cmd_group)
		return self._margin

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:EVM:XCORrelation \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.evm.xcorrelation.get() \n
		No command help available \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:BURSt:EVM:XCORrelation?')
		return trim_str_response(response)

	def clone(self) -> 'XcorrelationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = XcorrelationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
