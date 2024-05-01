from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DummyCls:
	"""Dummy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dummy", core, parent)

	def set(self, type_py: enums.TypePowerK6) -> None:
		"""SCPI: AUTO:POWer:DUMMy \n
		Snippet: driver.applications.k6Pulse.auto.power.dummy.set(type_py = enums.TypePowerK6.POWer) \n
		No command help available \n
			:param type_py: No help available
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TypePowerK6)
		self._core.io.write(f'AUTO:POWer:DUMMy {param}')
