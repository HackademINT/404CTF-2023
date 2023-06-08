#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <filesystem>

#include "wordShuffle.h"

namespace fs = std::filesystem;

int main(const int argc, const char* argv[]) {
	std::ifstream inputFile;
	std::ofstream outputFile;

	if (argc < 3) {
		std::cout << "Pas assez d'arguments, mode mot a mot:\n";

		std::string input;
		while (true) {
			std::cout << "Entrez la valeur : ";

			std::getline(std::cin, input);
			if (input.size() == 1) break;
			std::cout << '\n';

			std::istringstream iss(input);
			std::string word;

			while (iss >> word) {
				std::cout << processWord(word) << ' ';
			}
			std::cout << "\b\n\n";
		}

		return 0;
	}
	else if (argc == 3) {
		auto inputDir{ argv[1] };
		auto outputDir{ argv[2] };

		for (const fs::directory_entry& dir_entry : fs::recursive_directory_iterator(fs::path(inputDir))) {
			if (dir_entry.is_regular_file()) {
				std::cout << dir_entry << '\n';
				inputFile.open(dir_entry.path());
				if (!inputFile.is_open()) {
					std::cout << "error input file open " << dir_entry << '\n';
					return 1;
				}

				std::string outputName{ outputDir + dir_entry.path().filename().string() };
				outputFile.open(outputName);
				if (!inputFile.is_open()) {
					std::cout << "error output file open " << outputName << '\n';
					return 2;
				}
				std::cout << "=>" << outputName << '\n';

				std::string word;
				inputFile >> word;

				outputFile << processWord(word);
				while (inputFile >> word) {
					outputFile << ' ' << processWord(word);
				}

				inputFile.close();
				outputFile.close();
			}
		}

		return 0;
	}
	else {
		std::string word;
		for (int i{ 1 }; i < argc - 1; i++) {
			word = argv[i];
			std::cout << processWord(word) << ' ';
		}
		word = argv[argc - 1];
		std::cout << processWord(word);

		return 0;
	}
}
