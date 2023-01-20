class Potatoes:
    # initializing potato attributes for potato objects
    def __init__(self, ref_date, dguid, area_production_value, uom, uom_id,
                 scalar_factor, scalar_id, vector, coordinate, value, status,
                 symbol, terminated, decimals):
        """initializing function for potatoes object, using the column names as attributes"""
        self.ref_date = ref_date
        self.dguid = dguid
        self.apv = area_production_value
        self.uom = uom
        self.uom_id = uom_id
        self.scalar_function = scalar_factor
        self.scalar_id = scalar_id
        self.vector = vector
        self.coordinate = coordinate
        self.value = value
        self.status = status
        self.symbol = symbol
        self.terminated = terminated
        self.decimals = decimals