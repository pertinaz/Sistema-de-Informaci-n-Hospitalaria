from MODELO.hospital import Hospital
class Doctor(Hospital):
    doctorList = []
    def __init__(self,doctorName,speciality,dni, hospital):
        self.doctorName = doctorName
        self.speciality = speciality
        self.dni = dni
        self.hospital = hospital
        Doctor.doctorList.append(self)
        Hospital.addDoctor(self)

    @staticmethod
    def searchByDNI(dni):
        for doctor in Doctor.doctorList:
            if dni == doctor.dni:
                return doctor
            return None

