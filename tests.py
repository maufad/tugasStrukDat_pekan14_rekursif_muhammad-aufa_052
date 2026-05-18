"""
TESTING UNTUK KETIGA TUGAS REKURSIF
"""

import sys


def test_n_queens():
    print("\n" + "=" * 40)
    print("TEST N-QUEENS")
    print("=" * 40)

    sys.argv = ['1_n_queens.py']
    from 1_n_queens import NQueens

    # Test untuk n=4 (harus punya solusi)
    queens = NQueens(4)
    assert queens.solve() == True, "N=4 seharusnya punya solusi"
    print("✓ N=4 memiliki solusi")

    # Test untuk n=3 (tidak punya solusi)
    queens = NQueens(3)
    queens.solutions = []
    assert queens.solve() == False, "N=3 seharusnya TIDAK punya solusi"
    print("✓ N=3 tidak memiliki solusi")

    print("✅ Semua test N-Queens passed!")


def test_knights_tour():
    print("\n" + "=" * 40)
    print("TEST KNIGHT'S TOUR")
    print("=" * 40)

    from 2_knights_tour import KnightsTour

    # Test papan 5x5 (seharusnya punya solusi dari (0,0))
    knight = KnightsTour(5)
    assert knight.solve_from_position(0, 0) == True, "Papan 5x5 dari (0,0) seharusnya punya solusi"
    print("✓ Papan 5x5 dari (0,0) memiliki solusi")

    # Test papan 8x8 dari (0,0)
    knight = KnightsTour(8)
    assert knight.solve_from_position(0, 0) == True, "Papan 8x8 dari (0,0) seharusnya punya solusi"
    print("✓ Papan 8x8 dari (0,0) memiliki solusi")

    print("✅ Semua test Knight's Tour passed!")


def test_knapsack():
    print("\n" + "=" * 40)
    print("TEST KNAPSACK")
    print("=" * 40)

    from 3_knapsack import Knapsack

    # Test case dari soal
    weights = [2, 5, 6, 9, 12, 14, 20]
    target = 30

    knap = Knapsack(weights, target)
    solution = knap.solve_with_limit()

    assert solution is not None, "Seharusnya ada solusi untuk target 30"
    assert sum(solution) == 30, f"Total berat solusi harus 30, tapi {sum(solution)}"
    print("✓ Knapsack contoh soal: solusi ditemukan")

    # Test case tanpa solusi
    knap = Knapsack([3, 7, 11], 10)
    solution = knap.solve_with_limit()
    assert solution is None, "Seharusnya tidak ada solusi untuk target 10 dengan [3,7,11]"
    print("✓ Knapsack tanpa solusi: bekerja dengan benar")

    print("✅ Semua test Knapsack passed!")


if __name__ == "__main__":
    print("=" * 40)
    print("MENJALANKAN SEMUA TEST")
    print("=" * 40)

    test_n_queens()
    test_knights_tour()
    test_knapsack()

    print("\n" + "=" * 40)
    print("🎉 SEMUA TEST BERHASIL! 🎉")
    print("=" * 40)
