from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SspacingCls:
	"""Sspacing commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sspacing", core, parent)

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_value'):
			from .Value import ValueCls
			self._value = ValueCls(self._core, self._cmd_group)
		return self._value

	def set(self, subcarrier_spacing: enums.SubcarrierSpacingK91) -> None:
		"""SCPI: CONFigure:WLAN:SSPacing \n
		Snippet: driver.applications.k91Wlan.configure.wlan.sspacing.set(subcarrier_spacing = enums.SubcarrierSpacingK91.NSTandard) \n
		No command help available \n
			:param subcarrier_spacing: No help available
		"""
		param = Conversions.enum_scalar_to_str(subcarrier_spacing, enums.SubcarrierSpacingK91)
		self._core.io.write(f'CONFigure:WLAN:SSPacing {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SubcarrierSpacingK91:
		"""SCPI: CONFigure:WLAN:SSPacing \n
		Snippet: value: enums.SubcarrierSpacingK91 = driver.applications.k91Wlan.configure.wlan.sspacing.get() \n
		No command help available \n
			:return: subcarrier_spacing: No help available"""
		response = self._core.io.query_str(f'CONFigure:WLAN:SSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.SubcarrierSpacingK91)

	def clone(self) -> 'SspacingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SspacingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
