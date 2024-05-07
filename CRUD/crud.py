from abc  import ABC,abstractmethod
from MODELO.doctor import Doctor
search = Doctor.searchByDNI
class Crud(ABC):
    @abstractmethod
    def create(self,**kwargs):
       return Doctor(kwargs['doctorName'],kwargs['speciality'],kwargs['dni'])
    
    @abstractmethod
    def search(self,**kwargs):
        if kwargs == None:
            raise NotImplementedError
        else:
         return search(kwargs['dni'])