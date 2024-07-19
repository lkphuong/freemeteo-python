# freemeteo.py

`freemeteo.py` là một script Python được thiết kế để lấy dữ liệu thời tiết từ trang web [Freemeteo](https://freemeteo.vn) và lưu trữ vào cơ sở dữ liệu PostgreSQL.

## Tính năng

- **Lấy Nội Dung Trang Web**: Sử dụng thư viện `requests` để gửi yêu cầu HTTP GET đến URL và lấy nội dung trang web.
- **Phân Tích HTML**: Sử dụng thư viện `BeautifulSoup` từ `bs4` để phân tích nội dung HTML và trích xuất dữ liệu cần thiết.
- **Kết Nối Cơ Sở Dữ Liệu**: Sử dụng `psycopg2` để kết nối với cơ sở dữ liệu PostgreSQL và thực hiện các thao tác dữ liệu.
- **Lưu Trữ Dữ Liệu**: Lưu trữ dữ liệu thời tiết đã trích xuất vào cơ sở dữ liệu.

## Cách Sử Dụng

1. **Cài Đặt Môi Trường**: Cài đặt môi trường ảo Python và cài đặt các thư viện cần thiết thông qua `pip`:

    ```sh
    python -m venv env
    source env/bin/activate  # On Unix/macOS
    env\Scripts\activate.bat # On Windows
    pip install -r requirements.txt
    ```

2. **Chạy Script**: Chạy script từ dòng lệnh:

    ```sh
    python freemeteo.py
    ```

## Cấu Trúc File

- `fetch_webpage(url)`: Lấy nội dung trang web từ URL.
- `parse_html(html_content)`: Phân tích nội dung HTML và trích xuất dữ liệu.
- `connect_db()`: Kết nối tới cơ sở dữ liệu PostgreSQL.
- `find_feemeteo(year, month)`: Tìm và lưu dữ liệu thời tiết từ Freemeteo.
- `main()`: Hàm chính để chạy script.

## Yêu Cầu

- Python 3.6+
- requests
- BeautifulSoup4
- psycopg2

## Lưu Ý

Đảm bảo rằng bạn đã cấu hình cơ sở dữ liệu PostgreSQL và cập nhật thông tin kết nối trong hàm `connect_db()` trước khi chạy script.

## Tác Giả

Script được phát triển bởi phuonglk, với mục đích lấy dữ liệu thời tiết từ Freemeteo và lưu trữ vào cơ sở dữ liệu.
