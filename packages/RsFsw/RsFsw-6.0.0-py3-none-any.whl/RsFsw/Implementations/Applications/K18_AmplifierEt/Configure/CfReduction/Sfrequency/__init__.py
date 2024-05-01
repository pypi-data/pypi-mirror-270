from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfrequencyCls:
	"""Sfrequency commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfrequency", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedStateCls
			self._ledState = LedStateCls(self._core, self._cmd_group)
		return self._ledState

	def set(self, time: float) -> None:
		"""SCPI: CONFigure:CFReduction:SFRequency \n
		Snippet: driver.applications.k18AmplifierEt.configure.cfReduction.sfrequency.set(time = 1.0) \n
		Sets and queries the stopband frequency for crest factor reduction. \n
			:param time: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:CFReduction:SFRequency {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:CFReduction:SFRequency \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.cfReduction.sfrequency.get() \n
		Sets and queries the stopband frequency for crest factor reduction. \n
			:return: time: numeric value Unit: Hz"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:SFRequency?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SfrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SfrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
