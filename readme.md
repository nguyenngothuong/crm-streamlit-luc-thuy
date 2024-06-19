# Ứng dụng Điểm danh học viên

Ứng dụng Điểm danh học viên là một ứng dụng Streamlit giúp quản lý việc điểm danh và theo dõi trạng thái học tập của học viên. Ứng dụng kết nối với Larkbase để lấy dữ liệu học viên và cập nhật trạng thái điểm danh.

## Cài đặt và Cấu hình

1. Clone repository này về máy tính của bạn.
2. Cài đặt các thư viện cần thiết bằng lệnh `pip install -r requirements.txt`.
3. Tạo file `secrets.toml` trong thư mục `.streamlit` và cấu hình các biến môi trường sau:
   - `lark_app_id`: ID của ứng dụng Lark.
   - `lark_app_secret`: Secret key của ứng dụng Lark.
   - `lark_app_token`: Token của ứng dụng Lark.
   - `lark_table_id`: ID của bảng Larkbase chứa dữ liệu học viên.
   - `http_basic_auth_user`: Tên đăng nhập cho xác thực HTTP Basic.
   - `http_basic_auth_password`: Mật khẩu cho xác thực HTTP Basic.
   - `webhook_url`: URL của webhook để gửi dữ liệu điểm danh.
   - `supabase_url`: URL của dự án Supabase.
   - `supabase_key_public`: Public key của dự án Supabase.

## Cấu trúc thư mục

- `app.py`: File chính để chạy ứng dụng Streamlit.
- `auth.py`: Chứa các hàm liên quan đến xác thực người dùng (đăng nhập, đăng ký, đăng xuất).
- `main_page.py`: Chứa nội dung của trang chính, bao gồm chức năng điểm danh học viên.
- `pages.py`: Chứa các trang phụ như trang đăng nhập, đăng ký và hướng dẫn sử dụng.
- `requirements.txt`: Chứa danh sách các thư viện cần thiết để chạy ứng dụng.
- `.streamlit/secrets.toml`: File cấu hình các biến môi trường.

## Lưu ý quan trọng

- Không tự ý chỉnh sửa tên cột trong Larkbase để tránh gây lỗi cho ứng dụng. Các tên cột quan trọng bao gồm:
  - Tên môn học
  - Tên học viên
  - Số điện thoại
  - ID khóa học
  - ID MÔN HỌC
  - Môn học đăng ký
  - Trạng thái

## Báo lỗi

Nếu bạn gặp bất kỳ lỗi nào trong quá trình sử dụng hoặc phát triển ứng dụng, vui lòng gửi email báo lỗi đến địa chỉ: `report@nguyenngothuong.com`. Trong email, hãy mô tả chi tiết lỗi bạn gặp phải và cung cấp các thông tin liên quan (ví dụ: ảnh chụp màn hình, thông báo lỗi, ...) để chúng tôi có thể khắc phục vấn đề nhanh chóng.

## Đóng góp

Nếu bạn muốn đóng góp vào dự án này, vui lòng tạo pull request với các thay đổi của bạn. Chúng tôi rất hoan nghênh và đánh giá cao sự đóng góp của bạn.

## Liên hệ

Nếu bạn có bất kỳ câu hỏi hoặc góp ý nào, vui lòng liên hệ với chúng tôi qua email: `contact@nguyenngothuong.com`.