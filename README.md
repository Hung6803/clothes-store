# Clothes Store Web Application

## Giới thiệu

Đây là một ứng dụng web thương mại điện tử chuyên về quần áo, được xây dựng bằng **FastAPI** (Python) cho backend và **Vue.js** cho frontend. Ứng dụng cung cấp các chức năng như quản lý người dùng, sản phẩm, đơn hàng, giỏ hàng và thanh toán.

## Công nghệ sử dụng

- **Backend (server/):** FastAPI, SQLAlchemy, Pydantic
- **Frontend (client/):** Vue.js (Axios, Vue Router, Pinia)
- **Cơ sở dữ liệu:** PostgreSQL
- **Giao tiếp:** REST API
- **Triển khai:** Docker

## Chức năng chính

### 1. Quản lý người dùng

- Đăng ký, đăng nhập, đăng xuất
- Cập nhật thông tin cá nhân
- Quản lý danh sách người dùng (Admin)

### 2. Quản lý sản phẩm

- Thêm, sửa, xóa sản phẩm, thông tin về sản phẩm (Admin)
- Thêm, sửa, xóa những thông tin đặc trưng của sản phẩm: thương hiệu, kiểu dáng, size (Admin)
- Hiển thị danh sách sản phẩm
- Bộ lọc sản phẩm theo danh mục, giá cả

### 3. Giỏ hàng và thanh toán

- Thêm/xóa sản phẩm vào giỏ hàng
- Thanh toán đơn hàng
- Lưu lịch sử giao dịch

### 4. Hệ thống phân quyền

- Khách hàng (User): Xem thông tin sản phẩm, tìm kiến chọn lọc sản phẩm, mua hàng, quản lý tài khoản cá nhân
- Quản trị viên (Admin): Quản lý toàn bộ hệ thống, xem những đơn hàng mới và xử lý đơn hàng được đặt

## Giao diện các trang

### 1. Trang chủ (`/`)

- Hiển thị danh sách sản phẩm
- Thanh tìm kiếm, bộ lọc danh mục

### 2. Trang đăng nhập (`/login`)

- Form nhập email, mật khẩu
- Điều hướng sau khi đăng nhập thành công

### 3. Trang giỏ hàng (`/cart`)

- Danh sách sản phẩm đã thêm vào giỏ
- Tùy chọn thanh toán

### 4. Trang quản trị (`/admin`)

- Quản lý danh sách sản phẩm, đặc trưng sản phẩm, đơn hàng, người dùng
- Quản lý thương hiệu, kiểu dáng và size của sản phẩm: được thiết kế tương tự nhau với chức năng thêm thì chỉ cần nhập tên của thương hiệu, kiểu dáng hoặc size cần tạo mới; chức năng sửa tên của thương hiệu, kiểu dáng hoặc size; chức năng xóa thương hiệu, kiểu dáng hoặc size cần thiết.
    + Hiển thị danh sách kiểu dáng: danh sách kiểu dáng, phân trang và có nút chức năng thêm, sửa, xóa
      ![danh_sach_kieu_dang](https://github.com/user-attachments/assets/1a84eb9a-41d4-4160-8b4e-9261122dae32)

    + Thêm thương hiệu mới: Khi thêm mới hoàn thành sẽ quay lại trang hiển thị danh sách thương hiệu
      ![them_thuong_hieu](https://github.com/user-attachments/assets/7695726a-1e9e-4e3d-abcb-e0997e5a3edc)
      
    + Xóa thương hiệu: Khi xóa cần đảm bảo không có sản phẩm nào thuộc thương hiệu này mới có thể xóa được. Khi xóa sẽ có thông báo xác nhận.
      ![Anh_thong_bao_xoa](https://github.com/user-attachments/assets/692cba9d-aafb-4e71-b430-506503fc3ba2)
      ![Xoa_that_bai](https://github.com/user-attachments/assets/05a276b9-6af2-4897-bbf6-1f4e1306b226)
      
    + 
