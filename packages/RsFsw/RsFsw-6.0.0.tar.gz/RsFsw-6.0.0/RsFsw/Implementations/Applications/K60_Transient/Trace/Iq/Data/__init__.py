from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def memory(self):
		"""memory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_memory'):
			from .Memory import MemoryCls
			self._memory = MemoryCls(self._core, self._cmd_group)
		return self._memory

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPyCls
			self._formatPy = FormatPyCls(self._core, self._cmd_group)
		return self._formatPy

	def get(self) -> str:
		"""SCPI: TRACe:IQ:DATA \n
		Snippet: value: str = driver.applications.k60Transient.trace.iq.data.get() \n
		Initiates a measurement with the current settings and returns the captured data from I/Q measurements. Corresponds to:
		INIT:IMM;*WAI;method RsFsw.Trace.Iq.Data.Memory.get_ However, the method RsFsw.Trace.Iq.Data.get_ command is quicker in
		comparison. Note: Using the command with the *RST values for the TRACe:IQ:SET command, the following minimum buffer sizes
		for the response data are recommended: ASCII format 10 kBytes, binary format: 2 kBytes \n
			:return: results: Measured voltage for I and Q component for each sample that has been captured during the measurement. For analog baseband input in real baseband mode, the results for the irrelevant component are all 0. For more information see 'I/Q processing modes'. The number of samples depends on TRACe:IQ:SET. In ASCII format, the number of results is 2* the number of samples. The data format depends on method RsFsw.Applications.K18_AmplifierEt.Trace.Iq.Data.FormatPy.set. Unit: V"""
		response = self._core.io.query_str(f'TRACe:IQ:DATA?')
		return trim_str_response(response)

	def clone(self) -> 'DataCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DataCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
