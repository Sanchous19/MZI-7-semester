#include <fstream>
#include <iterator>
#include "io.h"

using namespace std;

string SECRET_FILE = "../secret.txt";
string ENCRYPTED_FILE = "../encrypted.txt";
string DECRYPTED_FILE = "../decrypted.txt";

string read_file(const string& filename) {
	ifstream stream(filename, ios::in | ios::binary);
	return string(istreambuf_iterator<char>(stream), istreambuf_iterator<char>());
}

string read_secret_file() {
	return read_file(SECRET_FILE);
}

string read_encrypted_file() {
	return read_file(ENCRYPTED_FILE);
}

void write_to_file(const string& filename, const string& output) {
	ofstream stream(filename, ios::out | ios::binary);
	stream << output;
}

void write_to_encrypted_file(const string& output) {
	write_to_file(ENCRYPTED_FILE, output);
}

void write_to_decrypted_file(const string& output) {
	write_to_file(DECRYPTED_FILE, output);
}
