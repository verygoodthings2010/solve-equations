import PySimpleGUI as psg
from sympy import symbols, Eq, solve
import sympy as sp

# 创建窗口布局
layout = [
    [psg.Text('请点击按钮输入方程')],
    [psg.Text('注:**幂运算,math.sqrt(x)根号x,math.pi圆周率,math.e自然常数e，乘号*不能省略')],
    [psg.Button('线性方程')],
    [psg.Text('solution', key='-IN-')],
    [psg.Button('Exit')]
]

# 创建窗口
window = psg.Window('方程解答器', layout)
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')  # 声明变量

while True:
    event, values = window.read()

    # 如果关闭窗口或点击"Exit"按钮，退出循环
    if event == psg.WIN_CLOSED or event == 'Exit':
        break

    if event == '线性方程':
        time = psg.popup_get_text('输入方程数量', title="输入方程数量")
        equations = [psg.popup_get_text('注:**幂运算,math.sqrt(x)根号x,math.pi圆周率,math.e自然常数e，乘号*不能省略', title="输入方程")for _ in range(int(time))]  # 从用户输入获取两个方程
        try:
            def convert_equations(equations):  # 化为标准式
                converted = []
                for eq in equations:
                    left, right = eq.split('=')
                    if right == '0':
                        converted.append(left)  # 保留左侧
                    else:
                        converted.append(f"{left}-{right}")  # 变为左侧 - 右侧
                return converted  # 返回一个列表


            # 使用转换函数
            converted_equations = convert_equations(equations)
            # 转换为 SymPy 方程并求解
            sympy_equations = [Eq(eval(eq), 0) for eq in converted_equations]
            # 求解方程
            solution = solve(sympy_equations, dict=True)
            # 更新 GUI，显示解
            # 格式化以在窗口中显示
            formatted_solution = ', '.join(str(sol) for sol in solution)
            window['-IN-'].update(formatted_solution)
        except Exception:
            psg.popup("这不是一个方程")

        # 关闭窗口
window.close()
