#include<iostream>
#include"securityStudent.h"
using std::cout;

SecurityStudent :: SecurityStudent() {
	setDegreeProgram(SECURITY);
}

SecurityStudent::SecurityStudent(string StudentID, string firstName, string lastName, string emailAddress, string age, int* dIC, DegreeProgram DegreeProgram) {
	setDegreeProgram(SECURITY);
}

DegreeProgram SecurityStudent::getDegreeProgram() {
	return SECURITY;
}
void SecurityStudent::setDegreeProgram(DegreeProgram b) {
	this->type = SECURITY;
}

void SecurityStudent::print() {
	this->Student::print();
	cout << "SECURITY" << "\n";
}

SecurityStudent::~SecurityStudent() {
	Student::~Student();
	delete this;
}