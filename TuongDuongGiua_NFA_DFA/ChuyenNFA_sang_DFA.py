import itertools as itt
import copy
    #1.Đọc dữ liệu từ file
with open('data_NFA.txt','r') as File:
    Data_NFA = File.readlines()

    #2.Khai báo biến và danh sách
Q = []                              #Tập các trạng thái
BCC = []                            #Tập các chữ cái
hamChuyen = {}                      #Hàm chuyển
start = str()                       #Trạng thái bắt đầu
end = []                         #Trạng thái kết thúc

    #3.Truyền dữ liệu từ file vào từng biến và từ điển
#3.1 Lưu các tập trạng thái
for i in Data_NFA[0]:
    Q.extend( list(map(str,i.split())) )

#3.2 Lưu bộ chữ cái
for i in Data_NFA[1]:
    BCC.extend( list(map(str,i.split())) )

#3.3 Lưu trạng thái đầu
start = str( list( map(str,Data_NFA[2].split() ))[0] )

#3.4 Lưu trạng thái kết thúc
end = list( map(str,Data_NFA[3].split() ))[0]

#3.5 Tạo các giá trị của từ điển là kiểu danh sách, còn khóa là kiểu tupple
for i in Data_NFA[4:]:
    X,W,Y = map(str,i.split())
    hamChuyen[(X,W)]= []

#3.6 Lưu dữ liệu vào từ điển
for i in Data_NFA[4:]:
    X,W,Y = map(str,i.split())
    #print("X:{0} - Y:{1} - W:{2}".format(X,Y,W))
    hamChuyen[(X,W)].append(Y)
    #4.Tạo lớp NFA
class NFA(object):
    def __init__(self,TapTrangThai,BoChuCai,HamChuyen,stat,end):
        self.TapTrangThai = TapTrangThai
        self.BoChuCai = BoChuCai
        self.HamChuyen = HamChuyen
        self.stat = stat
        self.end = end
    def InDuLieu(sefl):
        print("\n\t---Thông tin NFA:---")
        print("Tập các trạng thái: ",sefl.TapTrangThai)
        print("Bộ chữ cái: ",sefl.BoChuCai)
        print("Hàm chuyển: \n")
        Keys = list(sefl.HamChuyen.keys())
        Values = list(sefl.HamChuyen.values())
        for i in range(len(sefl.HamChuyen)):
            print("{0} - {1}".format(Keys[i],Values[i]))
        print("Trạng thái bắt đầu: ",sefl.stat)
        print("Trạng thái kết thúc: ",sefl.end)

    #5.Tạo lớp DFA
class DFA(object):
    def __init__(self,TapTrangThai,BoChuCai,HamChuyen,stat,end):
        self.TapTrangThai = TapTrangThai
        self.BoChuCai = BoChuCai
        self.HamChuyen = HamChuyen
        self.stat = stat
        self.end = end
    def __init__(self) :
        print("Không có đối số")
    def InDuLieu(sefl):
        print("\n\t---Thông tin DFA:---")
        print("Tập các trạng thái: ",sefl.TapTrangThai)
        print("Bộ chữ cái: ",sefl.BoChuCai)
        print("Hàm chuyển: \n")
        Keys = list(sefl.HamChuyen.keys())
        Values = list(sefl.HamChuyen.values())
        for i in range(len(sefl.HamChuyen)):
            print("{0} - {1}".format(Keys[i],Values[i]))
        print("Trạng thái bắt đầu: ",sefl.stat)
        print("Trạng thái kết thúc: ",sefl.end)
    #Phương thức xây dựng sao chép
    def __copy__(sefl):
        new_DFA = (sefl.TapTrangThai,sefl.BoChuCai,sefl.end,sefl.stat,sefl.HamChuyen)
        return new_DFA

#Tạo đối tượng NFA và gán giá trị
NFA1 = NFA(Q,BCC,hamChuyen,start,end)
NFA1.InDuLieu()
DFA1 = DFA()

#Hàm chuyển NFA sang DFA
def chuyen_NFA_sang_DFA(NFAx,DFAx):
    Qphay = []
#1.Chuyển Bộ chữ cái của NFA sang DFA
    dem = int(1)
    for i in range(len(NFAx.TapTrangThai)**2):
        Qphay.extend(list(itt.combinations(NFAx.TapTrangThai,dem)))
        dem+=1
    
#2. Nếu trong tập trạng thái của DFA mà có lưu 1 trạng thái kết thúc từ NFA thì đẩy trạng thái đó vào trạng thái kết thúc của DFA
    Fphay = []
    for i in Qphay:
        if NFAx.end in i:
            Fphay.append(i)
    
#3.Biến hàm chuyển của DFA với độ dài là số lượng phần tử trong bộ chữ cái của DFA * số lượng bộ chữ cái của NFA
    hamChuyenDFA = {}
    for i in Qphay:
        for j in NFAx.BoChuCai:
            hamChuyenDFA[(i,j)]=[]
#4.Lưu phần tử vào giá trị có kiển là danh sách của từ điển hamChuyenDFA
    #---Lặp 1: trên từng trạng thái của DFA
    for i in Qphay:
        #---Lặp 2: trên từng giá trị của bộ chữ cái của NFA
        for j in NFAx.BoChuCai:
            #print("\t\n Xét trạng thái ",i,' trên chữ cái',j)
            #print(">>Kết quả của hàm chuyển NFA trên")
            #---Lặp 3: Trên từng phần tử của trạng thái
            for K1 in i:
                #print('---Từng trạng thái:',K1)
                #---Lặp 4: trên từng phần tử có kiểu danh sách trong hàm chuyển của NFA 
                ##print(NFAx.HamChuyen[(K1,j)]) 
                for K2 in NFAx.HamChuyen[(K1,j)]:
                    if K2 not in hamChuyenDFA[(i,j)]:
                        hamChuyenDFA[(i,j)].append(K2)
    
#5. lưu Q',end', start của NFA, bộ chữ cái của NFA và hàm chuyển mới tính vào DFA
    DFAx.TapTrangThai = Qphay
    DFAx.end = Fphay
    DFAx.HamChuyen = hamChuyenDFA
    DFAx.BoChuCai = NFAx.BoChuCai
    DFAx.stat = NFAx.stat
    #Hiển thị kết quả
chuyen_NFA_sang_DFA(NFA1,DFA1)

DFA1.InDuLieu()