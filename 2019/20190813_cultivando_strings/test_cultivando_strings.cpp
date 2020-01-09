// https://www.urionlinejudge.com.br/judge/pt/problems/view/1141

#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "cultivando_strings.cpp"

#include <string>
#include <vector>
using namespace std;


TEST_CASE("Comecando por uma string " ) {
  vector<string> V = {"a"};
  REQUIRE(cultivandoStrings(V) == 1);
}

TEST_CASE("Duas string sequenciaveis " ) {
  vector<string> V = {"a","ab"};
  REQUIRE(cultivandoStrings(V) == 2);
}

TEST_CASE("Teste 3 strings com sequencia maxima de 2" ) {
  vector<string> V = {"a","ab", "c"};
  REQUIRE(cultivandoStrings(V) == 2);
}

TEST_CASE("Teste 3 strings que não formam sequencia" ) {
  vector<string> V = {"a","jk", "m"};
  REQUIRE(cultivandoStrings(V) == 1);
}

TEST_CASE("Teste 3 strings poderoso" ) {
  vector<string> V = {"ab","a", "c"};
  REQUIRE(cultivandoStrings(V) == 2);
}


