class Alert:
    def __init__(self, message, severity):
        self.message = message
        self.severity = severity

    def to_dict(self):
        return {"message": self.message, "severity": self.severity}
