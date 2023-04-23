from model.population import Population

class SelectionMethod:
    def select(self, population: Population) -> None:
        raise NotImplementedError()
    
    def initialize(self) -> None:
        raise NotImplementedError()