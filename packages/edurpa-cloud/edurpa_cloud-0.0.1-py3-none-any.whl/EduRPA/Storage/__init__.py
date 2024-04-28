name = 'edurpa_storage'
from .Storage import Storage
from robotlibcore import DynamicCore

class Storage(DynamicCore):
    def __init__(
        self
    ):
        # Register keyword libraries to LibCore
        libraries = [
            Storage()
        ]
        super().__init__(libraries)