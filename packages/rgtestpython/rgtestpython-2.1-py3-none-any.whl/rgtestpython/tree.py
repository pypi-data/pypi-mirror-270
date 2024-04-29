import turtle


def y(sz, level):
    """  定义Y函数，sz表示是树的尺寸， level是树的层次级别 """
    if level > 0:
        #  按照树的层次级别(level)设置树的颜色
        pen.pencolor(0, 255 // level, 0)

        pen.forward(sz)

        pen.right(angle)

        #  递归调用y函数，绘制右边子树
        y(0.8 * sz, level - 1)

        pen.pencolor(0, 255 // level, 0)

        pen.left(2 * angle)

        #  递归调用y函数，绘制左边子树
        y(0.8 * sz, level - 1)

        pen.pencolor(0, 255 // level, 0)

        pen.right(angle)
        pen.forward(-sz)


# if __name__ == '__main__':
pen = turtle.Turtle()

# 设置绘图速度
pen.speed('fastest')
# pen.speed('slowest')
# 设置颜色模式为255，即颜色范围是0~255
turtle.colormode(255)

# 设置画笔朝向
pen.right(-90)

# 设置树杈角度
# angle = 30
angle = 30
# 创建尺寸为80，层次级别是7的数
y(100, 7)

turtle.done()  # 结束绘画
