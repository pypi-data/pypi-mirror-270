from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EattenuationCls:
	"""Eattenuation commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eattenuation", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	def set(self, arg_0: float) -> None:
		"""SCPI: INPut:EATTenuation \n
		Snippet: driver.applications.k40PhaseNoise.inputPy.eattenuation.set(arg_0 = 1.0) \n
		Defines the electronic attenuation level. If the current reference level is not compatible with an attenuation that has
		been set manually, the command also adjusts the reference level. Is available with the optional electronic attenuator,
		but not if you are using the optional digital baseband input. \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'INPut:EATTenuation {param}')

	def get(self) -> float:
		"""SCPI: INPut:EATTenuation \n
		Snippet: value: float = driver.applications.k40PhaseNoise.inputPy.eattenuation.get() \n
		Defines the electronic attenuation level. If the current reference level is not compatible with an attenuation that has
		been set manually, the command also adjusts the reference level. Is available with the optional electronic attenuator,
		but not if you are using the optional digital baseband input. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'INPut:EATTenuation?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'EattenuationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EattenuationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
