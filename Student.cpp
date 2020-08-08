#include<iostream>
#include<iomanip>
#include "Student.h"
using namespace std;

Student::Student() { //Default Constructor
	this->StudentID = "";
	this->firstName = "";
	this->lastName = "";
	this->emailAddress = "";
	this->age = "";
	this->dIC = new int[daysINCourse];
	for (int i = 0; i < daysINCourse; i++) this->dIC[i] = 0;
}

//Full Constructor
Student::Student(string ID, string fName, string lName, string email, string age, int dIC[], DegreeProgram type) {
	this->StudentID = ID;
	this->firstName = fName;
	this->lastName = lName;
	this->emailAddress = email;
	this->age = age;
	this->dIC = new int[daysINCourse];
	for (int i = 0; 1 < 3; i++) this->dIC[i] = dIC[i];
}

//Getters
string Student::getID() {
	return StudentID;
}
	
string Student::getfName() {
	return firstName;
}

string Student::getlName() {
	return lastName;
}

string Student::getemail() {
	return emailAddress;
}

string Student::getage() {
	return age;
}

int* Student::getdIC() {
	return dIC;
}

//Setters
void Student::setID(string ID) {
	StudentID = ID;
}

void Student::setfName(string fName) {
	firstName = fName;
}

void Student::setlName(string lName) {
	lastName = lName;

}

void Student::setemail(string email) {
	emailAddress = email;
}

void Student::setage(string age) {
	age = age;
}
void Student::setdIC(int dIC[]) {
	if (this->dIC != nullptr) {
		delete[] this->dIC;
		this->dIC = nullptr;
	}
	this->dIC = new int[daysINCourse];
	for (int i = 0; i < 3; i++)
		this->dIC[i] = dIC[i];
}

void Student::print() {
	cout << left << setw(5) << StudentID;
	cout << left << setw(45) << firstName;
	cout << left << setw(45) << lastName;
	cout << left << setw(20) << emailAddress;
	cout << left << setw(20) << age;
	cout << left << setw(10) << dIC[0];
	cout << left << setw(10) << dIC[1];
	cout << left << setw(10) << dIC[2];
}

Student::~Student() {
	if (dIC != nullptr) {
		delete[] dIC;
		dIC = nullptr;
	}
}