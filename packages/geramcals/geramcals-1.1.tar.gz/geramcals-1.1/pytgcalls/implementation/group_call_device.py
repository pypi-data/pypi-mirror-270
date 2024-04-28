from typing import Optional

from pytgcalls.implementation import GroupCallBase


class GroupCallDevice(GroupCallBase):
    def __init__(
        self,
        mtproto_bridge,
        audio_input_device: Optional[str] = None,
        audio_output_device: Optional[str] = None,
        enable_logs_to_console=False,
        path_to_log_file=None,
        outgoing_audio_bitrate_kbit=128,
    ):
        super().__init__(mtproto_bridge, enable_logs_to_console, path_to_log_file, outgoing_audio_bitrate_kbit)

        self.__is_playout_paused = False
        self.__is_recording_paused = False

        self.__audio_input_device = audio_input_device or ''
        self.__audio_output_device = audio_output_device or ''

    def _setup_and_start_group_call(self):
        self._start_native_group_call(self.__audio_input_device, self.__audio_output_device)

    @property
    def audio_input_device(self):
        """Get audio input device name or GUID

        Note:
            To get system recording device list you can use `get_recording_devices()` method.
        """

        return self.__audio_input_device

    @audio_input_device.setter
    def audio_input_device(self, name=None):
        self.set_audio_input_device(name)

    @property
    def audio_output_device(self):
        """Get audio output device name or GUID

        Note:
            To get system playout device list you can use `get_playout_devices()` method.
        """

        return self.__audio_output_device

    @audio_output_device.setter
    def audio_output_device(self, name=None):
        self.set_audio_output_device(name)
