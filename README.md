# Clothes Store Web Application

## Giới thiệu

Đây là một ứng dụng web thương mại điện tử chuyên về quần áo, được xây dựng bằng **FastAPI** (Python) cho backend và **Vue.js** cho frontend. Ứng dụng cung cấp các chức năng như quản lý người dùng, sản phẩm, đơn hàng, giỏ hàng và thanh toán.

## Công nghệ sử dụng

- **Backend (server/):** FastAPI, SQLAlchemy, Pydantic.
- **Frontend (client/):** Vue.js (Axios, Vue Router, Pinia, Ant Design Vue).
- **Cơ sở dữ liệu:** PostgreSQL.
- **Giao tiếp:** REST API.
- **Triển khai:** Docker.

## Chức năng chính

### 1. Quản lý người dùng

- Đăng ký, đăng nhập, đăng xuất.
- Cập nhật thông tin cá nhân.
- Quản lý danh sách người dùng (Admin).

### 2. Quản lý sản phẩm

- Thêm, sửa, xóa sản phẩm, thông tin về sản phẩm (Admin).
- Thêm, sửa, xóa những thông tin đặc trưng của sản phẩm: thương hiệu, kiểu dáng, size (Admin).
- Hiển thị danh sách sản phẩm.
- Bộ lọc sản phẩm theo danh mục, giá cả.

### 3. Giỏ hàng và thanh toán

- Thêm/xóa sản phẩm vào giỏ hàng.
- Thanh toán đơn hàng.
- Lưu lịch sử giao dịch.

### 4. Hệ thống phân quyền

- Khách hàng (User): Xem thông tin sản phẩm, tìm kiến chọn lọc sản phẩm, mua hàng, quản lý tài khoản cá nhân.
- Quản trị viên (Admin): Quản lý toàn bộ hệ thống, xem những đơn hàng mới và xử lý đơn hàng được đặt.

## Giao diện các trang

Giao diện Admin được thiết kế đơn giản sử dụng những Components của Ant Design Vue. Giao diện User được sử dụng và tùy biến phù hợp với website từ template có sẵn (Adara - Modern & Multipurpose eCommerce Template).

### 1. Trang chủ (`/`)

- Hiển thị thông tin tổng quan về cửa hàng.
  ![image](https://github.com/user-attachments/assets/02b2bad8-b53f-4b09-a267-a09bedb4b5c0)

- Đưa ra những sản phẩm bán chạy hoặc những sản phẩm giảm giá.
  ![image](https://github.com/user-attachments/assets/f429c874-b3f8-4ec4-8758-2dd8acab816d)

### 2. Trang đăng nhập, đăng ký (`/login`)

- Form nhập email, mật khẩu.
  ![dang_nhap](https://github.com/user-attachments/assets/45a2593d-9d8d-485b-b8b8-6d345a13d351)

- Điều hướng về trang chủ sau khi đăng nhập thành công.
  ![dang_nhap_thanh_cong](https://github.com/user-attachments/assets/6a92fb0d-bc87-4336-a0f7-32d328a163ed)

- Form nhập thông tin đăng ký.
  ![dang_ky](https://github.com/user-attachments/assets/9c206157-ba03-4bf4-b3f5-4204057fe18e)

- Điều hướng về trang đăng nhập sau khi đăng ký thành công.
  ![dang_ky_thanh_cong](https://github.com/user-attachments/assets/7001dcd2-96ee-4825-9eb2-e0fc426e1a60)
  
### 3. Trang sản phẩm (`/shop`)

- Hiển thị danh sách sản phẩm: Bên trái là danh sách sản phẩm thể hiện hình ảnh, tên và giá bán, giá giảm của sản phẩm, có thể chọn sắp xếp sản phẩm tăng dần hoặc giảm dần theo giá. Danh sách sản phẩm được phân trang theo 9 sản phẩm một trang. Bên phải là bộ lọc để tìm kiếm sản phẩm theo tên, thương hiệu, kiểu dáng, size, giá tiền.
  ![ds_sp](https://github.com/user-attachments/assets/898714b0-1ce3-478d-8b78-a050d9909f06)

- Khi chọn một sản phẩm thì chuyển đến trang chi tiết sản phẩm: Hiển thị đầy đủ thông tin sản phẩm. Bên dưới có gợi ý những sản phẩm cùng kiểu dáng để khách hàng có thêm lựa chọn. Khi chọn được sản phẩm muốn mua chọn size của mình, số lượng sản phẩm cần mua và bấm "Thêm vào giỏ hàng". 
  ![ct_spsp](https://github.com/user-attachments/assets/289fc8cf-54a8-4bf6-8a18-53d6a2fc39ea)
  
### 4. Trang giỏ hàng (`/cart`)

- Danh sách sản phẩm đã thêm vào giỏ: Sau khi thêm sản phẩm vào giỏ hàng ta có thể xem danh sách sản phẩm ở vị trí giỏ hàng góc trên bên phải màn hình.
  ![ds_sp_gio_hang](https://github.com/user-attachments/assets/00c34f0c-0001-4aae-906b-0dca13ccbdac)

- Để xem chi tiết và chỉnh sửa giỏ hàng có thể bấm vào xem chi tiết giỏ hàng: có thể thay đổi size, số lượng của sản phẩm đã có trong giỏ hàng.
  ![ct_gio_hang](https://github.com/user-attachments/assets/4f222c6c-38e9-41d9-9e50-ed7141143f7d)

- Sau khi chọn xong sản phẩm khách hàng nhấn nút đặt hàng: Cần nhập đầy đủ thông tin của khách hàng, nếu đã đăng nhập thì thông tin khách hàng sẽ được tự động điền. Sau khi xác nhận hoàn tất sẽ có thông báo đặt hàng thành công và sẽ trừ số lượng sản phẩm tương ứng ở trong kho hàng.
  ![image](https://github.com/user-attachments/assets/2016d1ad-381e-4585-a318-5337dfc1621a)
  
  ![image](https://github.com/user-attachments/assets/b252e22b-6f5c-4909-856b-2e3c32bc2314)

### 5. Trang quản trị (`/admin`)

- Quản lý thương hiệu, kiểu dáng và size của sản phẩm: chức năng thêm cần nhập tên của thương hiệu, kiểu dáng hoặc size cần tạo mới; chức năng sửa tên của thương hiệu, kiểu dáng hoặc size; chức năng xóa thương hiệu, kiểu dáng hoặc size cần thiết.
    + Hiển thị danh sách kiểu dáng: danh sách kiểu dáng, phân trang và có nút chức năng thêm, sửa, xóa.
      ![danh_sach_kieu_dang](https://github.com/user-attachments/assets/1a84eb9a-41d4-4160-8b4e-9261122dae32)

    + Thêm thương hiệu mới: Khi thêm mới hoàn thành sẽ quay lại trang hiển thị danh sách thương hiệu.
      ![them_thuong_hieu](https://github.com/user-attachments/assets/7695726a-1e9e-4e3d-abcb-e0997e5a3edc)
      
    + Xóa thương hiệu: Khi xóa cần đảm bảo không có sản phẩm nào thuộc thương hiệu này mới có thể xóa được. Khi xóa sẽ có thông báo xác nhận.
      ![Anh_thong_bao_xoa](https://github.com/user-attachments/assets/692cba9d-aafb-4e71-b430-506503fc3ba2)
      
      ![Xoa_that_bai](https://github.com/user-attachments/assets/05a276b9-6af2-4897-bbf6-1f4e1306b226)
      
- Quản lý sản phẩm: Gồm những chức năng thêm, sửa, xóa sản phẩm.
    + Hiển thị danh sách sản phẩm: hiển thị những thông tin tiêu biểu của một sản phẩm bao gồm ảnh (hiển thị 1 trong các ảnh của sản phẩm), tên sản phẩm, kiểu dáng, thương hiệu, giá bán, và phần trăm giảm giá hiện tại của sản phẩm.
      ![ds_sp](https://github.com/user-attachments/assets/2bb7713c-1a36-4b4d-9035-83e39adef33f)

    + Thêm sản phẩm: Điền những thông tin về sản phẩm tên sản phẩm, giá bán, và phần trăm giảm giá hiện tại của sản phẩm. Lựa chọn kiểu dáng, thương hiệu của sản phẩm. Upload ảnh của sản phẩm.
      ![image](https://github.com/user-attachments/assets/5371129a-68c5-4354-b5e1-8c77df95dbf4)

    + Sửa thông tin sản phẩm: Admin có thể sửa thông tin về sản phẩm, thêm hoặc xóa hình ảnh sản phẩm.
      ![image](https://github.com/user-attachments/assets/6e88afeb-ac4a-493d-9696-a06e69a93fc1)

    + Xóa sản phẩm: Khi xóa cần đảm bảo không có sản phẩm nào trong kho hàng, nếu xóa thành công sẽ có thông báo.
      ![image](https://github.com/user-attachments/assets/3f6914fb-7886-42dd-82dc-eda40eaae89c)

      ![image](https://github.com/user-attachments/assets/84a107c0-9f42-4dfe-bc84-9ee2cf3067b8)

- Quản lý kho hàng: Gồm những chức năng thêm, sửa, xóa sản phẩm trong kho hàng.
    + Thêm sản phẩm vào kho: Chọn sản phẩm và size của sản phẩm muốn thêm và nhập thông tin về giá nhập và số lượng của sản phẩm đó.
      ![image](https://github.com/user-attachments/assets/a20f6ce9-de6f-4dfe-aecb-51bf9d9a39f4)

    + Sửa thông tin về số lượng và giá nhập của sản phẩm được chọn sau khi thành công sẽ có thông báo.
      ![image](https://github.com/user-attachments/assets/ee74116c-ffe3-4d62-9412-1445dafd344c)

      ![image](https://github.com/user-attachments/assets/82fe8bee-9a89-4773-b054-0a31226beb22)

    + Xóa sản phẩm được chọn khi cần thiết: đảm bảo sản phẩm chưa được thực hiện giao dịch với khách hàng.
      ![image](https://github.com/user-attachments/assets/18238902-3d6f-4c85-8808-ab5ac90e5c54)
        Sản phẩm đã có trong hóa đơn đặt hàng của khách.
      
      ![image](https://github.com/user-attachments/assets/5b976317-2827-492e-8fcb-0762ec8e8256)
        Không thể thực hiện xóa được.
      
- Quản lý đơn đặt hàng:
    + Có thể xem những đơn hàng mới được đặt để xác nhận đơn hàng cho khách và thực hiện xử lý, lựa chọn một đơn hàng cụ thể có thể xem chi tiết đơn hàng.
      ![image](https://github.com/user-attachments/assets/37d80971-b841-40dc-8044-77bcc74fb505)

      ![image](https://github.com/user-attachments/assets/3a898b99-490a-446c-9e97-285e6cf9463a)

    + Xem danh sách đơn đặt hàng: có thể xem được những thông tin cơ bản của đơn hàng, lựa chọn một đơn hàng cụ thể có thể xem chi tiết đơn hàng tương tự như phần đơn hàng mới.
      ![image](https://github.com/user-attachments/assets/034a5c33-904c-42d0-938b-0aa1e208242c)
