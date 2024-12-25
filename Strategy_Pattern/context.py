class Context():
    def __init__(self, strategy):
        self._strategy = strategy
    
    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, value):
        self._strategy = value

    def execute_strategy(self):
        """ Executes the strategy chosen by the client """
        self._strategy.execute()