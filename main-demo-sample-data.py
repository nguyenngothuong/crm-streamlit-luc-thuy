import streamlit as st
from datetime import datetime, date, time



def format_phone_number(phone_number):
    return f"{phone_number[:3]}***{phone_number[-3:]}"


# Danh sách thông tin học viên
hoc_vien = [
    {"ten": "Nguyễn Văn A", "sdt": "0123456789", "mon_hoc": "Toán", "khoa_hoc": "Khóa 1", "trang_thai": False},
    {"ten": "Trần Thị B", "sdt": "0987654321", "mon_hoc": "Lý", "khoa_hoc": "Khóa 2", "trang_thai": False},
    {"ten": "Lê Văn C", "sdt": "0909090909", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 1", "trang_thai": False},
    {"ten": "Phạm Thị D", "sdt": "0888888888", "mon_hoc": "Văn", "khoa_hoc": "Khóa 3", "trang_thai": False},
    {"ten": "Hoàng Văn E", "sdt": "0777777777", "mon_hoc": "Toán", "khoa_hoc": "Khóa 2", "trang_thai": False},
    {"ten": "Vũ Thị F", "sdt": "0666666666", "mon_hoc": "Lý", "khoa_hoc": "Khóa 1", "trang_thai": False},
    {"ten": "Đặng Văn G", "sdt": "0555555555", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 3", "trang_thai": False},
    {"ten": "Bùi Thị H", "sdt": "0444444444", "mon_hoc": "Văn", "khoa_hoc": "Khóa 2", "trang_thai": False},
    {"ten": "Lý Văn I", "sdt": "0333333333", "mon_hoc": "Toán", "khoa_hoc": "Khóa 3", "trang_thai": False},
    {"ten": "Trương Thị K", "sdt": "0222222222", "mon_hoc": "Lý", "khoa_hoc": "Khóa 1", "trang_thai": False},
    {"ten": "Ngô Văn L", "sdt": "0111111111", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 2", "trang_thai": False},
    {"ten": "Hà Thị M", "sdt": "0999999999", "mon_hoc": "Văn", "khoa_hoc": "Khóa 1", "trang_thai": False},
    {"ten": "Dương Văn N", "sdt": "0888888888", "mon_hoc": "Toán", "khoa_hoc": "Khóa 2", "trang_thai": False},
    {"ten": "Tạ Thị O", "sdt": "0777777777", "mon_hoc": "Lý", "khoa_hoc": "Khóa 3", "trang_thai": False},
    {"ten": "Phan Văn P", "sdt": "0666666666", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 1", "trang_thai": False},
    {"ten": "Đỗ Thị Q", "sdt": "0555555555", "mon_hoc": "Văn", "khoa_hoc": "Khóa 2", "trang_thai": False},
    {"ten": "Vương Văn R", "sdt": "0444444444", "mon_hoc": "Toán", "khoa_hoc": "Khóa 1", "trang_thai": False},
    {"ten": "Lâm Thị S", "sdt": "0333333333", "mon_hoc": "Lý", "khoa_hoc": "Khóa 3", "trang_thai": False},
    {"ten": "Trần Văn T", "sdt": "0222222222", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 2", "trang_thai": False},
    {"ten": "Nguyễn Thị U", "sdt": "0111111111", "mon_hoc": "Văn", "khoa_hoc": "Khóa 1", "trang_thai": False}
]

# Tiêu đề của ứng dụng
st.title("Danh sách thông tin học viên")

# Lấy danh sách khóa học
khoa_hoc_list = list(set(hv['khoa_hoc'] for hv in hoc_vien))

# Chọn khóa học
selected_khoa_hoc = st.selectbox("Chọn khóa học", khoa_hoc_list)

# Lấy danh sách môn học theo khóa học đã chọn
mon_hoc_list = list(set(hv['mon_hoc'] for hv in hoc_vien if hv['khoa_hoc'] == selected_khoa_hoc))

# Chọn môn học
selected_mon_hoc = st.selectbox("Chọn môn học", mon_hoc_list)

col1, col2 = st.columns(2)

# Chọn ngày học
today = date.today()
with col1:
    selected_ngay_hoc = st.date_input("Ngày học", value=today, min_value=today)

# Chọn thời gian điểm danh
now = datetime.now()
default_time = now.time()
with col2:
    selected_thoi_gian_diem_danh = st.time_input("Thời gian điểm danh", value=default_time)

# Lọc danh sách học viên theo khóa học và môn học đã chọn
filtered_hoc_vien = [hv for hv in hoc_vien if hv['khoa_hoc'] == selected_khoa_hoc and hv['mon_hoc'] == selected_mon_hoc]


st.write("---")
# Hiển thị thông tin học viên và checkbox để tích chọn trạng thái
for i, hv in enumerate(filtered_hoc_vien, start=1):
    st.write(f"STT: {i}")
    st.write(f"Tên: {hv['ten']}")
    st.write(f"Số điện thoại: {format_phone_number(hv['sdt'])}")
    hv['trang_thai'] = st.checkbox("Đã học", key=f"{selected_khoa_hoc}_{selected_mon_hoc}_{i}")
    st.write("---")
    
# Nút xác nhận gửi đi
if st.button("Xác nhận"):
    # In ra trạng thái học viên đã chọn
    for hv in filtered_hoc_vien:
        if hv['trang_thai']:
            st.write(f"Học viên {hv['ten']} đã học.")
        else:
            st.write(f"Học viên {hv['ten']} chưa học.")