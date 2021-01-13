#welcome to chương trình phòng vệ toàn cầu.
aliens= 2
password = "nguyenthao"

print("Nhanh lên! Người ngoài hành tinh đang xâm chiếm đấy!")
print("Bạn cần bật hệ thống phòng vệ toàn cầu lên ngay!")
print("Hy vọng bạn biết mật khẩu, vì tương lai Trái Đất...")
print()
print(".....................................................")
print("    CHÀO MỪNG TỚI HỆ THỐNG PHÒNG VỆ TOÀN CẦU      ")
print("-----------------------------------------------------")
print()

guess = input("Xin hãy điền mật khẩu:".upper())

while guess != password:
    print()
    print("Mật khẩu sai.")
    print()

    aliens = aliens **2
    print("Có", aliens,"người ngoài hành tinh xâm nhập Trái Đất. Làm ơn, hãy nhập lại.")
    if aliens > 7400000000:
        break
    print()
    print("Gợi ý mật khẩu : thứ đang tấn công chúng ta")
    print()
    guess = input("Nhanh nào.Nhập lại mật khẩu:".upper())
if aliens > 7400000000:
    print("Khôôông ! Người ngoài hành tinh nhiều hơn loài người chúng ta.CHúng ta thua rồi")
else:
    print("Chúng ta đã chiến thắng. Cả thế giới được giải cứu rồi.")
