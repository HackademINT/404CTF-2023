CXX=g++
CXXFLAGS=-g -std=c++17 -Wall

all: main

main: main.o wordShuffle.o
	$(CXX) main.cpp wordShuffle.cpp -o main $(CXXFLAGS)

clean:
	rm -f *.o ./main