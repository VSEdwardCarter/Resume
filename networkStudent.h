#pragma once
#include<string>
#include"Degree.h"
#include"Student.h"

class NetworkStudent : public Student {
public:
	NetworkStudent();

	NetworkStudent(
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

	~NetworkStudent();


};