def xeploai_hocsinh(duong_dan_xep_loai):
    dict_xep_loai = {}
    
    with open(duong_dan_xep_loai, "r", encoding="utf-8") as f:
        # Bỏ dòng tiêu đề
        header = f.readline()
        
        for line in f:
            line = line.strip()

            #Không lỗi nếu xuất hiện dòng trống
            if not line: continue
            
            # Tách các cột dựa trên dấu ;
            parts = line.split(";")
            
            # Mã học sinh
            ma_hs = parts[0].strip()

            # Gán giá trị điểm cho các môn
            Toan = float(parts[1])
            Ly = float(parts[2])
            Hoa = float(parts[3])
            Sinh = float(parts[4])
            Van = float(parts[5])
            Anh = float(parts[6])
            Su = float(parts[7])
            Dia = float(parts[8])

            #Tìm điểm số nhỏ nhất 
            tat_ca_diem = [Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia]
            min_diem = min(tat_ca_diem)

            #Tính điểm trung bình chuẩn
            dtb_chuan = ((Toan + Van + Anh) * 2 + (Ly + Hoa + Sinh + Dia))/11

            #Xếp loại học lực học sinh
            if  dtb_chuan > 9.0 and min_diem > 8.0:
                xep_loai = "Xuat sac"
            elif dtb_chuan > 8.0 and min_diem > 6.5:
                xep_loai = "Gioi"
            elif dtb_chuan > 6.5 and min_diem > 5.0:
                xep_loai = "Kha"
            elif dtb_chuan > 6.0 and min_diem > 4.5:
                xep_loai = "TB kha"
            else:
                xep_loai = "TB"
            
            #Tạo một Dict xếp loại học sinh:
            dict_xep_loai[ma_hs] = xep_loai 
    return dict_xep_loai

        
def xeploai_thidaihoc_hocsinh(duong_dan_khoi):
    dict_xep_loai_K = {}
    with open(duong_dan_khoi, "r", encoding="utf-8") as f:
        # Bỏ dòng tiêu đề
        header = f.readline()
        
        for line in f:
            line = line.strip()

            #Không lỗi nếu xuất hiện dòng trống
            if not line: continue
            
            # Tách các cột dựa trên dấu ;
            parts = line.split(";")
            
            # Mã học sinh
            ma_hs = parts[0].strip()

            # Gán giá trị điểm cho các môn
            Toan = float(parts[1])
            Ly = float(parts[2])
            Hoa = float(parts[3])
            Sinh = float(parts[4])
            Van = float(parts[5])
            Anh = float(parts[6])
            Su = float(parts[7])
            Dia = float(parts[8])

            #Điểm trung bình các khối
            Diem_TB_KA = Toan + Ly + Hoa
            Diem_TB_KA1 = Toan + Ly + Anh
            Diem_TB_KB = Toan + Hoa + Sinh
            Diem_TB_KC = Van + Su + Dia
            Diem_TB_KD = Toan + Van + Anh*2

            #Xep loai khoi A
            if Diem_TB_KA >= 24:
                xep_loai_KA = 1
            elif Diem_TB_KA >= 18:
                xep_loai_KA = 2
            elif Diem_TB_KA >= 12:
                xep_loai_KA = 3
            else:
                xep_loai_KA = 4

            #Xep loai khoi A1
            if Diem_TB_KA1 >= 24:
                xep_loai_KA1 = 1
            elif Diem_TB_KA1 >= 18:
                xep_loai_KA1 = 2
            elif Diem_TB_KA1 >= 12:
                xep_loai_KA1 = 3
            else:
                xep_loai_KA1 = 4

            #Xep loai khoi B
            if Diem_TB_KB >= 24:
                xep_loai_KB = 1
            elif Diem_TB_KB >= 18:
                xep_loai_KB = 2
            elif Diem_TB_KB >= 12:
                xep_loai_KB = 3
            else:
                xep_loai_KB = 4


            #Xep loai khoi C
            if Diem_TB_KC >= 21:
                xep_loai_KC = 1
            elif Diem_TB_KC >= 15:
                xep_loai_KC = 2
            elif Diem_TB_KC >= 12:
                xep_loai_KC = 3
            else:
                xep_loai_KC = 4


            #Xep loai khoi D
            if Diem_TB_KD >= 32:
                xep_loai_KD = 1
            elif Diem_TB_KD >= 24:
                xep_loai_KD = 2
            elif Diem_TB_KD >= 20:
                xep_loai_KD = 3
            else:
                xep_loai_KD = 4

            dict_xep_loai_K[ma_hs] = [xep_loai_KA, xep_loai_KA1, xep_loai_KB, xep_loai_KC, xep_loai_KD]
    return(dict_xep_loai_K)


def main():
    #Khai báo input và output:
    input = "diem_trungbinh.txt"
    output = "danhgia_hocsinh.txt"


    #Thực thi hàm xeploai_hocsinh
    ket_qua_xep_loai = xeploai_hocsinh(input)
    ket_qua_xep_khoi = xeploai_thidaihoc_hocsinh(input)

    #Tạo file output và lưu kết quả vào file “danhgia_hocsinh.txt"
    with open (output, "w", encoding = "utf - 8") as f:

        #Hàng đầu tiên của file “diem_trungbinh.txt” giữ nguyên như của “diem_chitiet.txt”
        f.write("Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B, xeploai_C, xeploai_D\n")

        #Gọi từng mã học sinh:
        for ma_hs in ket_qua_xep_loai.keys():

            #Kết quả xếp loại
            xep_loai_tb = ket_qua_xep_loai[ma_hs]

            #Kết quả xếp loại khối
            xep_loai_khoi = ket_qua_xep_khoi[ma_hs]

            # Chuyển list số [1, 1, 1, 3, 2] thành chuỗi "1;1;1;3;2" 
            str_xep_loai_khoi = ";".join(map(str, xep_loai_khoi))

            # Tạo dòng dữ liệu hoàn chỉnh: "MaHS;LoaiTB;A;A1;B;C;D"
            line = f"{ma_hs};{xep_loai_tb};{str_xep_loai_khoi}\n"
            
            # Ghi vào file
            f.write(line)


# Đảm bảo hàm main được chạy khi gọi chương trình
if __name__ == "__main__":
    main()