from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


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
		"""SCPI: INPut:DIQ:SRATe \n
		Snippet: driver.inputPy.diq.symbolRate.set(sample_rate = 1.0) \n
		Specifies or queries the sample rate of the input signal from the optional 'Digital Baseband' interface. (See 'Input
		Sample Rate') . Note: the final user sample rate of the FSW can differ and is defined using method RsFsw.Applications.
		K10x_Lte.Trace.Iq.SymbolRate.get_ (see method RsFsw.Applications.K10x_Lte.Trace.Iq.SymbolRate.get_) . \n
			:param sample_rate: Range: 1 Hz to 20 GHz, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'INPut:DIQ:SRATe {param}')

	def get(self) -> float:
		"""SCPI: INPut:DIQ:SRATe \n
		Snippet: value: float = driver.inputPy.diq.symbolRate.get() \n
		Specifies or queries the sample rate of the input signal from the optional 'Digital Baseband' interface. (See 'Input
		Sample Rate') . Note: the final user sample rate of the FSW can differ and is defined using method RsFsw.Applications.
		K10x_Lte.Trace.Iq.SymbolRate.get_ (see method RsFsw.Applications.K10x_Lte.Trace.Iq.SymbolRate.get_) . \n
			:return: sample_rate: Range: 1 Hz to 20 GHz, Unit: HZ"""
		response = self._core.io.query_str(f'INPut:DIQ:SRATe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SymbolRateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SymbolRateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
