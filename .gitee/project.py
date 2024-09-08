import PySimpleGUI as psg
from sympy import symbols, Eq, solve

# 创建窗口布局
layout = [
    [psg.Text('请点击按钮输入方程')],
    [psg.Text('注:**幂运算,math.sqrt(x)根号x,math.pi圆周率,math.e自然常数e')],
    [psg.Button('一元方程'), psg.Button('二元方程组')],
    [psg.Text('solution',key='-IN-')],
    [psg.Button('Exit')]
]

# 创建窗口
window = psg.Window('方程解答器', layout)
x = symbols('x')
while True:
    event, values = window.read()

    # 如果关闭窗口或点击"Exit"按钮，退出循环
    if event == psg.WIN_CLOSED or event == 'Exit':
        break

    if event == '一元方程':
        result = psg.popup_get_text('注:**幂运算,math.sqrt(x)根号x,math.pi圆周率,math.e自然常数e', title="输入方程")
        if result is not None:
            try:
                left_side, right_side = result.split('=')
                equation = Eq(eval(left_side), eval(right_side))
                solution = solve(equation, x, dict=True)
                window['-IN-'].update(solution)
            except Exception:
                psg.popup("这不是一个方程")
    if event == '二元方程组':
        equations = [psg.popup_get_text('注:**幂运算,math.sqrt(x)根号x,math.pi圆周率,math.e自然常数e', title="输入方程") for _ in range(2)]# 从用户输入获取两个方程
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
            x, y = symbols('x y')  # 声明变量
            sympy_equations = [Eq(eval(eq), 0) for eq in converted_equations]
            # 求解方程
            solution = solve(sympy_equations, dict=True)
            # 更新 GUI，显示解
            # 格式化以在窗口中显示
            formatted_solution = ', '.join(str(sol) for sol in solution)
            window['-IN-'].update(formatted_solution)
        except Exception:
            psg.popup("这不是一个方程")
            # 检查方程是否为 None
        if equations is None:
            break
        # 关闭窗口
window.close()



