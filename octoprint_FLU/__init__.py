# coding=utf-8

# FLU Plugin Template Test 

from __future__ import absolute_import

import octoprint.plugin

class FLUPlugin(octoprint.plugin.StartupPlugin,
		octoprint.plugin.TemplatePlugin,
		octoprint.plugin.SettingsPlugin,
                octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("You have FLU! (more: %s) " % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")

    def get_template_configs(self):
         return [
             dict(type="navbar", custom_bindings=False),
             dict(type="settings", custom_bindings=False)

         ]

    def get_assets(self):
         return dict(
         js=["js/FLU.js"],
         css=["css/FLU.css"]
     )   

    
__plugin_name__ = "FLU"
# __plugin_version__ = "0.0.1"
# __plugin_description__ = " Filament Load and Unload Plugin"
__plugin_implementation__ = FLUPlugin()

