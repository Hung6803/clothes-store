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

- Thêm, sửa, xóa sản phẩm
- Thêm, sửa, xóa những thông tin đặc trưng của sản phẩm
- Hiển thị danh sách sản phẩm
- Bộ lọc sản phẩm theo danh mục, giá cả

### 3. Giỏ hàng và thanh toán

- Thêm/xóa sản phẩm vào giỏ hàng
- Thanh toán đơn hàng
- Lưu lịch sử giao dịch

### 4. Hệ thống phân quyền

- Người dùng bình thường: Mua hàng, quản lý tài khoản
- Quản trị viên: Quản lý toàn bộ hệ thống

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


