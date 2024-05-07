from MODELO.hospital import Hospital
class Doctor(Hospital):
    def __init__(self,doctorName,speciality,dni):
        self.doctorName = doctorName
        self.speciality = speciality
        self.dni = dni

        self.doctorList = []
    @classmethod
    def searchByDNI(cls,dni):
        for doctor in cls.doctorList:
            if dni == doctor.dni:
                print(f"Doctor: {cls.doctorName}")
                print(f"Especialdad: {Doctor.speciality}")
                print(f"DNI: {Doctor.dni}")
            else:
                raise('Doctor not found')

