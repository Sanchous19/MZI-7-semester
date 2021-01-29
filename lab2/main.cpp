#include <string>

#include "stb.h"

int main() {
	std::string synchro = "verygoodsynchro.";
	std::string key = "Lorem ipsum dolor amet, consect."; //"verygoodkeyverygoodkeyverygoodke";

	STB stb = STB(key, synchro);

	stb.encrypt_plain();
	stb.decrypt_plain();

	return 0;
}
