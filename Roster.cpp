#include "Roster.h"
#include "Degree.h"
#include "softwareStudent.h"
#include "securityStudent.h"
#include "networkStudent.h"
using std::cout;
using std::cerr;

Roster::Roster() {
	this->capacity = 0;
	this->lastIndex = -1;
	this->roster = nullptr;
}

Roster::Roster(int capacity) {
	this->capacity = capacity;
	this->lastIndex = -1;
	this->roster = new Student*[capacity];
}

void Roster::parseAdd(string row) {
	if (lastIndex < capacity) {
		lastIndex++;
		int parray[Student::daysINCourse];

		if (row.back() == 'Y') {
			this->roster[lastIndex] = new SecurityStudent();
			roster[lastIndex]->setDegreeProgram(SECURITY);
		}
		else if (row.back() == 'K') {
			this->roster[lastIndex] = new NetworkStudent();
			roster[lastIndex]->setDegreeProgram(NETWORK);
		}
		else if (row.back() == 'E') {
			this->roster[lastIndex] = new SoftwareStudent();
			roster[lastIndex]->setDegreeProgram(SOFTWARE);
		}

		int rhs = row.find(",");
		roster[lastIndex]->setID(row.substr(0, rhs));

		int lhs = rhs + 1;
		rhs = row.find(',', lhs);
		roster[lastIndex]->setfName(row.substr(lhs, rhs - lhs));

		lhs = rhs + 1;
		rhs = row.find(',', lhs);
		roster[lastIndex]->setlName(row.substr(lhs, rhs - lhs));

		lhs = rhs + 1;
		rhs = row.find(',', lhs);
		roster[lastIndex]->setemail(row.substr(lhs, rhs - lhs));

		lhs = rhs + 1;
		rhs = row.find(',', lhs);
		roster[lastIndex]->setage(row.substr(lhs, rhs - lhs));

		lhs = rhs + 1;
		rhs = row.find(',', lhs);
		parray[0]=stod(row.substr(lhs, rhs - lhs));

		lhs = rhs + 1;
		rhs = row.find(',', lhs);
		parray[1]=stod(row.substr(lhs, rhs - lhs));

		lhs = rhs + 1;
		rhs = row.find(',', lhs);
		parray[2]=stod(row.substr(lhs, rhs - lhs));

		roster[lastIndex]->setdIC(parray); 

				

	}
	else {
		cerr << "ERROR, LIST HAS EXCEEDED MAXIMUM CAPACITY!\N EXITING NOW!";
		exit(-1);
	}
}

void Roster::print_All()
{
	for (int i = 0; i <= lastIndex; i++)
		roster[i]->print();

}

void Roster::remove(string StudentID)
{
	bool found = false;
	for (int i = 0; i <= lastIndex; i++) {
		if (roster[i]->getID()==StudentID){
			found = true;
			delete roster[i];		
			roster[i] = roster[lastIndex];
			lastIndex--;
			cout << StudentID << " removed." << endl;
		}
			
	}
	if (!found) {
		cout << StudentID << " Not Found." << endl;
	}
	
}

void Roster::printAveragedIC(string StudentID)
{
	for (int i = 0; i <= lastIndex; i++) {
		
		
		if (StudentID == roster[i]->getID()) {
			int* array = roster[i]->getdIC();
			double avg = (array[0] + array[1] + array[2]) / 3.0;
			cout << StudentID << " Average Day In Course: " << avg << endl;
		}
	}
}

void Roster::printInvalidEmail()
{
	string email;
	for (int i = 0; i <= lastIndex; i++) {
		email = roster[i]->getemail();
		if (email.find("@") == string::npos || email.find(".") == string::npos || email.find(" ") != string::npos) {
			cout << email << " Bad Email Address" << endl;
		}
	}
}

void Roster::printByDegreeProgram(DegreeProgram b)
{
	for (int i = 0; i <= lastIndex; i++) {
		
		if (roster[i]->getDegreeProgram() == b)
			roster[i]->print();
	}
}

Roster::~Roster()
{
	for (int i = 0; i <= lastIndex; i++) {
		delete roster[i];
		roster[i] = nullptr;
	}
}

int main() {
	string classRoster[numStudents] =
	{
		"A1,John,Smith,John1989@gm ail.com,20,30,35,40,SECURITY",
		"A2,Suzan,Erickson,Erickson_1990@gmailcom,19,50,30,40,NETWORK",
		"A3,Jack,Napoli,The_lawyer99yahoo.com,19,20,40,33,SOFTWARE",
		"A4,Erin,Black,Erin.black@comcast.net,22,50,58,40,SECURITY",
		"A5,Edward,Carter,ecart60@wgu.edu,35,18,29,35,SOFTWARE"
	};
	Roster roster(5);
	for (int i = 0; i < numStudents; i++) {
		roster.parseAdd(classRoster[i]);
		
	}
	roster.print_All();
	roster.printInvalidEmail();
	for (int i = 0; i < 5; i++) {
		string ID = roster.roster[i]->getID();
		roster.printAveragedIC(ID);
	}
	roster.printByDegreeProgram(SOFTWARE);
	roster.remove("A3");
	roster.remove("A3");
	

	return 0;
}