import re

    # --- Buoc 1: Doc luu lieu tu file ---

#Luu du lieu tu file
File = open('luatSinh.txt','r')
text = File.read() #Luu du lieu vao text
    # --- Buoc 2: Biến đổi dữ liệu và lưu vào mảng 2 chiều --- 

#Tao 1 danh sach 1 chiều dùng để lưu các phần tử dựa trên việc tách dấu xuống hàng
rules = [ i for i in text.split('\n')]
#Tao 1 danh sách 2 chiều
danhSach = [[]]
dem = 0
for i in rules:
    if i == '---': #Nếu mà gặp chuỗi '---' thì ta tạo 1 hàng mới cho mảng 2 chiều
        danhSach.append([])#Tạo 1 hàng mới
        dem+=1
    else:
        danhSach[dem].append(i) #Ngược lại ta thêm các chuỗi không phải là chuỗi '---' vào danh sách
    # --- Bước 3 kiểm tra văn phạm chính quy --- 
#Biến này dùng để đếm số chữ hoa bên trái    
demTrai = int(0)
#Biến này dùng để đếm số chữ hoa bên phải 
demPhai = int(0) 
#Biến này dùng để đếm số chữ thường bên vế phải
demBinhThuong = int(0)
#Biến này dùng để đếm số chữ thường bên vế phải
demChuHoa = int(0)
#Biến này dùng để lưu những luật sinh mà có biến xuất hiện ở giữa các ký tự kết thúc
Loi = int(0)
for i in danhSach:
    print(i)
    for j in i:
        chuoiDungSauMuiTen = r'->(.+)'      #Biêu thức chính quy này chỉ lấy những chuỗi đằg sau "->"
        ChuoiKQ = re.search(chuoiDungSauMuiTen,j)
        #DK1: kiểm tra xem 1 chuỗi xem có chữ in hoa ở giữa các chữ cái thường không (Kiểm tra xem có biến xuất hiện ở giữa các ký hiệu kết thúc không)
        if re.match(r'^[a-z0-9\.\,\!\?\$]+[A-Z]+[a-z0-9\.\,\!\?\$]+$',ChuoiKQ.group(1)):
            Loi+=1
        #DK2: Kiểm tra chuỗi đang xét có phải là 1 chuỗi các chữ cái thường không
        if re.match(r'^[a-z\.\,\!\?\$]*$',ChuoiKQ.group(1)):
            demBinhThuong+=1
        #DK: kiểm tra nếu trong luật sinh nào đó xuất hiện toàn là chữ cái hoa hay khôg
        if re.match(r'^[A-Z]*$',ChuoiKQ.group(1)):
            demChuHoa+=1
        #DK3: kiêm tra 1 chuỗi có thõa điều kiện là các chữ cái thường nằm bên trái , còn các chữ cái in hoa nằm bên phải(tuyến tính phải)
        if re.match(r'^[a-z0-9\.\,\!\?\$]+[A-Z]+$',ChuoiKQ.group(1)):
            demPhai+=1
        #DK4: kiêm tra 1 chuỗi có thõa điều kiện là các chữ cái in hoa nằm bên trái , còn các chữ cái thường nằm bên phải(tuyến tính trái)
        if re.match(r'^[A-Z]+[a-z0-9\.\,\!\?\$]+$',ChuoiKQ.group(1)):
            demTrai+=1

    #------------Kiểm tra văn phạm chính quy ------------------
    #Nếu mà lỗi > 0. Tức là xuất hiện chữ cái hoa ở giữa trong muôn vàng chữa cái thường -> không phải là văn phạm chính quy
    if Loi != 0:
        print("\n\tVăn phạm trên không phải là văn phạm chính quy\n")
    #Nếu mà toàn bộ luật sinh mà toàn là chữ cái thường mà không có chữ in hoa nào hết thì -> không phải là văn phạm chính quy
    else:
        if demPhai == 0 and demTrai == 0 and demBinhThuong >0:
            print("\n\tVăn phạm trên không phải là văn phạm chính quy\n")
    #Nếu mà tập các luật sinh mà có luật sinh tuyến tính trái và cũng có luật sinh tuyến tính phải -> không phải là văn phạm chính quy
        else:
            if demPhai > 0 and demTrai > 0:
                print("\n\tVăn phạm trên không phải là văn phạm chính quy\n")
    #Nếu trên tập luật sinh mà toàn có biến mà không có ký tụ kết thúc thì đó không phải là văn phạm chính quy
            else:
                if demChuHoa>0 and demBinhThuong == 0 and demPhai == 0 and demTrai == 0:
                    print("\n\tVăn phạm trên không phải là văn phạm chính quy\n")
    #Nếu tập luật sinh mà có chữ cái hoa xuất hiện bên phải và cũng có thể có luật sinh thuộc chữ cái thường -> Văn phạm chính quy
                else:
                    if Loi == 0 and demTrai == 0 and demBinhThuong >=0 and demPhai > 0:
                        print("\n\tVăn phạm trên là văn phạm chính quy")
                        print("---Văn phạm tuyến tính phải---\n")
    #Nếu tập luật sinh mà có chữ cái hoa xuất hiện bên trái và cũng có thể có luật sinh thuộc chữ cái thường -> Văn phạm chính quy
                    else:
                        if Loi == 0 and demTrai > 0 and demBinhThuong >=0 and demPhai == 0:
                            print("\n\tVăn phạm trên là văn phạm chính quy")
                            print("---Văn phạm tuyến tính trái---\n")
    #Đặt lại
    demTrai = demPhai = demBinhThuong = demChuHoa = Loi = int(0)