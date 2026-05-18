"""
TUGAS REKURSIF 3 – KNAPSACK
Mencari kombinasi barang yang berat totalnya tepat mencapai target berat
Menggunakan algoritma rekursif backtracking
"""

class Knapsack:
    def __init__(self, weights, target):
        self.weights = weights
        self.target = target
        self.n = len(weights)
        self.solutions = []

    def solve(self, index=0, current_sum=0, selected=None):
        """
        Mencari kombinasi barang dengan rekursif backtracking
        """
        if selected is None:
            selected = []

        # Base case: target tercapai
        if current_sum == self.target:
            self.solutions.append(selected[:])
            return True

        # Base case: sudah melewati target atau habis barang
        if current_sum > self.target or index >= self.n:
            return False

        found = False

        # Opsi 1: Ambil barang ke-index
        selected.append(self.weights[index])
        if self.solve(index + 1, current_sum + self.weights[index], selected):
            found = True
        selected.pop()  # Backtrack

        # Opsi 2: Lewati barang ke-index
        if self.solve(index + 1, current_sum, selected):
            found = True

        return found

    def solve_with_limit(self, index=0, current_sum=0, selected=None):
        """
        Versi: mencari satu solusi saja (lebih cepat untuk data besar)
        """
        if selected is None:
            selected = []

        if current_sum == self.target:
            return selected

        if current_sum > self.target or index >= self.n:
            return None

        # Coba ambil barang ini
        result = self.solve_with_limit(index + 1, current_sum + self.weights[index], selected + [self.weights[index]])
        if result is not None:
            return result

        # Coba lewati barang ini
        return self.solve_with_limit(index + 1, current_sum, selected)

    def get_all_solutions(self):
        """Dapatkan semua solusi yang mungkin"""
        self.solutions = []
        self.solve()
        return self.solutions

    def print_solution(self, solution):
        """Cetak solusi"""
        if solution:
            print(f"\n✅ SOLUSI DITEMUKAN!")
            print(f"   Barang yang dipilih: {solution}")
            print(f"   Jumlah barang: {len(solution)}")
            print(f"   Total berat: {sum(solution)}")
        else:
            print(f"\n❌ Tidak ada kombinasi yang tepat mencapai berat {self.target}")


def main():
    print("=" * 50)
    print("3. KNAPSACK SOLVER")
    print("=" * 50)

    # Contoh dari soal
    print("\n📌 Contoh dari soal:")
    print("   Barang: 2, 5, 6, 9, 12, 14, 20")
    print("   Target: 30\n")

    weights = [2, 5, 6, 9, 12, 14, 20]
    target = 30

    knap = Knapsack(weights, target)
    solution = knap.solve_with_limit()

    if solution:
        print(f"✅ Solusi: {solution}")
        print(f"   (2 + 5 + 9 + 14 = {sum(solution)})")
    else:
        print("❌ Tidak ada solusi")

    # Input kustom
    print("\n" + "=" * 50)
    print("🔧 MODE KUSTOM")
    print("=" * 50)

    try:
        use_custom = input("\nIngin mencoba data sendiri? (y/n): ").lower()
        if use_custom == 'y':
            weights_input = input("Masukkan berat barang (pisahkan dengan koma): ")
            weights = [int(w.strip()) for w in weights_input.split(",")]
            target = int(input("Masukkan berat target: "))

            knap = Knapsack(weights, target)
            solution = knap.solve_with_limit()

            print("\n" + "=" * 50)
            if solution:
                print("✅ SOLUSI DITEMUKAN!")
                print(f"   Barang dipilih: {solution}")
                print(f"   Total berat: {sum(solution)}")
            else:
                print("❌ TIDAK ADA SOLUSI")

    except ValueError:
        print("Input tidak valid!")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
