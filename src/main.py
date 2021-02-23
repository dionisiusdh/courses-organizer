from graph import *

# Variabel Global
semester_romawi = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VII'} # Konversi semester angka ke romawi
exit = False    # Status exit program

while (not exit):
    result = []     # Hasil pengambilan mata kuliah
    semester = 1    # Semester tracker

    # Meminta input nama file
    # Input dalam bentuk nama file saja, tanpa path dan ekstensi (Asumsi path selalu di ./test/)
    file_name = str(input("\nMasukkan nama file yang ingin diproses (tanpa path / ekstensi, contoh: 3): "))

    # Membuat graph dari file teks terkait
    g2 = makeGraphFromTxt(file_name)
    g2.printGraph()

    # Lakukan iterasi pencarian mata kuliah selama graph belum kosong
    while (not g2.isGraphEmpty()):
        lowest_degree_v = getLowestDegree(g2)   # Mengambil vertex dengan derajat masuk terendah
        
        print(f"Semester {semester_romawi[semester]} mengambil: {', '.join(lowest_degree_v)}")  # Output matakuliah yang dapat diambil

        # Manipulasi graph dengan mendelete vertex terkait
        curr = []
        for v in lowest_degree_v:
            curr.append(v)
            removeAllEdgeFrom(g2, v)
        result.append(curr)

        print(result)

        # Mencetak graph
        print("\nGraph:")
        g2.printGraph()

        # Mencetak sisa jumlah mata kuliah
        print(f"Jumlah mata kuliah tersisa: {g2.V}")

        semester += 1

    # Output hasil akhir
    print("\nSelesai merencanakan pengambilan mata kuliah.\n")

    for i in range(len(result)):
        print(f"Semester {semester_romawi[i+1]}: ", end="")
        print(result[i][0], end="")
        for j in range(1, len(result[i])):
            print(f", {result[i][j]}", end="")
        print()
    
    # Pilihan exit
    exit_choice = str(input("\nApakah anda ingin memproses file lain? (Y/N): "))
    if (exit_choice == "N" or exit_choice == "n"):
        exit = True

print("\nTerima kasih telah menggunakan program ini!")
