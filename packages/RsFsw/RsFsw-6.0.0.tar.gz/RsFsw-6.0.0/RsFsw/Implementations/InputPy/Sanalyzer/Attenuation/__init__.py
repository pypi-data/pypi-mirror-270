from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AttenuationCls:
	"""Attenuation commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	def set(self, attenuation: float) -> None:
		"""SCPI: INPut:SANalyzer:ATTenuation \n
		Snippet: driver.inputPy.sanalyzer.attenuation.set(attenuation = 1.0) \n
		Configures attenuation at the analyzer input for an active external frontend manually. \n
			:param attenuation: Range: see specifications document , Unit: DB
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'INPut:SANalyzer:ATTenuation {param}')

	def get(self) -> float:
		"""SCPI: INPut:SANalyzer:ATTenuation \n
		Snippet: value: float = driver.inputPy.sanalyzer.attenuation.get() \n
		Configures attenuation at the analyzer input for an active external frontend manually. \n
			:return: attenuation: Range: see specifications document , Unit: DB"""
		response = self._core.io.query_str(f'INPut:SANalyzer:ATTenuation?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'AttenuationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AttenuationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
