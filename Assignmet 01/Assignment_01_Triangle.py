import math
#Hàm tính khoảng cách, làm tròn đến 2 chữ số
def khoangcach(Ax,Ay,Bx,By):
    distance = math.sqrt((Ax - Bx)**2 + (Ay - By)**2)
    return round(distance,2)

#Hàm tính khoảng cách không làm tròn
def khoangcach_kt(Ax,Ay,Bx,By):
    distance = math.sqrt((Ax - Bx)**2 + (Ay - By)**2)
    return distance

#Hàm kiểm tra xem 03 điểm này có tạo thành được một tam giác hay không
def kiemtra_tamgiac(Ax, Ay, Bx, By, Cx, Cy):
    if khoangcach(Ax,Ay,Bx,By) + khoangcach(Bx,By,Cx,Cy) > khoangcach(Ax,Ay,Cx,Cy) and khoangcach(Bx,By,Cx,Cy) + khoangcach(Ax,Ay,Cx,Cy) > khoangcach(Ax,Ay,Bx,By) and khoangcach(Ax,Ay,Cx,Cy) + khoangcach(Ax,Ay,Bx,By) > khoangcach(Bx,By,Cx,Cy):
        return True
    else:
        return False

#Hàm này để tính độ của các góc trong một tam giác
def goc(Ax, Ay, Bx, By, Cx, Cy):
    #Tính góc ABC
    v_BAx, v_BAy = Ax - Bx, Ay - By
    v_BCx, v_BCy = Cx - Bx, Cy - By
    tu_ABC = (v_BAx * v_BCx) + (v_BAy * v_BCy)
    mau_ABC = khoangcach_kt(Ax,Ay,Bx,By) * khoangcach_kt(Bx,By,Cx,Cy)
    ABC = round(math.degrees(math.acos(max(min(tu_ABC / mau_ABC, 1), -1))), 2)

    #Tính góc BCA
    v_CBx, v_CBy = Bx - Cx, By - Cy
    v_CAx, v_CAy = Ax - Cx, Ay - Cy
    tu_BCA = (v_CBx * v_CAx) + (v_CBy * v_CAy)
    mau_BCA = khoangcach_kt(Cx,Cy,Bx,By) * khoangcach_kt(Cx,Cy,Ax,Ay)
    BCA = round(math.degrees(math.acos(max(min(tu_BCA / mau_BCA, 1), -1))), 2)

    #Tính góc BAC
    v_ACx, v_ACy = Cx - Ax, Cy - Ay
    v_ABx, v_ABy = Bx - Ax, By - Ay
    tu_BAC = (v_ACx * v_ABx) + (v_ACy * v_ABy) 
    mau_BAC = khoangcach_kt(Ax,Ay,Cx,Cy) * khoangcach_kt(Ax,Ay,Bx,By)
    BAC = round(math.degrees(math.acos(max(min(tu_BAC / mau_BAC, 1), -1))), 2)
    return ABC, BCA, BAC



#Xét loại của tam giác ABC

def loai_tamgiac(Ax,Ay,Bx,By,Cx,Cy):

    #Khai báo biến để dùng trong hàm này
    ABC, BCA, BAC = goc(Ax, Ay, Bx, By, Cx, Cy)
    AB = khoangcach(Ax,Ay,Bx,By)
    BC = khoangcach(Bx,By,Cx,Cy)
    AC = khoangcach(Ax,Ay,Cx,Cy)

    #Xác định các loại tam giác

    if AB == AC and AB == BC: return "Tam giác đều"
    if ABC > 90.0 and AB == BC: return "Tam giác tù và cân tại đỉnh B"
    if BCA > 90.0 and BC == AC: return "Tam giác tù và cân tại đỉnh C"
    if BAC > 90.0 and AB == AC: return "Tam giác tù và cân tại đỉnh A"
    if ABC == 90.0 and AB == BC: return "Tam giác vuông cân tại đỉnh B"
    if BCA == 90.0 and BC == AC: return "Tam giác vuông cân tại đỉnh C"
    if BAC == 90.0 and AB == AC: return "Tam giác vuông cân tại đỉnh A"
    if ABC == 90.0: return "Tam giác vuông tại đỉnh B"
    if BCA == 90.0: return "Tam giác vuông tại đỉnh C"
    if BAC == 90.0: return "Tam giác vuông tại đỉnh A"
    if AB == BC: return "Tam giác cân tại đỉnh B"
    if BC == AC: return "Tam giác cân tại đỉnh C"
    if AB == AC: return "Tam giác cân tại đỉnh A"
    if ABC > 90.0: return "Tam giác tù tại đỉnh B"
    if BCA > 90.0: return "Tam giác tù tại đỉnh C"
    if BAC > 90.0: return "Tam giác tù tại đỉnh A"
    return "Tam giác thường"

#Tính diện tích tam giác
def dientich_tamgiac(Ax,Ay,Bx,By,Cx,Cy):
    dien_tich = 0.5 * abs(Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))
    return round(dien_tich,2)


#Tính độ dài đường cao của tam giác
def duongcao_tamgiac(Ax,Ay,Bx,By,Cx,Cy):
    AB = khoangcach(Ax,Ay,Bx,By)
    BC = khoangcach(Bx,By,Cx,Cy)
    AC = khoangcach(Ax,Ay,Cx,Cy)
    p = (AB + BC + AC)/2
    Ha = 2 * (math.sqrt(p * (p - AB) * (p - BC) * (p - AC)))/BC
    Hb = 2 * (math.sqrt(p * (p - AB) * (p - BC) * (p - AC)))/AC
    Hc = 2 * (math.sqrt(p * (p - AB) * (p - BC) * (p - AC)))/AB
    return round(Ha,2), round(Hb,2), round(Hc,2)


#Tính đường trung tuyến của một tam giác
def trungtuyen_tamgiac(Ax,Ay,Bx,By,Cx,Cy):
    AB = khoangcach(Ax,Ay,Bx,By)
    BC = khoangcach(Bx,By,Cx,Cy)
    AC = khoangcach(Ax,Ay,Cx,Cy)
    Ma = math.sqrt((AB**2 + AC **2 - 0.5 * BC **2)/2)
    Mb = math.sqrt((BC**2 + AB **2 - 0.5 * AC **2)/2)
    Mc = math.sqrt((BC**2 + AC **2 - 0.5 * AB **2)/2)
    return round(Ma,2), round(Mb,2), round(Mc,2)

#Tìm toạ độ trọng tâm của tam giác
def trongtam_tamgiac(Ax,Ay,Bx,By,Cx,Cy):
    Gx = (Ax + Bx + Cx)/3
    Gy = (Ay + By + Cy)/3
    return round(Gx,2), round(Gy,2)

#Tìm toạ độ trực tâm của tam giác
def tructam_tamgiac(Ax,Ay,Bx,By,Cx,Cy):
    c = Bx - Cx
    d = By - Cy
    e = Ax - Cx
    f = Ay - Cy
    a = Ax * c + Ay * d
    b = Bx * e + By * f
    Hy = (a * e - b * c)/(e * d - f * c) + 0.0
    Hx = (f * a - d * b)/(c * f - e * d) + 0.0
    return round(Hx,2), round(Hy,2)


def main():
    print("PYB101x - Assignment 01")


    #Nhập tọa độ 3 điểm từ bàn phím
    du_lieu = input("Nhập tọa độ [Ax, Ay, Bx, By, Cx, Cy]:")
    danh_sach_toa_do = du_lieu.split(",")

    #Kiểm tra xem nhập đủ 6 số không
    if len(danh_sach_toa_do)!= 6:
        print("!Bạn phải nhập đủ 6 số nguyên!")
        return

    #Kiểm tra xem dù có đủ 6 kí tự nhưng mà phải số không, gán số cho các kí tự
    try:
        toa_do = [int(x.strip()) for x in danh_sach_toa_do]
        Ax, Ay, Bx, By, Cx, Cy = toa_do
    except:
        print("Bạn nhập kí tự sai, vui lòng chỉ nhập số")
        return

    #In ra màn hình độ dài các cạnh
    AB = khoangcach(Ax,Ay,Bx,By)
    BC = khoangcach(Bx,By,Cx,Cy)
    AC = khoangcach(Ax,Ay,Cx,Cy)
    print("Độ dài cạnh AB =", AB , "cm")
    print("Độ dài cạnh BC =", BC , "cm")
    print("Độ dài cạnh AC =", AC , "cm")
    
    #Kiểm tra xem có phải là một tam giá không
    if kiemtra_tamgiac (Ax, Ay, Bx, By, Cx, Cy):
        print("A, B, C là một tam giác")
    else:
        print("A, B, C không phải là một tam giác")
        return

    #In ra màn hình số độ
    ABC, BCA, BAC = goc(Ax, Ay, Bx, By, Cx, Cy)

    print ("Góc BAC = ", BAC, "(độ)")
    print ("Góc ABC = ", ABC, "(độ)")
    print ("Góc BCA = ", BCA, "(độ)")

    #In ra màn hình loại tam giác
    print("Loại của tam giác ABC:", loai_tamgiac(Ax,Ay,Bx,By,Cx,Cy))

    #In ra màn hình diện tích tam giác
    dien_tich = dientich_tamgiac(Ax,Ay,Bx,By,Cx,Cy)
    print("Diện tích của tam giác =" , dien_tich)


    #In ra màn hình độ dài đường cao
    Ha, Hb, Hc = duongcao_tamgiac(Ax,Ay,Bx,By,Cx,Cy)
    print ("Độ dài đường cao từ điểm A = ", Ha)
    print ("Độ dài đường cao từ điểm B = ", Hb)
    print ("Độ dài đường cao từ điểm C = ", Hc)


    #In ra màn hình độ dài đường trung tuyến
    Ma, Mb, Mc = trungtuyen_tamgiac(Ax,Ay,Bx,By,Cx,Cy)
    print ("Độ dài trung tuyến từ điểm A = ", Ma)
    print ("Độ dài trung tuyến từ điểm B = ", Mb)
    print ("Độ dài trung tuyến từ điểm C = ", Mc)

    #In ra màn hình toạ độ trọng tâm
    Gx, Gy = trongtam_tamgiac(Ax,Ay,Bx,By,Cx,Cy)
    print("Tọa độ trọng tâm của tam giác ABC: x = ", Gx , "y =", Gy)

    #In ra màn hình toạ độ trực tâm
    Hx, Hy = tructam_tamgiac(Ax,Ay,Bx,By,Cx,Cy)
    print("Tọa độ trực tâm của tam giác ABC: x = ", Hx , "y =", Hy)


if __name__ == "__main__":
    main()

