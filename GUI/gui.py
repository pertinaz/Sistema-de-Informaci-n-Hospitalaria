
import customtkinter as ctk
from customtkinter import *
import CONTROLLER.controller
from MODELO.hospital import Hospital 
hospitalList = Hospital.hospitalList

Controller = CONTROLLER.controller.Controller

class GUISetup(ctk.CTk):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("500x600")
        self.title("Hospital and Doctor Management")

        self.controller = Controller()

        self.buttonFrame = ctk.CTkFrame(self)
        self.buttonFrame.pack(padx=15,pady=15,fill="x")

        self.hospitalButton = ctk.CTkButton(self.buttonFrame, text="Create Hospital", command=self.showHospitalCreation)
        self.hospitalButton.pack(padx=5, pady=5)

        self.doctorButton = ctk.CTkButton(self.buttonFrame, text="Create Doctor", command=self.showDoctorCreation)
        self.doctorButton.pack(padx=5, pady=5)

        self.searchDoctorButton = ctk.CTkButton(self.buttonFrame, text="Search Doctor", command=self.showSearchDoctor)
        self.searchDoctorButton.pack(padx=5, pady=5)

        self.historyButton = ctk.CTkButton(self.buttonFrame, text="History", command=self.history)
        self.historyButton.pack(padx=5, pady=5)

        self.contentFrame = ctk.CTkFrame(self)
        self.contentFrame.pack(padx=15,pady=15,fill="both",expand=True)

        self.saveHospitalInfo.config(command=self.saveHospital)
        self.saveDocInfo.config(command=self.saveDoctor)


    def saveHospital(self):
        hospitalName = self.entryHospitalName.get()
        if hospitalName:
            self.controller.createHospital(hospitalName)

    def saveDoctor(self):
        doctorName = self.entryName.get()
        speciality = self.entrySpeciality.get()
        dni = self.entryDni.get()
        for hospital in hospitalList:
            if hospital in hospitalList:
                hospital = self.hospital.get()  # Debes implementar la lógica para obtener el hospital seleccionado
        if doctorName and speciality and dni and hospital:
            self.controller.createDoctor(doctorName, speciality, dni, hospital)


    def showHospitalCreation(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()
        hospitalCreation = self.HospitalCreation(self.contentFrame)
        hospitalCreation.pack(fill="both",expand=True)

    def showDoctorCreation(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()
        doctorCreation = self.DoctorCreation(self.contentFrame)
        doctorCreation.pack(fill="both",expand=True)

    def showSearchDoctor(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()
        searchDoctor = self.SearchDoctor(self.contentFrame)
        searchDoctor.pack(fill="both",expand=True)

    def history(self):
        for widget in self.contentFrame.winfo_children():
            widget.destroy()
        showHistory = self.History(self.contentFrame)
        showHistory.pack(fill="both",expand=True)

    class HospitalCreation(ctk.CTkFrame):
        def __init__(self,parent,*args,**kwargs):
            super().__init__(parent,*args,**kwargs)

            self.hospitalName = ctk.CTkLabel(self,text="HOSPITAL NAME: ")
            self.hospitalName.pack(padx=5,pady=5)

            self.entryHospitalName = ctk.CTkEntry(self)
            self.entryHospitalName.pack(padx=5,pady=5)

            self.saveHospitalInfo = ctk.CTkButton(self,text="Save Hospital")
            self.saveHospitalInfo.pack(padx=5,pady=5)

    class DoctorCreation(ctk.CTkFrame):
        def __init__(self,parent,*args,**kwargs):
            super().__init__(parent,*args,**kwargs)

            self.doctorName = ctk.CTkLabel(self,text="DOCTOR NAME: ")
            self.doctorName.pack(padx=5,pady=5)

            self.entryName = CTkEntry(self)
            self.entryName.pack(padx=5,pady=5)

            self.speciality = ctk.CTkLabel(self,text="SPECIALITY: ")
            self.speciality.pack(padx=5,pady=5)

            self.entrySpeciality = CTkEntry(self)
            self.entrySpeciality.pack(padx=5,pady=5)

            self.dni = ctk.CTkLabel(self,text="DNI: ")
            self.dni.pack(padx=5,pady=5)

            self.entryDni = CTkEntry(self)
            self.entryDni.pack(padx=5,pady=5)

            self.hospital = ctk.CTkLabel(self,text="HOSPITAL: ")
            self.hospital.pack(padx=5,pady=5)

            self.hospital = ctk.CTkOptionMenu(self,corner_radius=5,command="")
            self.hospital.pack(padx=5,pady=5)

            self.saveDocInfo = ctk.CTkButton(self,text="Save doctor information")
            self.saveDocInfo.pack(padx=5,pady=5)

    class SearchDoctor(ctk.CTkFrame):
        def __init__(self,parent,*args,**kwargs):
            super().__init__(parent,*args,**kwargs)

            self.hospitalSelectionLabel = ctk.CTkLabel(self, text="HOSPITALS")
            self.hospitalSelectionLabel.pack(padx=5, pady=5)


            self.hospitalSelection = ctk.CTkOptionMenu(self,corner_radius=5,)
            self.hospitalSelection.pack(padx=5,pady=5)

            self.searchByDni = ctk.CTkLabel(self,text="Enter the doctor DNI: ")
            self.searchByDni.pack(padx=5,pady=5)

            self.searchEntry = ctk.CTkEntry(self)
            self.searchEntry.pack(padx=5,pady=5)

    class History(ctk.CTkFrame):
        def __init__(self,parent,*args,**kwargs):
            super().__init__(parent,*args,**kwargs)
        
        def createTable(self):
            headers=["HOSPITAL","DNI","NOMBRE DOCTOR","SPECIALITY"]

            #encabezados
            for i,headers in enumerate(headers):
                headerLabel = ctk.CTkLabel(self,text=headers)
                headerLabel.grid(row=0,column=i,padx=5,pady=5)



if __name__ == "__main__":
    app = GUISetup()
    app.mainloop()

