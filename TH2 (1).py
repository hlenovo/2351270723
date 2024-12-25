import itertools
from sympy import symbols, sympify

def parse_expression(expr_str, variables):
    # Thay thế các ký tự logic trong chuỗi với các ký tự của sympy
    expr_str = expr_str.replace("∨", "|").replace("∧", "&").replace("¬", "~")
    
    # Sử dụng sympy để phân tích chuỗi thành biểu thức logic
    expr = sympify(expr_str)
    return expr

# Hàm để đánh giá biểu thức logic với các giá trị cụ thể của các biến
def evaluate_expression(expr, variables, values):
    # Tạo dictionary với giá trị các biến
    val_dict = {var: values[i] for i, var in enumerate(variables)}
    return expr.subs(val_dict)

# Hàm tạo bảng chân trị
def generate_truth_table(expr_str):
    # Tạo danh sách các biến từ A, B, C, ... trong biểu thức
    variables = sorted(set(filter(str.isalpha, expr_str)))
    
    # Phân tích biểu thức logic từ chuỗi
    expr = parse_expression(expr_str, variables)
    
    # Tạo tất cả các tổ hợp giá trị True/False cho các biến
    truth_values = list(itertools.product([True, False], repeat=len(variables)))
    
    # In tiêu đề bảng
    print("  ".join(variables) + "  Kết quả")
    print("-" * (len(variables) * 3 + 10))
    
    # Duyệt qua từng tổ hợp giá trị và tính toán kết quả
    for values in truth_values:
        result = evaluate_expression(expr, variables, values)
        result_val = 'T' if result else 'F'
        
        row = "  ".join('T' if v else 'F' for v in values)
        print(f"{row}  {result_val}")

if __name__ == "__main__":
    expr_str = input("Nhập biểu thức logic: ")
    
    # Tạo bảng chân trị cho biểu thức
    generate_truth_table(expr_str)
