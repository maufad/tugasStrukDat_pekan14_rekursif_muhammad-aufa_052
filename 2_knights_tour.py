"""
TUGAS REKURSIF 2 – KNIGHT'S TOUR
Mencari urutan langkah kuda yang mengunjungi semua petak papan tepat satu kali
Menggunakan algoritma backtracking rekursif + heuristik Warnsdorff
"""

class KnightsTour:
    # Pergerakan kuda (8 kemungkinan)
    MOVES = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    def __init__(self, size=8):
        self.size = size
        self.board = [[-1] * size for _ in range(size)]
        self.total_moves = size * size

    def is_valid(self, x, y):
        """Cek apakah posisi (x, y) valid dan belum dikunjungi"""
        return 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == -1

    def count_valid_moves(self, x, y):
        """Hitung jumlah langkah valid dari posisi (x, y) – untuk heuristik"""
        count = 0
        for dx, dy in self.MOVES:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                count += 1
        return count

    def get_sorted_moves(self, x, y):
        """
        Dapatkan daftar langkah yang diurutkan berdasarkan heuristik Warnsdorff
        (prioritaskan langkah dengan jumlah pilihan paling sedikit)
        """
        moves_with_count = []
        for dx, dy in self.MOVES:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                count = self.count_valid_moves(nx, ny)
                moves_with_count.append((count, nx, ny))

        # Urutkan dari yang paling sedikit pilihannya
        moves_with_count.sort()
        return [(nx, ny) for _, nx, ny in moves_with_count]

    def solve(self, x, y, move_num=1):
        """
        Mencari solusi tur kuda dengan rekursif backtracking
        """
        if move_num == self.total_moves:
            return True

        # Heuristik Warnsdorff: coba langkah dengan pilihan paling sedikit dulu
        for nx, ny in self.get_sorted_moves(x, y):
            self.board[nx][ny] = move_num
            if self.solve(nx, ny, move_num + 1):
                return True
            self.board[nx][ny] = -1  # Backtrack

        return False

    def print_board(self):
        """Cetak papan dengan urutan langkah"""
        print("-" * (6 * self.size + 1))
        for row in self.board:
            print("|", end="")
            for cell in row:
                print(f" {cell:2d} ", end="|")
            print()
            print("-" * (6 * self.size + 1))

    def reset(self):
        """Reset papan"""
        self.board = [[-1] * self.size for _ in range(self.size)]

    def solve_from_position(self, start_x, start_y):
        """Mulai tur dari posisi tertentu"""
        self.reset()
        self.board[start_x][start_y] = 0
        return self.solve(start_x, start_y)


def main():
    print("=" * 50)
    print("2. KNIGHT'S TOUR SOLVER")
    print("=" * 50)

    try:
        size = int(input("Masukkan ukuran papan (default 8): ") or 8)
        start_x = int(input("Masukkan baris awal (0-{}): ".format(size - 1)))
        start_y = int(input("Masukkan kolom awal (0-{}): ".format(size - 1)))

        if not (0 <= start_x < size and 0 <= start_y < size):
            print("Posisi awal tidak valid!")
            return

        knight = KnightsTour(size)
        print(f"\n🔍 Mencari tur kuda dari ({start_x}, {start_y})...")

        if knight.solve_from_position(start_x, start_y):
            print("\n✅ SOLUSI DITEMUKAN! (Angka menunjukkan urutan langkah)\n")
            knight.print_board()
        else:
            print(f"\n❌ Tidak ada solusi untuk papan {size}x{size} dari posisi ({start_x}, {start_y})")

    except ValueError:
        print("Input harus berupa angka!")


if __name__ == "__main__":
    main()
