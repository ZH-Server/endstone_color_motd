from endstone.plugin import Plugin
from endstone import ColorFormat
from endstone.event import ServerListPingEvent
import time

class ColorMotd(Plugin):
    api_version = "0.5"

    def on_enable(self) -> None:
        self.server.scheduler.run_task(self, self.change_motd, delay=0, period=100)
    
    def change_motd(self) -> None:
        ServerListPingEvent.motd.setter("Welcome to " + ColorFormat.BOLD + ColorFormat.MATERIAL_DIAMOND + "ZH-Server" + ColorFormat.RESET + " !")
        time.sleep(5)
        ServerListPingEvent.motd.setter("Powered by " + ColorFormat.BOLD + ColorFormat.YELLOW + "Endstone" + ColorFormat.RESET)
        time.sleep(5)
        ServerListPingEvent.motd.setter("Have fun!")
