from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionCls:
	"""Correction commands group definition. 50 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	@property
	def temperature(self):
		"""temperature commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_temperature'):
			from .Temperature import TemperatureCls
			self._temperature = TemperatureCls(self._core, self._cmd_group)
		return self._temperature

	@property
	def loss(self):
		"""loss commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_loss'):
			from .Loss import LossCls
			self._loss = LossCls(self._core, self._cmd_group)
		return self._loss

	@property
	def irejection(self):
		"""irejection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_irejection'):
			from .Irejection import IrejectionCls
			self._irejection = IrejectionCls(self._core, self._cmd_group)
		return self._irejection

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def enr(self):
		"""enr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_enr'):
			from .Enr import EnrCls
			self._enr = EnrCls(self._core, self._cmd_group)
		return self._enr

	@property
	def save(self):
		"""save commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_save'):
			from .Save import SaveCls
			self._save = SaveCls(self._core, self._cmd_group)
		return self._save

	def recall(self, recall_file_path: str) -> None:
		"""SCPI: [SENSe]:CORRection:RECall \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.recall(recall_file_path = 'abc') \n
		Sets the calibration results recall filepath and recalls the calibration results. \n
			:param recall_file_path: No help available
		"""
		param = Conversions.value_to_quoted_str(recall_file_path)
		self._core.io.write(f'SENSe:CORRection:RECall {param}')

	def clone(self) -> 'CorrectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CorrectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
