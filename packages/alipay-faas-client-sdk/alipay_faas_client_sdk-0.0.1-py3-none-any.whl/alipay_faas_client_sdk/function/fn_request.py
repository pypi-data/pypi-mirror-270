class CallFunctionConfig:
    def __init__(self, env: str = ""):
        self.env = env


class CallFunctionParam:
    def __init__(self, name: str, data: dict, config: CallFunctionConfig = None):
        self.name = name
        self.data = data
        self.config = config if config is not None else CallFunctionConfig()
