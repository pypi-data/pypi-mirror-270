from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRateCls:
	"""SymbolRate commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	def set(self, sample_rate: float) -> None:
		"""SCPI: TRACe:IQ:SRATe \n
		Snippet: driver.applications.k18AmplifierEt.trace.iq.symbolRate.set(sample_rate = 1.0) \n
		Sets the final user sample rate for the acquired I/Q data. Thus, the user sample rate can be modified without affecting
		the actual data capturing settings on the FSW. Note: The smaller the user sample rate, the smaller the usable I/Q
		bandwidth, see 'Sample rate and maximum usable I/Q bandwidth for RF input'. In order to ensure a minimum usable I/Q
		bandwidth use the method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.Mbwidth.set command. \n
			:param sample_rate: The valid sample rates are described in 'Sample rate and maximum usable I/Q bandwidth for RF input'. Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'TRACe:IQ:SRATe {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:SRATe \n
		Snippet: value: float = driver.applications.k18AmplifierEt.trace.iq.symbolRate.get() \n
		Sets the final user sample rate for the acquired I/Q data. Thus, the user sample rate can be modified without affecting
		the actual data capturing settings on the FSW. Note: The smaller the user sample rate, the smaller the usable I/Q
		bandwidth, see 'Sample rate and maximum usable I/Q bandwidth for RF input'. In order to ensure a minimum usable I/Q
		bandwidth use the method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.Mbwidth.set command. \n
			:return: sample_rate: The valid sample rates are described in 'Sample rate and maximum usable I/Q bandwidth for RF input'. Unit: HZ"""
		response = self._core.io.query_str(f'TRACe:IQ:SRATe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SymbolRateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SymbolRateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
