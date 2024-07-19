import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import psycopg2

def fetch_webpage(url): # Hàm lấy nội dung trang web
    try: # Thử thực hiện
        response = requests.get(url) # Gửi yêu cầu GET đến URL
        response.raise_for_status() # Nếu có lỗi thì báo lỗi
        return response.content # Trả về nội dung trang web
    except requests.exceptions.RequestException as e: # Nếu có lỗi
        print(f"Error fetching the URL: {e}") # Báo lỗi nếu có lỗi
        return None # Trả về None nếu có lỗi

def parse_html(html_content): # Hàm phân tích HTML
    soup = BeautifulSoup(html_content, 'html.parser') # Sử dụng thư viện BeautifulSoup để phân tích HTML

    table = soup.find('table', class_='monthly-history') # Tìm bảng dữ liệu có class là 'monthly-history'

    # headers = [header.text for header in table.find_all('th')] # Lấy tiêu đề của bảng
    
    rows = [] # Khởi tạo mảng chứa dữ liệu
    for row in table.find_all('tr')[1:]:  # Duyệt qua từng dòng dữ liệu
        columns = row.find_all('td') # Lấy các cột dữ liệu
        row_data = [column.text for column in columns] # Lấy dữ liệu từ các cột
        rows.append(row_data) # Thêm dữ liệu vào mảng dữ liệu
    return rows # Trả về mảng dữ liệu

def find_feemeteo(year, month): # Hàm tìm dữ liệu từ trang web freemeteo
    url = 'https://freemeteo.vn/thoi-tiet/ho-chi-minh-city/history/monthly-history/?gid=1566083&station=11437&month='+month+'&year='+year+'&language=vietnamese&country=vietnam'
    html_content = fetch_webpage(url) # Lấy nội dung trang web
    
    conn = connect_db() # Tạo kết nối tới database
    cursor = conn.cursor() # Tạo con trỏ để thao tác với database

    if html_content: # Nếu có nội dung trang web
        table = parse_html(html_content) # Lấy dữ liệu từ trang web

        for row in table: # Duyệt qua từng dòng dữ liệu
            print("row: ", row) # In ra dòng dữ liệu
            cursor.execute('INSERT INTO weather (date, min, max, wind_normal, wind_max, rain, snow, pressure, symbol, description) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)
            # Thêm dữ liệu vào bảng weather

    conn.commit() # Lưu thay đổi vào database
    cursor.close() # Đóng con trỏ
    conn.close() # Đóng kết nối

def connect_db(): # Hàm kết nối tới database
    connection = psycopg2.connect(
        dbname="",
        user="",
        password="",
        host="",
        port=""
    ) # Kết nối tới database
    return connection # Trả về kết nối


def main(): # Hàm chính
    for year in range(2019, 2025): # Duyệt qua từng năm
        for month in range(1, 13): # Duyệt qua từng tháng
            find_feemeteo(str(year), str(month).zfill(2)) # Tìm dữ liệu từ trang web freemeteo

if __name__ == "__main__":
    main()
