class patient(object):
	def __init__(self, id_number, name, allergies, bed_number):
		self.id = id_number
		self.name = name 
		self.allergies = allergies
		self.bed = bed_number


class hospital(object):
	def __init__(self, hospital_name, max_capacity):
		self.patients = []
		self.hospital_name = hospital_name
		self.max_capacity = max_capacity

	def admit(self, add_patient):
		if len(self.patients)>= self.max_capacity:
			print "We cannot admit the patient, no beds available"
			return self
		else:
			self.patients.append(add_patient)
			return self

	def display_all(self):
		for all in patients:
			print all
	def discharge(self, patient_num):
			print self.patients
			self.patients.remove(patient_num)
			self.bed = "none"
			print self.patients
			return self


patient1 = patient(01, "George", "milk", 01)
patient2 = patient(02, "Fred", "Glucose", 02)
patient3 = patient(03, "Petie", "Fruit", 03)

hospital = hospital("Dojo General", 3)
hospital.admit(patient1).admit(patient2).admit(patient3).discharge(patient2)