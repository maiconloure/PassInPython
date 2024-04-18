class HttpConflictError(Exception):
    def __init__(self, message: str):
        self.message = message
        self.name = "Conflict"
        self.status_code = 409
        super().__init__(self.message)