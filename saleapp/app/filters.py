def format_price(value):
    try:
        # Định dạng số tiền và thêm hậu tố "đ"
        return f"{value:,.0f}".replace(",", ".")
    except (ValueError, TypeError):
        # Trường hợp giá trị không hợp lệ, trả về chuỗi trống hoặc giá trị mặc định
        return "0"