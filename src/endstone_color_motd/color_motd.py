from endstone.plugin import Plugin
from endstone.event import ServerListPingEvent, event_handler

class ColorMotd(Plugin):
    api_version = "0.5"

    def __init__(self):
        super().__init__()
        self.motd: str = ""

    def on_enable(self) -> None:
        self.save_default_config()
        self.load_config()
        self.register_events(self)

    @event_handler
    def motd_update(self, event: ServerListPingEvent) -> None:
        event.motd = f"{str(self.motd)}"
    
    def load_config(self) -> None:
        self.motd = self.config["motd"]