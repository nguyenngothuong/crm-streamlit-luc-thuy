# Hệ thống Quản lý Đơn hàng dựa trên Streamlit

Dự án này là một ứng dụng web dựa trên Streamlit để quản lý đơn đặt hàng của khách hàng, tích hợp với Lark Suite (Feishu) để lưu trữ và quản lý dữ liệu.

## Mục lục

1. [Cấu trúc Dự án](#cấu-trúc-dự-án)
2. [Cài đặt và Thiết lập](#cài-đặt-và-thiết-lập)
3. [Xác thực](#xác-thực)
4. [Luồng Ứng dụng Chính](#luồng-ứng-dụng-chính)
5. [Tích hợp Lark Suite](#tích-hợp-lark-suite)
6. [Giao diện Người dùng](#giao-diện-người-dùng)
7. [Xử lý Dữ liệu](#xử-lý-dữ-liệu)
8. [Tích hợp Webhook](#tích-hợp-webhook)
9. [Triển khai](#triển-khai)
10. [Bảo trì và Xử lý Sự cố](#bảo-trì-và-xử-lý-sự-cố)

## Cấu trúc Dự án

Dự án bao gồm một số file Python:

- `main.py`: Điểm vào của ứng dụng
- `pages.py`: Chứa các layout trang khác nhau
- `auth.py`: Xử lý xác thực người dùng
- `main_page.py`: Giao diện quản lý đơn hàng chính
- `lark_connector.py`: Quản lý kết nối và truy xuất dữ liệu từ Lark Suite

## Cài đặt và Thiết lập

1. Clone repository
2. Cài đặt các package cần thiết:
   ```
   pip install streamlit pandas requests uuid unidecode
   ```
3. Thiết lập biến môi trường hoặc Streamlit secrets cho thông tin nhạy cảm (API keys, thông tin đăng nhập)

## Xác thực

Xác thực được xử lý trong `auth.py`:

1. Sử dụng Supabase để quản lý người dùng
2. Hàm `login()` xác thực người dùng
3. Hàm `logout()` đăng xuất người dùng
4. Session state được sử dụng để duy trì trạng thái đăng nhập

## Luồng Ứng dụng Chính

1. `main.py` đóng vai trò là điểm vào
2. Nó kiểm tra trạng thái đăng nhập và render các trang phù hợp
3. Sử dụng `streamlit_navigation_bar` để điều hướng giữa các trang

## Tích hợp Lark Suite

`lark_connector.py` quản lý tích hợp Lark Suite:

1. `get_tenant_access_token()`: Lấy access token cho các API call
2. `get_larkbase_data_v4()`: Lấy dữ liệu từ các bảng Lark Suite
3. `create_a_record()` và `create_records()`: Thêm bản ghi mới vào bảng Lark Suite

## Giao diện Người dùng

Giao diện quản lý đơn hàng chính nằm trong `main_page.py`:

1. Hiển thị form thông tin khách hàng
2. Cho phép thêm và chỉnh sửa các mặt hàng trong đơn hàng
3. Tính toán tổng đơn hàng
4. Xử lý tải lên file đính kèm cho đơn hàng

## Xử lý Dữ liệu

1. Dữ liệu khách hàng được lấy và xử lý từ Lark Suite
2. Dữ liệu sản phẩm được truy xuất và sử dụng cho việc chọn mặt hàng trong đơn hàng
3. Dữ liệu đơn hàng được thu thập và định dạng trước khi gửi đi

## Tích hợp Webhook

Ứng dụng gửi dữ liệu đơn hàng đến một webhook:
1. Dữ liệu đơn hàng được định dạng thành một payload
2. Gửi thông qua request POST đến URL webhook đã chỉ định
3. Phản hồi được xử lý và hiển thị cho người dùng

## Triển khai

Ứng dụng có thể được triển khai bằng Streamlit sharing hoặc bất kỳ nền tảng nào hỗ trợ ứng dụng web Python.

## Bảo trì và Xử lý Sự cố

1. Thường xuyên kiểm tra và cập nhật token API Lark Suite
2. Theo dõi phản hồi webhook để phát hiện vấn đề tích hợp
3. Cập nhật các dependency
4. Kiểm tra log Streamlit để phát hiện lỗi runtime

Đối với bất kỳ vấn đề nào:
1. Xác minh kết nối Lark Suite
2. Đảm bảo endpoint webhook có thể truy cập được
3. Kiểm tra luồng xác thực với Supabase
4. Xem xét quản lý session state của Streamlit
