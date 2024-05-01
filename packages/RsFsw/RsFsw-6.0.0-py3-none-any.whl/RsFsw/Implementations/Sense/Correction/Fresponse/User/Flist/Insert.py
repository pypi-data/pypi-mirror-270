from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InsertCls:
	"""Insert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("insert", core, parent)

	def set(self, file_path: str, fileList=repcap.FileList.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:FLISt<fli>:INSert \n
		Snippet: driver.sense.correction.fresponse.user.flist.insert.set(file_path = 'abc', fileList = repcap.FileList.Default) \n
		Loads a frequency response (.fres) file to the current configuration. The maximum number of files per configuration is 15.
		The new file is added below the entry specified by the <fli> index. All other entries with a higher suffix are moved down
		by one position. \n
			:param file_path: string Path and file name The default directory for .fres files is C:/R_S/INSTR/USER/Fresponse.
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
		"""
		param = Conversions.value_to_quoted_str(file_path)
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:FLISt{fileList_cmd_val}:INSert {param}')

	def get(self, fileList=repcap.FileList.Default) -> str:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:FLISt<fli>:INSert \n
		Snippet: value: str = driver.sense.correction.fresponse.user.flist.insert.get(fileList = repcap.FileList.Default) \n
		Loads a frequency response (.fres) file to the current configuration. The maximum number of files per configuration is 15.
		The new file is added below the entry specified by the <fli> index. All other entries with a higher suffix are moved down
		by one position. \n
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
			:return: file_path: string Path and file name The default directory for .fres files is C:/R_S/INSTR/USER/Fresponse."""
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:FLISt{fileList_cmd_val}:INSert?')
		return trim_str_response(response)
