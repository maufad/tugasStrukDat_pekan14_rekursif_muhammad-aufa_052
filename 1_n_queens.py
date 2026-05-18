"""
TUGAS REKURSIF 1 – N-QUEENS
Mencari solusi penempatan N ratu di papan NxN tanpa saling menyerang
Menggunakan algoritma backtracking rekursif
"""

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        """Cek apakah ratu di (row, col) aman dari serangan"""
        # Cek kolom (ke atas)
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Cek diagonal kiri atas
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Cek diagonal kanan atas
        i, j = row - 1, col + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve(self, row=0):
        """
        Mencari solusi dengan rekursif backtracking
        Returns: True jika solusi ditemukan
        """
        if row == self.n:
            # Simpan solusi
            self.solutions.append([row[:] for row in self.board])
            return True

        found = False
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve(row + 1):
                    found = True
                # Backtrack: hapus ratu
                self.board[row][col] = 0

        return found

    def print_board(self, board=None):
        """Cetak papan solusi"""
        if board is None and self.solutions:
            board = self.solutions[0]
        elif board is None:
            board = self.board

        print("-" * (4 * self.n + 1))
        for row in board:
            print("|", end="")
            for cell in row:
                print(" Q " if cell == 1 else " . ", end="|")
            print()
            print("-" * (4 * self.n + 1))

    def get_all_solutions(self):
        """Dapatkan semua solusi (opsional)"""
        self.solutions = []
        self.solve()
        return self.solutions


def main():
    print("=" * 50)
    print("1. N-QUEENS SOLVER")
    print("=" * 50)

    try:
        n = int(input("Masukkan ukuran papan (n): "))
        if n <= 0:
            print("Ukuran papan harus > 0")
            return

        queens = NQueens(n)
        print(f"\n🔍 Mencari solusi untuk papan {n}x{n}...")

        if queens.solve():
            print("\n✅ SOLUSI DITEMUKAN!\n")
            queens.print_board()
        else:
            print(f"\n❌ Tidak ada solusi untuk papan {n}x{n}")

    except ValueError:
        print("Input harus berupa angka!")


if __name__ == "__main__":
    main()
