from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import CurrentCls
			self._current = CurrentCls(self._core, self._cmd_group)
		return self._current

	def set(self, count: float) -> None:
		"""SCPI: [SENSe]:SWEep:STATistics:COUNt \n
		Snippet: driver.applications.k18AmplifierEt.sense.sweep.statistics.count.set(count = 1.0) \n
		Sets and queries the sweep statistics count. \n
			:param count: numeric value
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:SWEep:STATistics:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:STATistics:COUNt \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.sweep.statistics.count.get() \n
		Sets and queries the sweep statistics count. \n
			:return: count: numeric value"""
		response = self._core.io.query_str(f'SENSe:SWEep:STATistics:COUNt?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'CountCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CountCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
