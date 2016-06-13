# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class FLUPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("You have FLU!")




__plugin_name__ = "FLU"
# __plugin_version__ = "0.0.1"
# __plugin_description__ = " Filament Load and Unload Plugin"
__plugin_implementation__ = FLUPlugin()
