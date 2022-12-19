defmodule Day9 do
  def read() do
    sP = %{x: 0, y: 0}

    "229.in"
    |> File.read!()
    |> String.split("\r\n")
    |> Enum.map(&String.split(&1, " "))
    |> Enum.map(&%{dir: hd(&1), step: &1 |> List.last() |> String.to_integer()})
    |> then(fn x -> move(x, sP, [sP]) end)
  end

  def get_neigh(el),
    do:
      for(
        {x, y} <- [{0, 0}, {1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {-1, -1}, {-1, 1}, {1, -1}],
        do: %{x: el.x + x, y: el.y + y}
      )

  def move(mv, _ph, pt) when length(mv) == 0 do
    pt
    |> Enum.uniq()
    |> Enum.sum()
  end

  def move([mh | mt], ph, pt) do
    inspect(ph)
    inspect(pt)
    nph = mv_head(ph, mh)
    npt = mv_tail(nph, pt, 1)
    move(mt, List.last(nph), npt)
  end

  def mv_tail(r, t, i) when length(r) == i, do: t

  def mv_tail(r, t, i) do
    ct = t |> List.last()
    f = Enum.at(r, i)

    case Enum.member?([], ct) do
      true -> mv_tail(r, t, i + 1)
      false -> mv_tail(r, [Enum.at(t, i - 1) | t], i + 1)
    end
  end

  def mv_head(ph, %{dir: "R", step: step}),
    do: for(x <- 0..step, do: %{x: x + ph.x, y: ph.y})

  def mv_head(ph, %{dir: "L", step: step}),
    do: for(x <- 0..step, do: %{x: ph.x - x, y: ph.y})

  def mv_head(ph, %{dir: "U", step: step}),
    do: for(y <- 0..step, do: %{x: ph.x, y: ph.y + y})

  def mv_head(ph, %{dir: "D", step: step}),
    do: for(y <- 0..step, do: %{x: ph.x, y: ph.y - y})
end

Day9.read()
