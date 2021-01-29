#pragma once

#include <string>

using namespace std;

string read_secret_file();
string read_encrypted_file();

void write_to_encrypted_file(const string& output);
void write_to_decrypted_file(const string& output);
