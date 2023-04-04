class student:
   
    def __init__(self, id, first_name, last_name, grade, l, f):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._grade = grade
        self._letter = l
        self.final = f

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_first_name(self):
        return self._first_name
    
    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, last_name):
        self._last_name = last_name
    
    def get_grade(self):
        return self._grade
    
    def set_grade(self, grade):
        self._grade = grade
    
    def get_letter(self):
        return self._letter

    def set_final(self, final):
        self.final = final

    def get_final(self):
        return self.final
        



