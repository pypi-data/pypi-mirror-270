from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:ATTenuation:AUTO \n
		Snippet: driver.applications.k9X11Ad.inputPy.attenuation.auto.set(state = False) \n
		Couples or decouples the attenuation to the reference level. Thus, when the reference level is changed, the FSW
		determines the signal level for optimal internal data processing and sets the required attenuation accordingly.
		If an external frontend is active (see [SENSe:]EFRontend[:STATe]) , you can configure the attenuation of the external
		frontend and the analyzer separately. See also method RsFsw.InputPy.Sanalyzer.Attenuation.Auto.set and method RsFsw.
		InputPy.Sanalyzer.Attenuation.set. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:ATTenuation:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: INPut:ATTenuation:AUTO \n
		Snippet: value: bool = driver.applications.k9X11Ad.inputPy.attenuation.auto.get() \n
		Couples or decouples the attenuation to the reference level. Thus, when the reference level is changed, the FSW
		determines the signal level for optimal internal data processing and sets the required attenuation accordingly.
		If an external frontend is active (see [SENSe:]EFRontend[:STATe]) , you can configure the attenuation of the external
		frontend and the analyzer separately. See also method RsFsw.InputPy.Sanalyzer.Attenuation.Auto.set and method RsFsw.
		InputPy.Sanalyzer.Attenuation.set. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'INPut:ATTenuation:AUTO?')
		return Conversions.str_to_bool(response)
