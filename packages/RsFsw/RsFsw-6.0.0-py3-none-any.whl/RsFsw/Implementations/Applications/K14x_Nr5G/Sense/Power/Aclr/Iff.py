from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IffCls:
	"""Iff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iff", core, parent)

	def set(self, size: enums.DutSize) -> None:
		"""SCPI: [SENSe]:POWer:ACLR:IFF \n
		Snippet: driver.applications.k14Xnr5G.sense.power.aclr.iff.set(size = enums.DutSize.DUT15) \n
		No command help available \n
			:param size: No help available
		"""
		param = Conversions.enum_scalar_to_str(size, enums.DutSize)
		self._core.io.write(f'SENSe:POWer:ACLR:IFF {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DutSize:
		"""SCPI: [SENSe]:POWer:ACLR:IFF \n
		Snippet: value: enums.DutSize = driver.applications.k14Xnr5G.sense.power.aclr.iff.get() \n
		No command help available \n
			:return: size: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACLR:IFF?')
		return Conversions.str_to_scalar_enum(response, enums.DutSize)
