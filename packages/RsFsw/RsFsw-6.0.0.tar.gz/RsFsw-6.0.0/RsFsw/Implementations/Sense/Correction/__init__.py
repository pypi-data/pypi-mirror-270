from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionCls:
	"""Correction commands group definition. 117 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	@property
	def fresponse(self):
		"""fresponse commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fresponse'):
			from .Fresponse import FresponseCls
			self._fresponse = FresponseCls(self._core, self._cmd_group)
		return self._fresponse

	@property
	def transducer(self):
		"""transducer commands group. 11 Sub-classes, 1 commands."""
		if not hasattr(self, '_transducer'):
			from .Transducer import TransducerCls
			self._transducer = TransducerCls(self._core, self._cmd_group)
		return self._transducer

	@property
	def method(self):
		"""method commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_method'):
			from .Method import MethodCls
			self._method = MethodCls(self._core, self._cmd_group)
		return self._method

	@property
	def collect(self):
		"""collect commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_collect'):
			from .Collect import CollectCls
			self._collect = CollectCls(self._core, self._cmd_group)
		return self._collect

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def cvl(self):
		"""cvl commands group. 10 Sub-classes, 1 commands."""
		if not hasattr(self, '_cvl'):
			from .Cvl import CvlCls
			self._cvl = CvlCls(self._core, self._cmd_group)
		return self._cvl

	def recall(self) -> None:
		"""SCPI: [SENSe]:CORRection:RECall \n
		Snippet: driver.sense.correction.recall() \n
		Restores the measurement configuration used for calibration. Is only available if External Generator Control (R&S
		FSW-B10) is installed and active. \n
		"""
		self._core.io.write(f'SENSe:CORRection:RECall')

	def recall_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:CORRection:RECall \n
		Snippet: driver.sense.correction.recall_with_opc() \n
		Restores the measurement configuration used for calibration. Is only available if External Generator Control (R&S
		FSW-B10) is installed and active. \n
		Same as recall, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:RECall', opc_timeout_ms)

	def clone(self) -> 'CorrectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CorrectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
