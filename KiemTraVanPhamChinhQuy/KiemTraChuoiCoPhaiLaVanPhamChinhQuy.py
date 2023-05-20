import re

#--------------------------Kiêm tra chuổi có thuộc văn phạm chính quy không-----------------------
    #Đọc dữ liệu từ file văn phạm chính quy và đọc chuỗi đầu vào có thỏa văn phạm chính quy trên không
teptin = open('grammar.txt','r')
DoanVB = teptin.read()                          #Biến này dùng để lưu nguyên văn bản từ tệp tin grammar.txt

mangCuaDoanVB = [i for i in DoanVB.split('\n')] #Mảng này lưu trữ các phần tử dựa trên việc tách nội dung dựa trên dấu xuống dòng trong biến DoanVB
tapLuatSinh = []                                #Đây là 1 danh sách tập các luật sinh nhận từ tệp tin grammar.txt
chuoiDauVao = str()                             #Đây là chuỗi đầu vào nhận từ tệp tin grammar.txt
        #Vòng lặp để lưu từng luật sinh vào biến tapLuatSinh
for i in range(0,len(mangCuaDoanVB)):
    if mangCuaDoanVB[i] == '---':
        chuoiDauVao = mangCuaDoanVB[i+1]
        break
    tapLuatSinh.append(mangCuaDoanVB[i])
    #Ham kiem tra tập luật sinh là văn phạm tuyến tính trái hay là tuyến tính phải.Hàm này sẽ trả về giá trị 1, 2 và 0 (1: là văn phạm tuyến tính trái; 2: là văn phạm tuyến tính phải; 0: không phải là văn phạm chính quy)
def KiemTraVanPhamChinhQuy(G):
    #Biến này dùng để đếm số chữ hoa bên trái    
    demTrai = int(0)
    #Biến này dùng để đếm số chữ hoa bên phải 
    demPhai = int(0) 
    #Biến này dùng để đếm số chữ thường bên vế phải
    demBinhThuong = int(0)
    #Biến này dùng để đếm số chữ thường bên vế phải
    demChuHoa = int(0)
    
    #1.Vòng lặp kiểm tra tập luật sinh
    for i in G:
        chuoiSauMuiTen = r'->(.+)'
        vePhai = re.search(chuoiSauMuiTen,i)
        #print(vePhai.group(1))
        #DK1: kiểm tra xem 1 chuỗi xem có chữ in hoa ở giữa các chữ cái thường không (Kiểm tra xem có biến xuất hiện ở giữa các ký hiệu kết thúc không)
        if re.match(r'^[a-z0-9\.\,\!\?\$]+[A-Z]+[a-z0-9\.\,\!\?\$]+$',vePhai.group(1)):
            return 0
        #DK2: Kiểm tra chuỗi đang xét có phải là 1 chuỗi các chữ cái thường không
        if re.match(r'^[a-z\.\,\!\?\$]*$',vePhai.group(1)):
            demBinhThuong+=1
        #DK: kiểm tra nếu trong luật sinh nào đó xuất hiện toàn là chữ cái hoa hay khôg
        if re.match(r'^[A-Z]*$',vePhai.group(1)):
            demChuHoa+=1
        #DK3: kiêm tra 1 chuỗi có thõa điều kiện là các chữ cái thường nằm bên trái , còn các chữ cái in hoa nằm bên phải(tuyến tính phải)
        if re.match(r'^[a-z0-9\.\,\!\?\$]+[A-Z]+$',vePhai.group(1)):
            demPhai+=1
        #DK4: kiêm tra 1 chuỗi có thõa điều kiện là các chữ cái in hoa nằm bên trái , còn các chữ cái thường nằm bên phải(tuyến tính trái)
        if re.match(r'^[A-Z]+[a-z0-9\.\,\!\?\$]+$',vePhai.group(1)):
            demTrai+=1
    #2. Giờ kiểm tra xem có phải là văn phạm chính quy không (Nếu là văn phạm chính quy thì nó tuyến tính trá hay tuyến tính phải)
    if demPhai == 0 and demTrai == 0 and demBinhThuong >0:
            return 0
    #Nếu mà tập các luật sinh mà có luật sinh tuyến tính trái và cũng có luật sinh tuyến tính phải -> không phải là văn phạm chính quy
    else:
        if demPhai > 0 and demTrai > 0:
            return 0
    #Nếu trên tập luật sinh mà toàn có biến mà không có ký tụ kết thúc thì đó không phải là văn phạm chính quy
        else:
            if demChuHoa>0 and demBinhThuong == 0 and demPhai == 0 and demTrai == 0:
                return 0
    #Nếu tập luật sinh mà có chữ cái hoa xuất hiện bên phải và cũng có thể có luật sinh thuộc chữ cái thường -> Văn phạm chính quy
            else:
                if demTrai == 0 and demBinhThuong >=0 and demPhai > 0:
                    return 2
    #Nếu tập luật sinh mà có chữ cái hoa xuất hiện bên trái và cũng có thể có luật sinh thuộc chữ cái thường -> Văn phạm chính quy
                else:
                    if demTrai > 0 and demBinhThuong >=0 and demPhai == 0:
                        return 1

KQkiemTra = KiemTraVanPhamChinhQuy(tapLuatSinh)
    #Hàm thứ 2 dùng để kiểm tra chuỗi đầu vào
def KiemTraChuoiDauVao(TapLuatSinh,ChuoiDauVao,KQkiemTra):
    #Nếu kết quả kiểm tra mang giá trị là 0 thì không thực hiện
    if KQkiemTra == 0:
        print("Không phải là văn phạm chính quy")
        return      #Văn phạm trên không phải là văn phạm chính quy
    else:
        print("Ta có văn phạm chính quy như sau: {0}".format(TapLuatSinh))
        print("Xét chuỗi đầu vào: {0}".format(ChuoiDauVao))
        #Nếu đây là văn phạm tuyến tính phải thì ta kiểm tra chuỗi theo cách 1
        if KQkiemTra == 2:                              
            luatSinh = r'([a-z0-9\.\,\!\?\$]+)([A-Z]*)' #Biểu thức chính quy này nhằm dùng để tách chuỗi ra theo ký tự kết thúc nằm ở bên trái và các biến ở bên phải
            #Vòng lặp chính không biết lặp bao nhiêu lần
            while True:
                ketQuaSoSanh = int(0)
                #1.Vòng lặp này dùng để so sách chuỗi ký tự kết thúc và chuỗi đầu vào. Thực hiện như sau
                for i in TapLuatSinh:
                    kyTuKetThuc = re.search(luatSinh, i)
                    if kyTuKetThuc:
                        ChuoiKT = kyTuKetThuc.group(1) #Biến ChuoiKT này dùng để nhận các ký hiệu kết thúc của luật sinh
                #Ta thực hiện so sánh chuỗi ký tự kết thúc với chuỗi đầu vào dựa trên độ dài.(Nếu khớp thì đặt biến ketQuaSoSanh = 1)
                        if ChuoiKT == ChuoiDauVao[0:len(ChuoiKT)]:
                            ketQuaSoSanh = int(1)
                            ChuoiDauVao = ChuoiDauVao[len(ChuoiKT):]    #Cắt chuỗi đầu vào
                            break               #Dừng để lặp tiếp theo trong vòng lặp tập luật sinh
                #Nếu sau khi so sánh mà biến ChuoiDauVao có kích cỡ là 0 thì trả về 1
                if len(ChuoiDauVao) == 0:
                    print("=> Chuỗi này hợp lệ với văn phạm chính quy")
                    break
                #Nếu sau khi thực hiện mà kết quả so sánh vẫn = 0 thì ngưng vòng lặp. Vì chuỗi đầu vào không hợp lệ với văn phạm chính quy
                if ketQuaSoSanh == 0:
                    print("=> Chuỗi này không hợp lệ với văn phạm chính quy")
                    break
        else: 
            #Nếu đây là văn phạm tuyến tính trái thì ta kiểm tra chuỗi theo cách 2
            if KQkiemTra == 1:                              
                luatSinh = r'([A-Z]+)([a-z0-9\.\,\!\?\$]*)' #Biểu thức chính quy này nhằm dùng để tách chuỗi ra theo ký tự kết thúc nằm ở bên trái và các biến ở bên phải
                #Vòng lặp chính không biết lặp bao nhiêu lần
                while True:
                    ketQuaSoSanh = int(0)
                    #1.Vòng lặp này dùng để so sách chuỗi ký tự kết thúc và chuỗi đầu vào. Thực hiện như sau
                    for i in TapLuatSinh:
                        kyTuKetThuc = re.search(luatSinh, i)
                        if kyTuKetThuc:
                            ChuoiKT = kyTuKetThuc.group(2) #Biến ChuoiKT này dùng để nhận các ký hiệu kết thúc của luật sinh
                            #Ta thực hiện so sánh chuỗi ký tự kết thúc với chuỗi đầu vào dựa trên độ dài.(Nếu khớp thì đặt biến ketQuaSoSanh = 1)
                            if ChuoiKT == ChuoiDauVao[0:len(ChuoiKT)]:
                                ketQuaSoSanh = int(1)
                                ChuoiDauVao = ChuoiDauVao[len(ChuoiKT):]    #Cắt chuỗi đầu vào
                                break               #Dừng để lặp tiếp theo trong vòng lặp tập luật sinh
                    #Nếu sau khi so sánh mà biến ChuoiDauVao có kích cỡ là 0 thì trả về 1
                    if len(ChuoiDauVao) == 0:
                        print("=> Chuỗi này hợp lệ với văn phạm chính quy")
                        break
                    #Nếu sau khi thực hiện mà kết quả so sánh vẫn = 0 thì ngưng vòng lặp. Vì chuỗi đầu vào không hợp lệ với văn phạm chính quy
                    if ketQuaSoSanh == 0:
                        print("=> Chuỗi này không hợp lệ với văn phạm chính quy")
                        break

KiemTraChuoiDauVao(tapLuatSinh,chuoiDauVao,KQkiemTra)