using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace aoc
{
    public class D20
    {
        public void Start()
        {
            var file = File.ReadAllLines("aoc/day22.in");
            var hashes = new string[file.Length];
            var li = new List<(int e, string h)>();
            for (var i = 0; i < file.Length; i++)
            {
                var g = Guid.NewGuid().ToString();
                hashes[i] = g;
                li.Add((int.Parse(file[i]), g));
            }

            int[] res = new int[3];

            int cIndex = 0;

            System.Console.WriteLine(li.MaxBy(x => x.e).e);
            System.Console.WriteLine(li.MinBy(x => x.e).e);
            return;
            for (var i = 1; i < 8; i++)
            {
                Move(li, hashes[cIndex]);
                cIndex++;
                if (cIndex >= li.Count) cIndex = 0;
                if (i % 1000 == 0) AddRes(res, li, i);
                System.Console.WriteLine(string.Join(", ", li.Select(x => x.e)));
            }
            //System.Console.WriteLine(string.Join(", ", res));
        }

        public void AddRes(int[] res, List<(int e, string h)> d, int it)
        {
            for (var i = 0; i < d.Count; i++)
            {
                if (d[i].e == 0)
                {
                    if (i + 1 == d.Count)
                    {
                        res[(it - 100) / 1000] = d[0].e;
                    }
                    else
                    {
                        res[(it - 100) / 1000] = d[i + 1].e;
                    }
                    return;
                }
            }
            throw new Exception("0 not found");
        }

        public void Move(List<(int e, string h)> d, string hash)
        {
            var index = d.FindIndex(x => x.h == hash);
            var el = d[index];
            var newIndex = index + el.e;
            if (newIndex < 0) newIndex = d.Count - newIndex;
            if (newIndex >= d.Count) newIndex -= d.Count;

            d.RemoveAt(index);
            d.Insert(newIndex, el);
        }
    }
}
