from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Antenna, default value after init: Antenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antenna_get', 'repcap_antenna_set', repcap.Antenna.Nr1)

	def repcap_antenna_set(self, antenna: repcap.Antenna) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Antenna.Default
		Default value after init: Antenna.Nr1"""
		self._cmd_group.set_repcap_enum_value(antenna)

	def repcap_antenna_get(self) -> repcap.Antenna:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, state: bool, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: INPut:EGAin<ant>:STATe \n
		Snippet: driver.applications.k14Xnr5G.inputPy.egain.state.set(state = False, antenna = repcap.Antenna.Default) \n
		Before this command can be used, the external preamplifier must be connected to the FSW. See the preamplifier's
		documentation for details. When activated, the FSW automatically compensates the magnitude and phase characteristics of
		the external preamplifier in the measurement results. Note that when an optional external preamplifier is activated, the
		internal preamplifier is automatically disabled, and vice versa. For FSW85 models with two RF inputs, you must enable
		correction from the external preamplifier for each input individually. Correction cannot be enabled for both inputs at
		the same time. When deactivated, no compensation is performed even if an external preamplifier remains connected. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 No data correction is performed based on the external preamplifier ON | 1 Performs data corrections based on the external preamplifier
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'State')
		"""
		param = Conversions.bool_to_str(state)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'INPut:EGAin{antenna_cmd_val}:STATe {param}')

	def get(self, antenna=repcap.Antenna.Default) -> bool:
		"""SCPI: INPut:EGAin<ant>:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.inputPy.egain.state.get(antenna = repcap.Antenna.Default) \n
		Before this command can be used, the external preamplifier must be connected to the FSW. See the preamplifier's
		documentation for details. When activated, the FSW automatically compensates the magnitude and phase characteristics of
		the external preamplifier in the measurement results. Note that when an optional external preamplifier is activated, the
		internal preamplifier is automatically disabled, and vice versa. For FSW85 models with two RF inputs, you must enable
		correction from the external preamplifier for each input individually. Correction cannot be enabled for both inputs at
		the same time. When deactivated, no compensation is performed even if an external preamplifier remains connected. \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'State')
			:return: state: ON | OFF | 0 | 1 OFF | 0 No data correction is performed based on the external preamplifier ON | 1 Performs data corrections based on the external preamplifier"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'INPut:EGAin{antenna_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'StateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
