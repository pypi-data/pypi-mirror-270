from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpathCls:
	"""Dpath commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpath", core, parent)

	def set(self, auto_off: enums.State) -> None:
		"""SCPI: INPut:DPATh \n
		Snippet: driver.applications.k70Vsa.inputPy.dpath.set(auto_off = enums.State.ALL) \n
		Enables or disables the use of the direct path for frequencies close to 0 Hz. If an external frontend is active, the
		direct path is always used. \n
			:param auto_off: AUTO | OFF AUTO | 1 (Default) the direct path is used automatically for frequencies close to 0 Hz. OFF | 0 The analog mixer path is always used.
		"""
		param = Conversions.enum_scalar_to_str(auto_off, enums.State)
		self._core.io.write(f'INPut:DPATh {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.State:
		"""SCPI: INPut:DPATh \n
		Snippet: value: enums.State = driver.applications.k70Vsa.inputPy.dpath.get() \n
		Enables or disables the use of the direct path for frequencies close to 0 Hz. If an external frontend is active, the
		direct path is always used. \n
			:return: auto_off: No help available"""
		response = self._core.io.query_str(f'INPut:DPATh?')
		return Conversions.str_to_scalar_enum(response, enums.State)
