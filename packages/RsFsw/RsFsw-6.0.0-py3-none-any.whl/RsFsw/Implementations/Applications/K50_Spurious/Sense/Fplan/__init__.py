from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FplanCls:
	"""Fplan commands group definition. 13 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fplan", core, parent)

	@property
	def predicted(self):
		"""predicted commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_predicted'):
			from .Predicted import PredictedCls
			self._predicted = PredictedCls(self._core, self._cmd_group)
		return self._predicted

	@property
	def transfer(self):
		"""transfer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transfer'):
			from .Transfer import TransferCls
			self._transfer = TransferCls(self._core, self._cmd_group)
		return self._transfer

	@property
	def component(self):
		"""component commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_component'):
			from .Component import ComponentCls
			self._component = ComponentCls(self._core, self._cmd_group)
		return self._component

	def save(self, filename: str) -> None:
		"""SCPI: [SENSe]:FPLan:SAVE \n
		Snippet: driver.applications.k50Spurious.sense.fplan.save(filename = 'abc') \n
		Saves the current frequency plan configuration to a user-defined .csv file for later use. The result is a comma-separated
		list of values with the following syntax for each row of the frequency plan: <Num>,<Comp>,<InFreq1>,<MaxHarm1>,<InFreq2>,
		<Fact>,<MaxHarm2>,<Ident2>,<BandCtr>,<BandSpn> \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:FPLan:SAVE {param}')

	def load(self, filename: str) -> None:
		"""SCPI: [SENSe]:FPLan:LOAD \n
		Snippet: driver.applications.k50Spurious.sense.fplan.load(filename = 'abc') \n
		Loads a stored frequency plan configuration from a .csv file. \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:FPLan:LOAD {param}')

	def clone(self) -> 'FplanCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FplanCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
