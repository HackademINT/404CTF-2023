#include <iostream>
#include <utility>
#include <array>
#include <list>
#include <cmath>
#include <algorithm>

#include "wordShuffle.h"

const std::vector<char> vowels{ {'a', 'e', 'i', 'o', 'u', 'y' } };

std::string processWord(std::string& input) {
	// Rule 1
	invertString(input);
	// Rule 2
	std::string res{ input };
	rule2(res);
	
	if (res.size() < 3) return res;

	// Rule 3
	bool left{ vectorContains(vowels, res[2]) };
	res = input;
	shiftVowels(res, left);

	// Rule 3.2
	rule2(res);

	// Rule 4.1
	rule4o1(res);
	// Rule 4.2
	rule4o2(res);

	return res;
}

// Implements the process of the 2nd rule
void rule2(std::string& str) {
	if (str.size() % 2 == 0) {
		swapParts(str, str.size() / 2);
	}
	else {
		std::vector<char> toRemove{ str[str.size() / 2] };
		removeChars(str, toRemove);
	}
}

// Inverts a string, time linear
void invertString(std::string& toProcess) {
	std::string res;
	for (size_t i{ toProcess.size() }; i >= 1; i--) {
		res.push_back(toProcess[i - 1]);
	}
	toProcess = std::move(res);
}

// Cuts a string in two parts from middle and swaps these parts, time linear
void swapParts(std::string& toProcess, size_t middle) {
	if (middle > toProcess.size()) return;
	toProcess = std::move(toProcess.substr(middle, toProcess.size() - middle).append(toProcess.substr(0, middle)));
}

// Looks if a char vector contains a certain char, time linear (in worst case)
bool vectorContains(std::vector<char> vector, char c) {
	for (char t : vector) {
		if (t == c) {
			return true;
		}
	}
	return false;
}

// Removes all the chars present in the vector in a string, time bilinear (O(arraySize * stringSize))
void removeChars(std::string& toProcess, std::vector<char>& toRemove) {
	std::string res{};
	for (auto c{ toProcess.begin() }; c < toProcess.end(); c++) {
		if (!vectorContains(toRemove, *c)) {
			res.push_back(*c);
		}
	}
	toProcess = std::move(res);
}

// Shifts all the vowels in a string, time linear
void shiftVowels(std::string& toProcess, bool left) {
	if (left) {
		char first{};
		std::string::iterator lastPos{ toProcess.end() };
		for (auto c{ toProcess.begin() }; c < toProcess.end(); c++) {
			if (vectorContains(vowels, *c)) {
				if (lastPos != toProcess.end())	*lastPos = *c;
				else first = *c;
				lastPos = c;
			}
		}
		if (lastPos != toProcess.end()) *lastPos = first;
	}
	else {
		char last{};
		auto lastPos{ toProcess.rend() };
		for (auto c{ toProcess.rbegin() }; c != toProcess.rend(); c++) {
			if (vectorContains(vowels, *c)) {
				if (lastPos != toProcess.rend()) *lastPos = *c;
				else last = *c;
				lastPos = c;
			}
		}
		if (lastPos != toProcess.rend()) *lastPos = last;
	}
}

char findCharToAdd(const char c, const long long s) {
	// Gets the previous vowel in the alphabet
	char vp{};
	// Lowercase case
	if (c >= 97) {
		for (auto v{ vowels.rbegin() }; v < vowels.rend(); v++) {
			if (c - *v > 0) {
				vp = *v;
				break;
			}
		}
	}
	// Capital case
	else {
		for (auto v{ vowels.rbegin() }; v < vowels.rend(); v++) {
			if (c - *v + 32 > 0) {
				vp = *v - 32;
				break;
			}
		}
	}

	// Gets the letter
	return (vp + s) % 95 + 32;
}

// Implements the first part of rule 4
void rule4o1(std::string& input) {
	// Output string
	std::string res{};
	
	//std::list<std::pair<char, long>> buf{};
	// The sum of the vowels
	long long s{};

	// Iterating through the word
	auto f{ input.begin() };
	// The current caracter
	char c{ *f };
	while (true) {
		// Puting the letter at the end of the output word
		res.push_back(c);
		// Doubling the sum
		s <<= 1;

		// Vowel case (lower and capital case (shifting 32 to get lower from capital))
		if (vectorContains(vowels, c) || vectorContains(vowels, c + 32)) {
			// Adding to vowel to the sum
			s += static_cast<long long>(c);

			// Incrementing f and pass to the next letter
			f++;
			if (f < input.end())
				c = *f;
			else break;
		}
		// Consonant case
		else if ((65 <= c && c <= 90) || (97 <= c && c <= 122)) {
			// Getting the letter
			c = findCharToAdd(c, s);
		}
		// Other char are just ignored
		else {
			// Incrementing f and pass to the next letter
			f++;
			if (f < input.end())
				c = *f;
			else break;
		}
	}
	input = std::move(res);
}

// Compares the second element of pairs and the first (for ties)
bool compPairs(std::pair<char, long>& lhs, std::pair<char, long>& rhs) {
	return lhs.second > rhs.second || (lhs.second == rhs.second && lhs.first < rhs.first);
}

// Implements the second part of rule 4
void rule4o2(std::string& input) {
	std::array<std::pair<char, long>, 95> occurances{};
	
	// initialize array
	for (char c{ 0 }; c < 127 - 32; c++)
		occurances[c] = std::pair<char, long>(c + 32, 0);

	// counts letter
	for (auto it{ input.begin() }; it < input.end(); it++)
		occurances[static_cast<size_t>(* it - 32)].second++;

	// sort array
	std::sort(occurances.begin(), occurances.end(), compPairs);

	// The result
	std::string res{};

	// Reconstructing the String
	for (auto it{ occurances.begin() }; it < occurances.end(); it++)
		while (it->second > 0) {
			res.push_back(it->first);
			it->second--;
		}

	input = std::move(res);
}


