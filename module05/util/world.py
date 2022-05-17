class Country:
    def __init__(self):
        self.code = ""
        self.name = ""
        self.continent = ""
        self.population = 0
        self.surface_area = 0

    def __str__(self):
        return f"Country [code: {self.code}, name: {self.name}, population: {self.population}, surface_area: {self.surface_area}]"


