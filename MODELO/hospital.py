class Hospital():
    hospitalList = []
    def __init__(self,hospitalName):
        self.hospitalName = hospitalName
        self.doctors = []
        Hospital.hospitalList.append(self)
        
    def addDoctor(self,doctor):
        self.doctors.append(doctor)
