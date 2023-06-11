    #1. Đọc dữ liệu từ file
with open('DoThi_NFA.txt','r') as file:
    DuLieu = file.readlines()
# a. Lưu lại số lượng đỉnh và số lượng cung
soDinh, soCung = map(int, DuLieu[0].split())
print("Số lượng đỉnh: {0} - Số lượng cung: {1}".format(soDinh,soCung))

# b. Tìm các giá trị trên cung rồi lưu vào bộ chữ cái và lưu đỉnh bắt đầu với đỉnh kết thúc và chuỗi đang xét nữa
boChuCai = []
for i in range(1,soCung+1):
    X,Y,W = map(int, DuLieu[i].split())
    #Kiểm tra giá trị có bên trong danh sách không .Nếu không có thì đẩy trọng số vào trong danh sách .Ngược lại thì không làm gì
    if W not in boChuCai:
        boChuCai.append(W)
print("Bộ chữ cái: {0}".format(boChuCai))
start,end = map(int, DuLieu[soCung+1].split())
chuoiXet = str(DuLieu[soCung+2])

tuDien = {}
# c. Tạo khóa cho từ điển với giá trị của khóa là 1 tuple mang 2 giá trị. Trong đó giá trị thứ nhất là đỉnh giá trị thứ 2 là 1 trong những phần tử trong danh sách bộ chữ cái
for i in range(soDinh): #Các số đỉnh đã tồn tại
    for j in boChuCai:  #Các giá trị trong bộ chữ cái
        tuDien[(i,j)] = []

# d. Thêm giá trị vào phần tử giá trị được thêm vào là đỉnh có cung nối với đỉnh đang xét
for i in range(1,soCung+1):
    X,Y,W = map(int, DuLieu[i].split())
    tuDien[(X,W)].append(Y)
# e. Hiển thị bảng như sau:
print("Đỉnh bắt đầu: {0} - Đỉnh kết thúc {1}".format(start,end))
print("\t --- Bảng: ---")
for khoa,giatri in tuDien.items():
    print("Khóa: {0}\t-\tGiá trị: {1}".format(khoa,giatri))
print("Chuỗi cần xét: {0}".format(chuoiXet))

    #2. Xây dụng 1 số hàm như sau
#1. Trả về danh sách các đỉnh kể có giá trị V nào đó
def TraVeDinhKeCoGiaTri(tudien,dinhX,trongSo):
    return list(tudien[(dinhX,trongSo)])

#2. Hàm chuyển
def hamChuyen(tudien,start,end,chuoiXet):
    #0. Xác định số lần lặp
    lanLap = int(1)
    #1. Tạo danh sách
    temp =[]    #Đây là danh sách lưu trữ dữ liệu tạm thời
    DS = []     #Đây là danh sách trả về sau khi xét đến ký tự cuối cùng của chuỗi
    #2. Đẩy đỉnh bắt đầu vào DS
    DS.append(start)
    #3. Vòng lặp dựa trên từ ký tự của chuỗi xét
    for i in  chuoiXet:
        #Vòng lặp thứ 2 dùng để lấy từ phần tử trong temp để xét với ký tự được lấy ra
        for j in DS:
            temp.extend(list(TraVeDinhKeCoGiaTri(tudien,j,int(i))))    #Lưu trữ đỉnh kề thứ j có trọng số thứ i
        #Đặt lại
        DS = temp[:]    #Cho danh sách DS sao chép danh sách temp hiện tại
        print(DS)
        temp.clear()    #Làm rỗng danh sách temp để tiếp tục cho lần lặp kế tiếp
        
        #Điều kiện dừng vòng lặp đúng: Nếu đỉnh kết thúc(end) nằm trong danh sách DS thì trả về 1
        if end in DS:
            print("Do {0} thuộc F nên {1} thuộc L(M).".format(end,chuoiXet))
            return 1
    #Điều kiện dừng vòng lặp sai: Nếu xét từng ký tự đến cuỗi chuỗi rồi mà không tìm được đỉnh cuối cùng trong danh sách DS thì trả về 0
    print("Do không tìm được đỉnh kết thúc mà đến cuỗi chuỗi rồi. Vậy nên {0} không thuộc L(M).".format(chuoiXet))
    return 0

hamChuyen(tuDien,start,end,chuoiXet)