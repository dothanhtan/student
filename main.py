import student

if __name__ == '__main__':
    s = student.Student()
    action = 0
    while action >= 0:
        if action == 1:
            s.add()
        elif action == 2:
            s.edit()
        elif action == 3:
            s.delete()
        elif action == 4:
            s.show()

        print('Chọn chức năng muốn thực hiện')
        print('Nhập 1: Thêm sinh viên')
        print('Nhập 2: Sửa sinh viên')
        print('Nhập 3: Xóa sinh viên')
        print('Nhập 4: Hiển thị sinh viên')
        print('Nhập 0: Thoát khỏi chương trình')
        action = int(input('Nhập số cần thao tác: '))
        if action == 0:
            break
