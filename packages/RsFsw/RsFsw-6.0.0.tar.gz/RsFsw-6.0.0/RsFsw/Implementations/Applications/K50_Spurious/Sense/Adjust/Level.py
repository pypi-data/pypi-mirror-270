from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:ADJust:LEVel \n
		Snippet: driver.applications.k50Spurious.sense.adjust.level.set() \n
		Initiates a single (internal) measurement that evaluates and sets the ideal reference level for the current input data
		and measurement settings. This ensures that the settings of the RF attenuation and the reference level are optimally
		adjusted to the signal level without overloading the FSW or limiting the dynamic range by an S/N ratio that is too small. \n
		"""
		self._core.io.write(f'SENSe:ADJust:LEVel')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADJust:LEVel \n
		Snippet: driver.applications.k50Spurious.sense.adjust.level.set_with_opc() \n
		Initiates a single (internal) measurement that evaluates and sets the ideal reference level for the current input data
		and measurement settings. This ensures that the settings of the RF attenuation and the reference level are optimally
		adjusted to the signal level without overloading the FSW or limiting the dynamic range by an S/N ratio that is too small. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:LEVel', opc_timeout_ms)
