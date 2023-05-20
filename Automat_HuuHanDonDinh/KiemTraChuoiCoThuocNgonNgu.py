    # 1. Một số hàm về ma trận
#a. làm rỗng ma trận

def makeNullMatrix(maTran,slDinh):
    for i in range(slDinh):
        for j in range(slDinh):
            maTran[i][j] = -1

#b. Thêm cung vào ma trận

def addEdge(maTran,X,Y,W):
    maTran[X][Y] = W

#c. In ma Trận

def PrintMatrix(maTran,slDinh):
    for i in range(slDinh):
        for j in range(slDinh):
            print(maTran[i][j],end=' ')
        print()

#d.  Tìm đỉnh có trọng số với đỉnh đang xét

def TraVeDinhCoTrongSoVoiDinh(maTran,soDinh,dinhXet,W):
    for i in range(soDinh):
        if maTran[dinhXet][i] == W:
            return i    #Tìm thấy đỉnh xét cùng
    return -1 #Không tìm thấy đỉnh xét cùng

    #2. Đọc dữ liệu từ file
with open('DoThiThuNhat.txt','r') as file:
    DuLieu = file.readlines()
# a. Lưu lại số lượng đỉnh và số lượng cung
soDinh, soCung = map(int, DuLieu[0].split())
print("Số lượng đỉnh: {0} - Số lượng cung: {1}".format(soDinh,soCung))
# b. Tạo ma trận đỉnh - đỉnh
maTran = [[j for j in range(soDinh)] for i in range(soDinh)]
# c. làm rỗng ma trận cái
makeNullMatrix(maTran,soDinh)
# d. Đọc từng cung r lưu vào ma trân
for i in range(1,soCung+1):
    U,V,W = map(int, DuLieu[i].split())
    addEdge(maTran,U,V,W)
#e. Đọc Đỉnh bắt đầu và đỉnh kết thúc
start, end = map(int , DuLieu[soCung+1].split())
print("đỉnh bắt đầu : {0} - đỉnh kết thúc: {1}".format(start,end))
chuoiXet = str(DuLieu[soCung+2])    #đây là 1 chuỗi để xét
print("Xét chuỗi có thuộc ngôn ngữ không : {0}".format(chuoiXet))

#3. Tạo hàm chuyển để xét đỉnh bắt đầu so với chuỗi sẽ trả về kết quả đỉnh cuối là gì
def hamChuyen(dinh,chuoi):
    temp = dinh
    for i in chuoi:
        temp = TraVeDinhCoTrongSoVoiDinh(maTran,soDinh,temp,int(i))
    return temp

#Cuối cùng: Kiểm tra xem nếu hàm chuyển trả về end thì chuỗi này thuộc L(M)
if hamChuyen(start,chuoiXet) == end:
    print("{0} có thuộc L(M).".format(chuoiXet))
else:
    print("{0} không thuộc L(M).".format(chuoiXet))