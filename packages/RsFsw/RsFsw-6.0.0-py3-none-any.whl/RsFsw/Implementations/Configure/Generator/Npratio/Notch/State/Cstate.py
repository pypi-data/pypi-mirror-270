from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CstateCls:
	"""Cstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cstate", core, parent)

	# noinspection PyTypeChecker
	def get(self, notch=repcap.Notch.Default) -> enums.ControlState:
		"""SCPI: CONFigure:GENerator:NPRatio:NOTCh<notch>:STATe:CSTate \n
		Snippet: value: enums.ControlState = driver.configure.generator.npratio.notch.state.cstate.get(notch = repcap.Notch.Default) \n
		Queries the state of the generator notch setting for the specified notch. \n
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: control_state: OFF | SUCCessful | ERRor OFF Signal generator control off SUCCessful Setting successfully applied on the signal generator ERRor Control error, for example because a specified value cannot be applied on the signal generator"""
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:NOTCh{notch_cmd_val}:STATe:CSTate?')
		return Conversions.str_to_scalar_enum(response, enums.ControlState)
