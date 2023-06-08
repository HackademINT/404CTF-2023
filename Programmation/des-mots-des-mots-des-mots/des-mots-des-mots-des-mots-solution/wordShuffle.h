#ifndef WORD_SHUFFLE_H
#define WORD_SHUFFLE_H

#include <vector>
#include <string>

struct letter {
	char c;
	long long index;
};

std::string processWord(std::string&);

void rule2(std::string& str);

void invertString(std::string& toProcess);

void swapParts(std::string& toProcess, size_t middle);

bool vectorContains(std::vector<char> vector, char c);

void removeChars(std::string& toProcess, std::vector<char>& toRemove);

void shiftVowels(std::string& toProcess, bool left);

void rule4o1(std::string& input);

bool compPairs(std::pair<char, long>& lhs, std::pair<char, long>& rhs);

void rule4o2(std::string& input);

#endif