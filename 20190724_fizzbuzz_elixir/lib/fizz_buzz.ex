defmodule DojoElixir.FizzBuzz do
  @doc """
    ## Example

      iex > fizz_buzz(0)
      0
  """
  def fizz_buzz(0), do: 0
  def fizz_buzz(number) when rem(number, 3) === 0 and rem(number, 5) === 0, do: :fizz_buzz
  def fizz_buzz(number) when rem(number, 3) === 0, do: :fizz
  def fizz_buzz(number) when rem(number, 5) === 0, do: :buzz
  def fizz_buzz(number), do: number
end