import datetime


class Individual:
    '''
    This is the class for individual. 
    id is the only variable that is required. If other variable does not exist, it would return None
    If children/spouse does not exist, it would return an empty list
    
    all date value are passed in as str, and saved as tuple with formate (year, month, day)
    '''

    def __init__(self, id: str):
        self.id = id
        self._name = None
        self._gender = None
        self._birthDate = None
        self._deathDate = None
        self._family = []
        self._parentFamily = None

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self._name

    def get_gender(self) -> str:
        return self._gender

    def get_birthDate(self) -> tuple:
        return self._birthDate

    def get_age(self) -> int:
        '''
        calculate age base on the birthdate. If birthdate is None, this would return None

        require datetime module
        '''
        if not self._birthDate: return -1
        today = datetime.datetime.now()
        return today.year - self._birthDate[0] - ((today.month, today.day) < (self._birthDate[1], self._birthDate[2]))

    def get_deathDate(self) -> tuple:
        return self._deathDate

    def get_family(self):
        return self._family

    def get_parent_family(self):
        return self._parentFamily

    def set_name(self, name: str) -> None:
        # if not isinstance(name, str): raise TypeError("input has to be a str type")
        self._name = name

    def set_gender(self, gender: str) -> None:
        # if not isinstance(gender, str): raise TypeError("input has to be a str type")
        self._gender = gender

    def set_birthDate(self, birth_date: list) -> None:
        # if not isinstance(birth_date, str): raise TypeError("input has to be a str type")
        self._birthDate = self.change_date_formate(birth_date)

    def set_deathDate(self, death_date: list) -> None:
        # if not isinstance(death_date, str): raise TypeError("input has to be a str type")
        self._deathDate = self.change_date_formate(death_date)

    def add_to_family(self, family) -> None:
        # if not isinstance(family, list): raise TypeError("input has to be a list type")
        self._family.append(family)

    def set_parentFamily(self, parent_family) -> None:
        # if not isinstance(parent_family, family): raise TypeError("input has to be a family type")
        self._parentFamily = parent_family


    def change_date_formate(self, date: list) -> tuple:
        '''
        Would take the string input and convert it into a int tuple:(year, month, day)
        '''
        monthList = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9,
                     "OCT": 10, "NOV": 11, "DEC": 12}
        return int(date[2]), monthList[date[1]], int(date[0])

    def dates_before_current_date(self):
        pass

    def birth_before_marriage(self):
        pass

    def birth_before_death(self):
        pass

    def less_then_150_years_old(self):
        pass

    def no_bigamy(self):
        pass

    def siblings_spacing(self):
        pass

    def parents_not_too_old(self):
        pass