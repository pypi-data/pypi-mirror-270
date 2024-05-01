from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LinkCls:
	"""Link commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("link", core, parent)

	def set(self, mode: enums.GeneratorLink) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:GENerator:LINK \n
		Snippet: driver.applications.k30NoiseFigure.system.communicate.rdevice.generator.link.set(mode = enums.GeneratorLink.GPIB) \n
		Selects the link type of the external generator if the GPIB interface is used. The difference between the two GPIB
		operating modes is the execution speed. During GPIB operation, each frequency to be set is transmitted to the generator
		separately. If the TTL interface is also used, a whole frequency list can be programmed in one go. Frequencies can then
		be switched per TTL handshake, which speeds up the process considerably. \n
			:param mode: GPIB | TTL GPIB GPIB connection without TTL synchronization (for all generators of other manufacturers and some Rohde & Schwarz devices) TTL GPIB connection with TTL synchronization (if available; for most Rohde&Schwarz devices)
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.GeneratorLink)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:GENerator:LINK {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GeneratorLink:
		"""SCPI: SYSTem:COMMunicate:RDEVice:GENerator:LINK \n
		Snippet: value: enums.GeneratorLink = driver.applications.k30NoiseFigure.system.communicate.rdevice.generator.link.get() \n
		Selects the link type of the external generator if the GPIB interface is used. The difference between the two GPIB
		operating modes is the execution speed. During GPIB operation, each frequency to be set is transmitted to the generator
		separately. If the TTL interface is also used, a whole frequency list can be programmed in one go. Frequencies can then
		be switched per TTL handshake, which speeds up the process considerably. \n
			:return: mode: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:GENerator:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.GeneratorLink)
