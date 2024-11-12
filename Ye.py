class Ye:
    @staticmethod
    def y(p:bool, q:bool)-> bool:
        """ Conjunción
            Devuelve True cuando ambas proposiciones son True,
            devuelve False en cualquier otro caso.
        """
        if p:
            return q
        else:
            return False
    
    verdadero=True
    
    @staticmethod
    def getTrue():
        return Ye.verdadero


