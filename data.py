
class Data:
    __diasMax = [31,28,31,30,31,30,31,31,30,31,30,31,30,31]

    def __init__(self, dia:int, mes:int, ano:int=2023) -> None:
        self.setData(dia, mes, ano)
    
    def __str__(self) -> str:
        return f'{self.dia}/{self.mes}/{self.ano}'

    @property
    def dia(self) -> int:
        return self.__dia
    
    @dia.setter
    def dia (self, dia):
        diaMax = Data.__diasMax[self.mes-1]
        if dia < 1 or dia > diaMax:
            return
        
        self.__dia = dia

    @property
    def mes(self) -> int:
        return self.__mes
    
    @mes.setter
    def mes (self, mes):
        if mes < 1 or mes > 12:
            return
        self.__mes = mes


    @property
    def ano(self) -> int:
        return self.__ano
    
    @ano.setter
    def ano (self, ano):
        if ano < 0:
            return
        self.__ano = ano



    def setData(self, dia:int, mes:int, ano:int):
        if mes < 1 or mes > 12:
            return
        
        diaMax = Data.__diasMax[mes-1]
        if dia < 1 or dia > diaMax:
            return
        if ano < 0:
            return
        
        self.mes = mes
        self.dia = dia
        self.ano = ano