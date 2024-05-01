from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


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
		"""SCPI: INPut:ATTenuation \n
		Snippet: driver.applications.k9X11Ad.inputPy.attenuation.set(attenuation = 1.0) \n
		Defines the total attenuation for RF input. If an electronic attenuator is available and active, the command defines a
		mechanical attenuation (see method RsFsw.Applications.K17_Mcgd.InputPy.Eatt.State.set) . If you set the attenuation
		manually, it is no longer coupled to the reference level, but the reference level is coupled to the attenuation. Thus, if
		the current reference level is not compatible with an attenuation that has been set manually, the command also adjusts
		the reference level. If an external frontend is active (see [SENSe:]EFRontend[:STATe]) , you can configure the
		attenuation of the external frontend and the analyzer separately. See also method RsFsw.InputPy.Sanalyzer.Attenuation.
		Auto.set and method RsFsw.InputPy.Sanalyzer.Attenuation.set. Is not available if the optional 'Digital Baseband'
		interface is active. \n
			:param attenuation: Range: see specifications document , Unit: DB
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'INPut:ATTenuation {param}')

	def get(self) -> float:
		"""SCPI: INPut:ATTenuation \n
		Snippet: value: float = driver.applications.k9X11Ad.inputPy.attenuation.get() \n
		Defines the total attenuation for RF input. If an electronic attenuator is available and active, the command defines a
		mechanical attenuation (see method RsFsw.Applications.K17_Mcgd.InputPy.Eatt.State.set) . If you set the attenuation
		manually, it is no longer coupled to the reference level, but the reference level is coupled to the attenuation. Thus, if
		the current reference level is not compatible with an attenuation that has been set manually, the command also adjusts
		the reference level. If an external frontend is active (see [SENSe:]EFRontend[:STATe]) , you can configure the
		attenuation of the external frontend and the analyzer separately. See also method RsFsw.InputPy.Sanalyzer.Attenuation.
		Auto.set and method RsFsw.InputPy.Sanalyzer.Attenuation.set. Is not available if the optional 'Digital Baseband'
		interface is active. \n
			:return: attenuation: Range: see specifications document , Unit: DB"""
		response = self._core.io.query_str(f'INPut:ATTenuation?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'AttenuationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AttenuationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
