from endstone.plugin import Plugin
from endstone.event import ServerListPingEvent

class ColorMotd(Plugin):
    api_version = "0.5"

    def __init__(self):
        super().__init__()
        self.update_period: int = 20
        self.first_motd: str = ""
        self.second_motd: str = ""
        self.third_motd: str = ""

    def on_enable(self) -> None:
        self.save_default_config()
        self.load_config()
        self.server.scheduler.run_task(self, self.change_motd, delay=0, period=self.update_period)
    
    def change_motd(self, event: ServerListPingEvent) -> None:
        event.motd = self.first_motd
        self.server.scheduler.run_task(self, self.change_motd, delay=self.update_period)
        event.motd = self.second_motd
        self.server.scheduler.run_task(self, self.change_motd, delay=self.update_period)
        event.motd = self.third_motd
    
    def load_config(self) -> None:
        self.update_period = self.config["update_period"]
        self.first_motd = self.config["first_motd"]
        self.second_motd = self.config["second_motd"]
        self.third_motd = self.config["third_motd"]

