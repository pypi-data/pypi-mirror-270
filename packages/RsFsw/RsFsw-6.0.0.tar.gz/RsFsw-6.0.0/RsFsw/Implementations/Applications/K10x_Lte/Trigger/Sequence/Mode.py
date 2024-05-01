from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: MimoAntenna, default value after init: MimoAntenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_mimoAntenna_get', 'repcap_mimoAntenna_set', repcap.MimoAntenna.Nr1)

	def repcap_mimoAntenna_set(self, mimoAntenna: repcap.MimoAntenna) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MimoAntenna.Default
		Default value after init: MimoAntenna.Nr1"""
		self._cmd_group.set_repcap_enum_value(mimoAntenna)

	def repcap_mimoAntenna_get(self) -> repcap.MimoAntenna:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, source: enums.TriggerSourceLte, mimoAntenna=repcap.MimoAntenna.Default) -> None:
		"""SCPI: TRIGger[:SEQuence]:MODE<ant> \n
		Snippet: driver.applications.k10Xlte.trigger.sequence.mode.set(source = enums.TriggerSourceLte.BBPower, mimoAntenna = repcap.MimoAntenna.Default) \n
		Turns continuous triggering on and off. \n
			:param source: CONTinuous Continuous measurement STOP Measurement stops after the trigger event is done MARK A free-run measurement is performed; the trigger event is merely indicated in the results, but does not change the behavior of the measurement. This setting is only available for FSW-B512R/-B800R.
			:param mimoAntenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mode')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSourceLte)
		mimoAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoAntenna, repcap.MimoAntenna)
		self._core.io.write(f'TRIGger:SEQuence:MODE{mimoAntenna_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, mimoAntenna=repcap.MimoAntenna.Default) -> enums.TriggerSourceLte:
		"""SCPI: TRIGger[:SEQuence]:MODE<ant> \n
		Snippet: value: enums.TriggerSourceLte = driver.applications.k10Xlte.trigger.sequence.mode.get(mimoAntenna = repcap.MimoAntenna.Default) \n
		Turns continuous triggering on and off. \n
			:param mimoAntenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mode')
			:return: source: No help available"""
		mimoAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoAntenna, repcap.MimoAntenna)
		response = self._core.io.query_str(f'TRIGger:SEQuence:MODE{mimoAntenna_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceLte)

	def clone(self) -> 'ModeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
