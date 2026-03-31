
# ----Hàm tính điểm----
def tinhdiem_trungbinh(duong_dan_input):

    #Tạo Dict lớn
    Dict_ten_diem = {}


    with open (duong_dan_input, "r", encoding = "utf-8") as f:
    #Loại cái tiêu đề Ma HS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia
        header = f.readline()

        for line in f:

            #Loại bỏ khoảng trống
            line = line.strip()

            #Không lỗi nếu xuất hiện dòng trống
            if not line: continue

            #Tách dòng ra 6 phần dựa trên dấu ;
            parts = line.split(";")

            #Đưa vào Dict
            d = {"Toan": parts[1].strip(),
                "Ly": parts[2].strip(), 
                "Hoa": parts[3].strip(), 
                "Sinh": parts[4].strip(), 
                "Van": parts[5].strip(), 
                "Anh": parts[6].strip(), 
                "Su": parts[7].strip(), 
                "Dia": parts[8].strip()
            }

            #Danh sach điểm Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia
            Diem_Toan_list = parts[1].strip().split(',')
            Diem_Ly_list = parts[2].strip().split(',')
            Diem_Hoa_list = parts[3].strip().split(',')
            Diem_Sinh_list = parts[4].strip().split(',')
            Diem_Van_list = parts[5].strip().split(',')
            Diem_Anh_list = parts[6].strip().split(',')
            Diem_Su_list = parts[7].strip().split(',')
            Diem_Dia_list = parts[8].strip().split(',')

            #Điểm trung bình các môn tự nhiên
            Diem_Toan_tb = round(((float(Diem_Toan_list[0])*0.05 + float(Diem_Toan_list[1])*0.1 + float(Diem_Toan_list[2])*0.15 + float(Diem_Toan_list[3])*0.7)),2)
            Diem_Ly_tb = round(((float(Diem_Ly_list[0])*0.05 + float(Diem_Ly_list[1])*0.1 + float(Diem_Ly_list[2])*0.15 + float(Diem_Ly_list[3])*0.7)),2)
            Diem_Hoa_tb = round(((float(Diem_Hoa_list[0])*0.05 + float(Diem_Hoa_list[1])*0.1 + float(Diem_Hoa_list[2])*0.15 + float(Diem_Hoa_list[3])*0.7)),2)
            Diem_Sinh_tb = round(((float(Diem_Sinh_list[0])*0.05 + float(Diem_Sinh_list[1])*0.1 + float(Diem_Sinh_list[2])*0.15 + float(Diem_Sinh_list[3])*0.7)),2)
        
            #Điểm trung bình các môn xã hội
            Diem_Anh_tb = round(((float(Diem_Anh_list[0])*0.05 + float(Diem_Anh_list[1])*0.1 + float(Diem_Anh_list[2])*0.1 + float(Diem_Anh_list[3])*0.15 + float(Diem_Anh_list[4])*0.6)),2)
            Diem_Van_tb = round(((float(Diem_Van_list[0])*0.05 + float(Diem_Van_list[1])*0.1 + float(Diem_Van_list[2])*0.1 + float(Diem_Van_list[3])*0.15 + float(Diem_Van_list[4])*0.6)),2)
            Diem_Su_tb = round(((float(Diem_Su_list[0])*0.05 + float(Diem_Su_list[1])*0.1 + float(Diem_Su_list[2])*0.1 + float(Diem_Su_list[3])*0.15 + float(Diem_Su_list[4])*0.6)),2)
            Diem_Dia_tb = round(((float(Diem_Dia_list[0])*0.05 + float(Diem_Dia_list[1])*0.1 + float(Diem_Dia_list[2])*0.1 + float(Diem_Dia_list[3])*0.15 + float(Diem_Dia_list[4])*0.6)),2)
        
            #Tạo Dict lưu điểm trung bình
            dict_diem_tb = {
                "Toan": Diem_Toan_tb,
                "Ly": Diem_Ly_tb,
                "Hoa": Diem_Hoa_tb,
                "Sinh": Diem_Sinh_tb,
                "Van": Diem_Van_tb,
                "Anh": Diem_Anh_tb,
                "Su": Diem_Su_tb,
                "Dia": Diem_Dia_tb
            }
            #Đưa vào cái Dict lớn với Key là Mã HS
            Dict_ten_diem[parts[0].strip()] = dict_diem_tb
    return Dict_ten_diem

#----Hàm lưu file----
def luudiem_trungbinh(Dict_ten_diem, duong_dan_output):
    with open (duong_dan_output, "w", encoding = "utf-8") as f:

        #Hàng đầu tiên của file “diem_trungbinh.txt” giữ nguyên như của “diem_chitiet.txt”
        f.write("Ma HS, Toan, Ly Hoa, Sinh, Van, Anh, Su, Dia\n")

        #Lưu các biến vào trong file này
        for ma_hs, diem_tb in Dict_ten_diem.items():
            line_data = (f"{ma_hs};{diem_tb['Toan']};{diem_tb['Ly']};{diem_tb['Hoa']};{diem_tb['Sinh']};{diem_tb['Van']};{diem_tb['Anh']};{diem_tb['Su']};{diem_tb['Dia']}\n")
            f.write (line_data)

#----Hàm Main----
def main():

    #Khai báo đường dẫn input
    input_file = "diem_chitiet.txt"
    #Khai báo đường dẫn output
    output_file = "diem_trungbinh.txt"
    #Chạy hàm tinhdiem_trungbinh
    bang_diem = tinhdiem_trungbinh(input_file)
    #Chạy hàm luudiem_trungbinh
    luudiem_trungbinh(bang_diem, output_file)


if __name__ == "__main__":
    main()







