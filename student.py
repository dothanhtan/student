class Student:
    __data = []

    def find_student(self, _id):
        for index in range(0, len(self.__data)):
            if self.__data[index]['id'] == _id:
                return [index, self.__data[index]]
        return False

    def add(self):
        print('*** Hàm thêm sinh viên ***')
        infor = {'id': '', 'name': ''}
        _id = input('Nhập ID: ')
        while True:
            student = self.find_student(_id)
            if student is not False:
                print('ID đã tồn tại, vui lòng nhập lại!')
                _id = input('Nhập ID: ')
            else:
                break
        infor['id'] = _id
        name = input('Nhập tên: ')
        infor['name'] = name
        self.__data.append(infor)

    def edit(self):
        print('*** Hàm sửa sinh viên ***')
        _id = input('Nhập ID: ')
        student = self.find_student(_id)
        if student is False:
            print('Không tìm thấy sinh viên', _id)
        else:
            name = input('Nhập tên: ')
            student[1]['name'] = name
            self.__data[student[0]] = student[1]

    def delete(self):
        print('*** Hàm xóa sinh viên ***')
        _id = input('Nhập ID: ')
        student = self.find_student(_id)
        if student is not False:
            self.__data.remove(student[1])
            print(f'Xóa sinh viên {_id} thành công')
        else:
            print(f'Không tìm thấy sinh viên {_id} cần xóa!')

    def show(self):
        print('DANH SÁCH SINH VIÊN HIỆN TẠI')
        size = len(self.__data) - 1
        for index in range(0, size):
            print(f"[{self.__data[index]['id']} - {self.__data[index]['name']}]", end=', ')
        print(f"[{self.__data[size]['id']} - {self.__data[size]['name']}]")
