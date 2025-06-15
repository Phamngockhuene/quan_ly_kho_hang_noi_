'''import pandas as pd

def doc_file(tenfile="KHO.TXT"):
    try:
        df = pd.read_csv(tenfile, sep='|')
        return df.values.tolist()
    except FileNotFoundError:
        print("Chưa có dữ liệu")
        return []

def luu_file(dskho, tenfile="KHO.TXT"):
    df = pd.DataFrame(dskho, columns=["Mã SP", "Tên SP", "Loại", "Số lượng", "Đơn giá"])
    df.to_csv(tenfile, sep='|', index=False, encoding='utf-8')
    print("Đã lưu dữ liệu")

import pandas as pd

def doc_file(tenfile="KHO.TXT"):
    try:
        df = pd.read_csv(tenfile, sep='|')
        return df.values.tolist()
    except FileNotFoundError:
        print("Chưa có dữ liệu.")
        return []

def luu_file(dskho, tenfile="KHO.TXT"):
    df = pd.DataFrame(dskho, columns=["Mã SP", "Tên SP", "Loại", "Số lượng", "Đơn giá"])
    df.to_csv(tenfile, sep='|', index=False, encoding='utf-8')
    print("Đã lưu dữ liệu.")'''


import pandas as pd

def doc_file(tenfile="KHO.TXT"):
    try:
        df = pd.read_csv(tenfile, sep='|')
        return df.values.tolist()
    except FileNotFoundError:
        print("Chưa có dữ liệu")
        return []

def luu_file(dskho, tenfile="KHO.TXT"):
    df = pd.DataFrame(dskho, columns=["Mã SP", "Tên SP", "Loại", "Số lượng", "Đơn giá"])
    df.to_csv(tenfile, sep='|', index=False, encoding='utf-8')
    print("Đã lưu dữ liệu")

