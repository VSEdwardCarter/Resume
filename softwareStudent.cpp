#include<iostream>
#include<string>
#include"softwareStudent.h"
#include"Degree.h"
using std::cout;

SoftwareStudent::SoftwareStudent() {
	setDegreeProgram(SOFTWARE);
}

SoftwareStudent::SoftwareStudent (string StudentID, string firstName, string lastName, string emailAddress, string age, int* dIC, DegreeProgram DegreeProgram) {
	setDegreeProgram(SOFTWARE);
}

DegreeProgram SoftwareStudent::getDegreeProgram() {
	return SOFTWARE;
}
void SoftwareStudent::setDegreeProgram(DegreeProgram b) {
	type = SOFTWARE;
}

void SoftwareStudent::print() {
	Student::print();
	cout << "SOFTWARE" << endl;
}

SoftwareStudent:: ~SoftwareStudent() {
	Student::~Student();
	delete this;
}