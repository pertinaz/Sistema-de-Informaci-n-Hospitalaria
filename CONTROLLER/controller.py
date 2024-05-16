from MODELO import doctor,hospital
from CRUD.crud import DoctorCrud

class Controller():
    def __init__(self):
        self.crud = DoctorCrud()
    
    def createHospital(self,hospitalName):
        hospital = self.crud.createHospital(hospitalName = hospitalName)
        return hospital

    def createDoctor(self,doctorName,speciality,dni,hospital):
        doctor = self.crud.createDoctor(doctorName=doctorName,speciality=speciality,dni=dni,hospital=hospital)
        return doctor
    
    def searchDoctor(self,dni):
        doctor = self.crud.search(dni=dni)
        if doctor:
            return f"Información del doctor \n {doctor.doctorName},{doctor.speciality},{doctor.dni}, Hospital: {doctor.hospitalName}"
        else:
            return "Doctor no encontrado."
