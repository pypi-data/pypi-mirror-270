from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.LisnType) -> None:
		"""SCPI: INPut:LISN[:TYPE] \n
		Snippet: driver.inputPy.lisn.typePy.set(type_py = enums.LisnType.ENV216) \n
		Turns automatic control of a LISN on and off. It also selects the type of network. \n
			:param type_py: ENV216 R&S ENV 216 / AMN6500: two phases and highpass are controllable. ENV432 R&S ENV 432: four phases are controllable. ENV4200 R&S ENV 4200: four phases are controllable. ESH2Z5 R&S ESH2-Z5: four phases (incl. protective earth) are controllable. ESH3Z5 R&S ESH3-Z5: two phases (incl. protective earth) are controllable. FOURphase R&S ESH2-Z5: four phases (incl. protective earth) are controllable. OFF Turns off remote control of the LISN. TWOPhase R&S ESH3-Z5: two phases (incl. protective earth) are controllable.
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.LisnType)
		self._core.io.write(f'INPut:LISN:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.LisnType:
		"""SCPI: INPut:LISN[:TYPE] \n
		Snippet: value: enums.LisnType = driver.inputPy.lisn.typePy.get() \n
		Turns automatic control of a LISN on and off. It also selects the type of network. \n
			:return: type_py: ENV216 R&S ENV 216 / AMN6500: two phases and highpass are controllable. ENV432 R&S ENV 432: four phases are controllable. ENV4200 R&S ENV 4200: four phases are controllable. ESH2Z5 R&S ESH2-Z5: four phases (incl. protective earth) are controllable. ESH3Z5 R&S ESH3-Z5: two phases (incl. protective earth) are controllable. FOURphase R&S ESH2-Z5: four phases (incl. protective earth) are controllable. OFF Turns off remote control of the LISN. TWOPhase R&S ESH3-Z5: two phases (incl. protective earth) are controllable."""
		response = self._core.io.query_str(f'INPut:LISN:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.LisnType)
