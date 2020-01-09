defmodule DojoElixirTest do
  use ExUnit.Case
  doctest DojoElixir.FizzBuzz

  test "given a number that is not multiple returns number" do
    result = DojoElixir.FizzBuzz.fizz_buzz(0)

    assert result == 0
  end

  test "given a number that is multiple of 3 return :fizz" do
    result = DojoElixir.FizzBuzz.fizz_buzz(3)

    assert result == :fizz
  end

  test "given a number that is multiple of 5 return :buzz" do
    result = DojoElixir.FizzBuzz.fizz_buzz(5)

    assert result == :buzz
  end

  test "given a number that is multiple of 5 and multiple of 3 return :fizz_buzz" do
    result = DojoElixir.FizzBuzz.fizz_buzz(15)

    assert result == :fizz_buzz
  end

  test "given a number which does not fit in any test returns the number" do
    result = DojoElixir.FizzBuzz.fizz_buzz(7)

    assert result == 7
  end

end
