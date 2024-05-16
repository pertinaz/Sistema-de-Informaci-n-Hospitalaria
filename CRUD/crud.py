from abc  import ABC,abstractmethod
from MODELO.doctor import Doctor
from MODELO.hospital import Hospital
search = Doctor.searchByDNI
class Crud(ABC):
    @abstractmethod
    def createHospital(self,**kwargs):
       return Hospital(kwargs['hospitalName'])
    
    @abstractmethod
    def createDoctor(self,**kwargs):
       return Doctor(kwargs['doctorName'],kwargs['speciality'],kwargs['dni'])
    
    @abstractmethod
    def search(self,**kwargs):
        if kwargs is None:
            raise NotImplementedError
        else:
         return search(kwargs['dni'])
        
class DoctorCrud(Crud):
   def createHospital(self,**kwargs):
        return super().createHospital(**kwargs)
   
   def createDoctor(self,**kwargs):
        return super().createDoctor(**kwargs)
   
   def seach(self,**kwargs):
      return super().search(**kwargs)
   
