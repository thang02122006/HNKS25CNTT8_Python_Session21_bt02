import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


class ItemNotFoundError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


def show_menu():
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")

    for code, item in DRINK_MENU.items():
        print(
            f"[{code}] - "
            f"{item['name']} - "
            f"{item['price']:,} VNĐ"
        )


def add_to_order(code, quantity):
    code = code.strip().upper()

    if code not in DRINK_MENU:
        raise ItemNotFoundError

    if quantity <= 0:
        raise InvalidQuantityError

    current_order.append({
        "code": code,
        "name": DRINK_MENU[code]["name"],
        "price": DRINK_MENU[code]["price"],
        "quantity": quantity
    })

    logging.info(
        f"Added {quantity} of {code} to order"
    )


def calculate_total(order):
    total = 0

    for item in order:
        total += item["price"] * item["quantity"]

    return total


def view_order():
    if not current_order:
        print(
            "Giỏ hàng trống, vui lòng chọn món "
            "(Chức năng 2)."
        )
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(
        "Mã SP | Tên đồ uống | "
        "Đơn giá | Số lượng | Thành tiền"
    )

    print("-" * 60)

    for item in current_order:
        money = item["price"] * item["quantity"]

        print(
            f"{item['code']} | "
            f"{item['name']} | "
            f"{item['price']:,} | "
            f"{item['quantity']} | "
            f"{money:,} VNĐ"
        )

    print("-" * 60)

    total = calculate_total(current_order)

    print(
        f"Tổng tiền cần thanh toán: "
        f"{total:,} VNĐ"
    )


def checkout():
    if not current_order:
        print(
            "Giỏ hàng trống, vui lòng chọn món "
            "(Chức năng 2)."
        )
        return

    total = calculate_total(current_order)

    print("\n--- THANH TOÁN ---")
    print(
        f"Tổng tiền cần thanh toán: "
        f"{total:,} VNĐ"
    )

    choice = input(
        f"Xác nhận thanh toán "
        f"{total:,} VNĐ? (y/n): "
    ).lower()

    if choice == "y":
        print("Thanh toán thành công.")
        logging.info("Checkout successful")

        current_order.clear()

        print("Giỏ hàng đã được làm trống.")

    elif choice == "n":
        print(
            "Đã hủy thao tác thanh toán. "
            "Quay lại menu chính."
        )

    else:
        print(
            "Lựa chọn không hợp lệ. "
            "Thanh toán đã bị hủy."
        )


def main():
    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            print("\n--- THÊM MÓN VÀO GIỎ ---")

            code = input("Nhập mã đồ uống: ")

            try:
                quantity = int(
                    input("Nhập số lượng: ")
                )

                add_to_order(code, quantity)

                code = code.strip().upper()

                print(
                    f"Đã thêm {quantity} x "
                    f"{DRINK_MENU[code]['name']} "
                    f"vào giỏ hàng."
                )

            except ValueError:
                logging.error(
                    "ValueError - Invalid quantity input"
                )
                print(
                    "Vui lòng nhập số lượng "
                    "là một số nguyên!"
                )

            except ItemNotFoundError:
                logging.warning(
                    f"ItemNotFoundError - Code: {code}"
                )
                print(
                    "Mã đồ uống không hợp lệ, "
                    "vui lòng kiểm tra lại thực đơn!"
                )

            except InvalidQuantityError:
                logging.warning(
                    f"InvalidQuantityError - "
                    f"Quantity: {quantity}"
                )
                print("Số lượng phải lớn hơn 0!")

        elif choice == "3":
            view_order()

        elif choice == "4":
            checkout()

        elif choice == "5":
            logging.info(
                "Cashier logged out. System shutdown."
            )

            print(
                "Đã thoát ca làm việc. "
                "Hẹn gặp lại!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()