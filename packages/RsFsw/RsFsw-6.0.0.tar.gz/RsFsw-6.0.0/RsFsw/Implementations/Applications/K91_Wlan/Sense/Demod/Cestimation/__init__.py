from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CestimationCls:
	"""Cestimation commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cestimation", core, parent)

	@property
	def payload(self):
		"""payload commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import PayloadCls
			self._payload = PayloadCls(self._core, self._cmd_group)
		return self._payload

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import RangeCls
			self._range = RangeCls(self._core, self._cmd_group)
		return self._range

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DEMod:CESTimation \n
		Snippet: driver.applications.k91Wlan.sense.demod.cestimation.set(state = False) \n
		Note that this command is maintained for compatibility reasons only. Use [SENSe:]DEMod:CESTimation:RANGe for new remote
		control programs. Defines whether channel estimation uses preamble and payload or only preamble. Channel estimation using
		both the preamble and the payload improves the EVM measurement results. However, this functionality is not supported by
		the IEEE 802.11 standard and must be disabled if the results are to be measured strictly according to the standard. \n
			:param state: ON | OFF | 1 | 0 ON | 1 The channel estimation is performed using the preamble and the payload. The EVM results can be calculated more accurately. OFF | 0 The channel estimation is performed using the preamble only as required in the standard.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:CESTimation {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:CESTimation \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.demod.cestimation.get() \n
		Note that this command is maintained for compatibility reasons only. Use [SENSe:]DEMod:CESTimation:RANGe for new remote
		control programs. Defines whether channel estimation uses preamble and payload or only preamble. Channel estimation using
		both the preamble and the payload improves the EVM measurement results. However, this functionality is not supported by
		the IEEE 802.11 standard and must be disabled if the results are to be measured strictly according to the standard. \n
			:return: state: ON | OFF | 1 | 0 ON | 1 The channel estimation is performed using the preamble and the payload. The EVM results can be calculated more accurately. OFF | 0 The channel estimation is performed using the preamble only as required in the standard."""
		response = self._core.io.query_str(f'SENSe:DEMod:CESTimation?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'CestimationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CestimationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
