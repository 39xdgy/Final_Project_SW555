class Family:
    '''
    This is the class for Family. 
    id is the only variable that is required. If other variable does not exist, it would return None
    If children does not exist, it would return an empty list
    
    all date value are passed in as str, and saved as tuple with formate (year, month, day)
    '''
    def __init__(self, id: str):
        #from Individual import Individual
        self.id = id
        self._husband = None
        self._wife = None
        self._marriedDate = None
        self._divorced = None
        self._children = []

    def get_id(self) -> str:
        return self.id

    def get_husband(self):
        return self._husband

    def get_wife(self):
        return self._wife

    def get_marriedDate(self) -> tuple:
        return self._marriedDate
    
    def get_divorcedDate(self) -> tuple:
        return self._divorced

    def get_children(self) -> list:
        return self._children

    def set_husband(self, husband) -> None:
        ##if not isinstance(husband, Individual): raise TypeError("input has to be a Individual type")
        self._husband = husband
    
    def set_wife(self, wife) -> None:
        
        ##if not isinstance(wife, Individual): raise TypeError("input has to be a Individual type")
        self._wife = wife
    
    def set_marriedDate(self, married_date: tuple) -> None:
        
        ##if not isinstance(married_date, str): raise TypeError("input has to be a str type")
        self._marriedDate = self.change_date_formate(married_date)
    
    def set_divorcedDate(self, divorced_date: tuple) -> None:
        
        ##if not isinstance(divorced_date, str): raise TypeError("input has to be a str type")
        self._divorced = self.change_date_formate(divorced_date)

    def set_children(self, children_list: list) -> None:
        ##if not isinstance(children_list, list): raise TypeError("input has to be a list type")
        self._children = children_list

    def add_child(self, child) -> None:
        '''
        this function would add one kid into the children list
        '''
        ##if not isinstance(child, Individual): raise TypeError("input has to be a Individual type")
        self._children.append(child)

    def change_date_formate(self, date: list) -> tuple:
        '''
        Would take the string input and convert it into a int tuple:(year, month, day)
        '''
        '''
        Would take the string input and convert it into a int tuple:(year, month, day)
        '''
        monthList = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9,
                     "OCT": 10, "NOV": 11, "DEC": 12}
        return int(date[2]), monthList[date[1]], int(date[0])
    


    def multiple_births_lessOrEqual_than_5(self):
        pass

    def marriage_before_divorce(self):
        pass

    def dates_before_current_date(self):
        pass
        
    def marriage_after_14(self):
        pass

    def marriage_before_death(self):
        pass

    def divorce_before_death(self):
        pass

    def birth_before_marriage_of_parents(self):
        pass

    def birth_before_death_of_parents(self):
        pass
