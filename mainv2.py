import streamlit as st
from datetime import datetime, date, time
import json
import pytz
from lark_connector import get_larkbase_data_v4, get_tenant_access_token
import requests
from requests.auth import HTTPBasicAuth


# Lấy múi giờ GMT+7 (giờ Hồ Chí Minh, Việt Nam)
timezone_vietnam = pytz.timezone('Asia/Ho_Chi_Minh')


def format_phone_number(phone_number):
    return f"{phone_number[:3]}***{phone_number[-3:]}"


lark_app_id = st.secrets["lark_app_id"]
lark_app_secret = st.secrets["lark_app_secret"]
tenant_access_token = get_tenant_access_token(lark_app_id, lark_app_secret)
lark_app_token = st.secrets["lark_app_token"]
lark_table_id = st.secrets["lark_table_id"]
http_basic_auth_user = st.secrets["http_basic_auth_user"]
http_basic_auth_password = st.secrets["http_basic_auth_password"]
webhook_url = st.secrets["webhook_url"]


payload = {
    "field_names": ["Tên học viên","Số điện thoại","ID khóa học", "ID MÔN HỌC", "Môn học đăng ký", "Trạng thái"],
    "filter": {
        "conjunction": "and",
        "conditions": [
            {
                "field_name": "Trạng thái",
                "operator": "isNot",
                "value": ["Đã học"]
            }
        ]
    },
  "automatic_fields": True
}

records = get_larkbase_data_v4(tenant_access_token, lark_app_token, lark_table_id, payload=payload , app_id=lark_app_id, app_secret=lark_app_secret)

def save_data_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

save_data_to_json(records,"records.json")

# # Đọc dữ liệu học viên từ file JSON test code
# with open('data.json', 'r', encoding='utf-8') as f:
#     records = json.load(f)

# Tiêu đề của ứng dụng
st.title("Điểm danh học viên")

# Lấy danh sách khóa học
khoa_hoc_list = list(set(hv['fields'].get('ID khóa học', {}).get('value', [{}])[0].get('text', '') for hv in records))

# Hàm để bóc tách số từ khóa học
def extract_number(khoa_hoc):
    return int(khoa_hoc.split(' ')[0][1:])

# Sắp xếp danh sách khóa học theo số đằng sau "K"
khoa_hoc_list = sorted(khoa_hoc_list, key=extract_number, reverse=True)

# Chọn khóa học
selected_khoa_hoc = st.selectbox("Chọn khóa học", khoa_hoc_list)

# Lấy danh sách môn học theo khóa học đã chọn
mon_hoc_list = list(set(hv['fields'].get('ID MÔN HỌC', {}).get('value', [{}])[0].get('text', '') for hv in records if hv['fields'].get('ID khóa học', {}).get('value', [{}])[0].get('text', '') == selected_khoa_hoc))
# Sắp xếp danh sách môn học theo thứ tự từ Z đến A
mon_hoc_list = sorted(mon_hoc_list, reverse=False)

# Chọn môn học
selected_mon_hoc = st.selectbox("Chọn môn học", mon_hoc_list)

col1, col2 = st.columns(2)

# Chọn ngày học
today = date.today()
with col1:
    selected_ngay_hoc = st.date_input("Ngày học", value=today)

# Lấy thời gian hiện tại theo múi giờ GMT+7
now = datetime.now(timezone_vietnam)
with col2:
    selected_thoi_gian_diem_danh = st.time_input("Thời gian điểm danh", value="now")

# Lọc danh sách học viên theo khóa học và môn học đã chọn
filtered_hoc_vien = [hv for hv in records if hv['fields'].get('ID khóa học', {}).get('value', [{}])[0].get('text', '') == selected_khoa_hoc and hv['fields'].get('ID MÔN HỌC', {}).get('value', [{}])[0].get('text', '') == selected_mon_hoc]

st.write("---")
# Hiển thị thông tin học viên và checkbox để tích chọn trạng thái
for i, hv in enumerate(filtered_hoc_vien, start=1):
    st.write(f"STT: {i}")
    st.write(f"Tên học viên: {hv['fields'].get('Tên học viên', {}).get('value', [{}])[0].get('text', '')}")
    st.write(f"Số điện thoại: {format_phone_number(hv['fields'].get('Số điện thoại', {}).get('value', [''])[0])}")
    hv['trang_thai'] = st.checkbox("Điểm danh", key=f"{selected_khoa_hoc}_{selected_mon_hoc}_{i}")
    st.write("---")






def send_data_to_webhook(json_data, webhook_url, user, password):
    # Thiết lập thông tin xác thực
    auth = HTTPBasicAuth(user, password)

    # Gửi yêu cầu POST đến webhook với dữ liệu JSON và xác thực
    response = requests.post(webhook_url, json=json_data, auth=auth)

    # Kiểm tra kết quả gửi
    if response.status_code == 200:
        print("Dữ liệu đã được gửi thành công đến webhook.")
    else:
        print("Gửi dữ liệu đến webhook thất bại.")
        print("Mã trạng thái:", response.status_code)
        print("Nội dung phản hồi:", response.text)
        
# Nút xác nhận gửi đi
if st.button("Xác nhận"):
    diem_danh_data = []
    # Lặp qua danh sách học viên đã lọc
    for hv in filtered_hoc_vien:
        if hv.get('trang_thai', False):
            diem_danh_data.append({
                "record_id": hv['record_id'],
                "fields": {
                    "Trạng thái": "Đã học"
                }
            })
        else:
            diem_danh_data.append({
                "record_id": hv['record_id'],
                "fields": {
                    "Trạng thái": "Chưa học"
                }
            })
    
    # Lưu dữ liệu điểm danh vào file JSON
    # save_data_to_json(diem_danh_data, "diem_danh.json")
    # Gửi dữ liệu điểm danh đến webhook
    send_data_to_webhook(diem_danh_data, webhook_url, http_basic_auth_user, http_basic_auth_password)
    # Hiển thị thông báo thành công
    st.success("Điểm danh thành công và đã gửi dữ liệu đến Larkbase!")