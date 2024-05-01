from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AttenuationCls:
	"""Attenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	def set(self, attenuation: float) -> None:
		"""SCPI: INPut:ATTenuation \n
		Snippet: driver.applications.k30NoiseFigure.inputPy.attenuation.set(attenuation = 1.0) \n
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
		Snippet: value: float = driver.applications.k30NoiseFigure.inputPy.attenuation.get() \n
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
