from endstone.plugin import Plugin
from endstone.event import ServerListPingEvent, event_handler

class ColorMotd(Plugin):
    api_version = "0.5"

    def __init__(self):
        super().__init__()
        self.update_period: int = 20
        self.motd: list[str] = []
        self.i: int = 0

    def on_enable(self) -> None:
        self.save_default_config()
        self.load_config()
        self.register_events(self)

    @event_handler
    def motd_update(self, event: ServerListPingEvent) -> None:
        for i in len(self.motd):
            event.motd = str(self.motd[i])
            i+1
        else:
            i=0
    
    def load_config(self) -> None:
        self.update_period = self.config["update_period"]
        self.motd = self.config["motd"]