# ========== SORTING & SEARCHING ==========
def selection_sort_waktu(data, ascending=True):
    for i in range(len(data)):
        idx_extreme = i
        for j in range(i + 1, len(data)):
            if (ascending and data[j]["waktu"] < data[idx_extreme]["waktu"]) or \
               (not ascending and data[j]["waktu"] > data[idx_extreme]["waktu"]):
                idx_extreme = j
        data[i], data[idx_extreme] = data[idx_extreme], data[i]
    return data


def binary_search_produk(data, nama):
    hasil = []
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid]['nama'].lower() == nama.lower():
            hasil.append(data[mid])
            break
        elif data[mid]['nama'].lower() < nama.lower():
            left = mid + 1
        else:
            right = mid - 1
    return hasil

def selection_sort_nama(data, ascending=True):
    for i in range(len(data)):
        idx_extreme = i
        for j in range(i + 1, len(data)):
            nama_i = data[idx_extreme]['nama'].lower()
            nama_j = data[j]['nama'].lower()

            if (ascending and nama_j < nama_i) or (not ascending and nama_j > nama_i):
                idx_extreme = j
        data[i], data[idx_extreme] = data[idx_extreme], data[i]
    return data

def insertion_sort_feedback(data, ascending=True):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and ((data[j]["tanggal"] > key["tanggal"]) if ascending else (data[j]["tanggal"] < key["tanggal"])):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
