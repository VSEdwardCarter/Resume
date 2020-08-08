#pragma once
#include<string>
#include"Degree.h"
#include"Student.h"

class SoftwareStudent : public Student {
	public:
		SoftwareStudent();

		SoftwareStudent(
			string StudentID,
			string firstName,
			string lastName,
			string emailAddress,
			string age,
			int* dIC,
			DegreeProgram DegreeProgram
			); 

		DegreeProgram getDegreeProgram();
		void setDegreeProgram(DegreeProgram b);
		void print();

		~SoftwareStudent();


};