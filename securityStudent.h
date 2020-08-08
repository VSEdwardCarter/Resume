#pragma once
#include<string>
#include"Degree.h"
#include"Student.h"

class SecurityStudent : public Student {
public:
	SecurityStudent();

	SecurityStudent(
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

	~SecurityStudent();


};