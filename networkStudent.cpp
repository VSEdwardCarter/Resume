#include<iostream>
#include"networkStudent.h"
using std::cout;

NetworkStudent::NetworkStudent() {
	setDegreeProgram(NETWORK);
}

NetworkStudent::NetworkStudent(string StudentID, string firstName, string lastName, string emailAddress, string age, int* dIC, DegreeProgram DegreeProgram) {
	setDegreeProgram(NETWORK);
}

DegreeProgram NetworkStudent::getDegreeProgram() {
	return NETWORK;
}
void NetworkStudent::setDegreeProgram(DegreeProgram b) {
	this->type = NETWORK;
}

void NetworkStudent::print() {
	this->Student::print();
	cout << "NETWORK" << "\n";
}


NetworkStudent::~NetworkStudent() {
	Student::~Student();
	delete this;
}