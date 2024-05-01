from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CustomCls:
	"""Custom commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("custom", core, parent)

	@property
	def number(self):
		"""number commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_number'):
			from .Number import NumberCls
			self._number = NumberCls(self._core, self._cmd_group)
		return self._number

	def set(self, modulation: str) -> None:
		"""SCPI: [SENSe]:NR5G:MODulation:SELect:CUSTom \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.modulation.select.custom.set(modulation = 'abc') \n
		No command help available \n
			:param modulation: No help available
		"""
		param = Conversions.value_to_quoted_str(modulation)
		self._core.io.write(f'SENSe:NR5G:MODulation:SELect:CUSTom {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:NR5G:MODulation:SELect:CUSTom \n
		Snippet: value: str = driver.applications.k14Xnr5G.sense.nr5G.modulation.select.custom.get() \n
		No command help available \n
			:return: modulation: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:MODulation:SELect:CUSTom?')
		return trim_str_response(response)

	def clone(self) -> 'CustomCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CustomCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
