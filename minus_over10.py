from manim import *

class Subtract59From31Dot(Scene):
    def construct(self):
        # 創建題目（使用者輸入的問題）
        self.create_texts()

        # 創建點和圈
        self.minus_dots()

        self.show_answer()
        
    def create_texts(self):
        n1 = 61
        n2 = 39
        
        s1 = f"小明有{n1}個糖果, 他給了小红{n2}個, 現在剩下多少個?"
        s2 = f"首先我們有{n1}顆糖果"
        s3 = f"他給了小红{n2}顆"
        s4 = f"我們可以把十位數跟個位數分開"
        s5 = f"{n1}可以被分成{n1 // 10}個10跟{n1 % 10}個1"
        s6 = f"要從{n1}拿出{n2}個"
        s7 = f"把要給的1拿出, 再把要給的10拿出"
        s8 = f"數數看剩下共有幾個點" 
        s9 = f"因此我們最後剩下{n1 - n2}顆"
        
        self.title = Text(s1, font="Noto Sans CJK", font_size=36, color=YELLOW).to_edge(UP)
        self.exp_1 = Text(s2, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 2)
        self.exp_2 = Text(s3, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        self.exp_3 = Text(s4, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4)
        self.exp_4 = Text(s5, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + DOWN * 1)
        self.exp_5 = Text(s6, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 2)
        self.exp_6 = Text(s7, font="Noto Sans CJK", font_size=30, color=GREEN).move_to(LEFT * 4 + UP * 1)
        self.exp_7 = Text(s8, font="Noto Sans CJK", font_size=24, color=GREEN).move_to(LEFT * 4)
        self.ans = Text(s9, font="Noto Sans CJK", font_size=30, color=YELLOW).to_edge(DOWN)

        # 打印文字
        self.play(Write(self.title))
        self.wait(1)
        self.play(Write(self.exp_1))
        self.wait(1)
        self.play(Write(self.exp_2))
        self.wait(1)
        self.play(Write(self.exp_3))
        self.wait(1)
        self.play(Write(self.exp_4))
        self.wait(1)
        self.play(FadeOut(self.exp_1), FadeOut(self.exp_2), FadeOut(self.exp_3), FadeOut(self.exp_4))
        self.play(Write(self.exp_5))
        self.wait(1)
        self.play(Write(self.exp_6))
        self.wait(1)
        self.play(Write(self.exp_7))

        #借位時的文字解釋
        if n1 % 10< n2 % 10:
            self.text1 =  Text(f"因為個位數不夠減", font="Noto Sans CJK", font_size=24).move_to(LEFT * 4+ DOWN * 1)
            self.text2 =  Text(f"我們必須把一個10拆開變成10個1", font="Noto Sans CJK", font_size=24).move_to(LEFT * 4 + DOWN * 2)
            self.play(FadeIn(self.text1), FadeIn(self.text2))


    def minus_dots(self):
        #創建點
        n1=61
        n2=39
        units1 = n1 % 10
        tens1 = n1 // 10
        units2 = n2 % 10
        tens2 = n2 // 10
        
        unit_dots1 = []
        ten_circles1 = []
        
        for j in range(units1):
            dot = Dot(point=(j * 0.3 - 0.5, 0.5, 0), color=RED)
            unit_dots1.append(dot)
        
        for i in range(tens1):
            circle = Circle(radius=0.3, color=RED).move_to((i * 0.6 - 0.5, 0, 0))
            text = Text("10", font="Noto Sans CJK", font_size=24).move_to(circle.get_center())
            ten_circles1.append(VGroup(circle, text))

        # 打印所有點
        for dot in unit_dots1:
            self.play(FadeIn(dot), run_time=0.05)
        for circle in ten_circles1:
            self.play(FadeIn(circle), run_time=0.1)
        pre_num = Text(str(n1), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        self.play(FadeIn(pre_num))
        
        

        #借位
        if units1<units2:
            tens1-=1
            units1+=10
            self.play(ten_circles1[tens1].animate.move_to(DOWN * 1.5))
            for j in range(j+10):
                dot = Dot(point=((j+1) * 0.3 - 0.5,0.5, 0), color=YELLOW)
                self.play(FadeIn(dot), run_time=0.1)
                unit_dots1.append(dot)
            self.wait(2)
            self.remove(ten_circles1[tens1])
            ten_circles1.remove(ten_circles1[tens1])


        #把要提出的點拿出
        selected_dots = unit_dots1[:units2]
        selected_circles = ten_circles1[:tens2]
        
        for dot in selected_dots:
            dot.set_color(BLUE)
            self.play(dot.animate.move_to(RIGHT * ((unit_dots1.index(dot) - units2/2)*0.5+2) + DOWN * 1), run_time=0.5)
        
        for circle in selected_circles:
            circle[0].set_color(BLUE)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * ((ten_circles1.index(circle) - tens2/2)*0.5+2) + DOWN * 1.5), run_time=0.5)
        minus =Text("-", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 1) 
        lat_num = Text(str(n2), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6 + DOWN * 2)
        self.play(FadeIn(minus),FadeIn(lat_num),FadeOut(self.exp_5), FadeOut(self.exp_6),FadeOut(self.text1),FadeOut(self.text2))
        self.wait(2)
        for dot in selected_dots:
            self.remove(dot)
        for circle in selected_circles:
            self.remove(circle)

        self.play(pre_num.animate.move_to(LEFT * 2 + DOWN * 2))
        self.play(minus.animate.move_to(LEFT * 1 + DOWN * 2))
        self.play(lat_num.animate.move_to(DOWN * 2))

        #計算剩下的點
        remaining_dots = [dot for dot in unit_dots1 if dot not in selected_dots]
        remaining_circles = [circle for circle in ten_circles1 if circle not in selected_circles]
        
        
        for dot in remaining_dots:
            dot.set_color(GREEN)
            self.play(dot.animate.move_to(RIGHT * (remaining_dots.index(dot) )*0.5 + UP * 1), run_time=0.5)
        
        for circle in remaining_circles:
            circle[0].set_color(GREEN)
            circle[1].set_color(WHITE)
            self.play(circle.animate.move_to(RIGHT * (remaining_circles.index(circle) )), run_time=0.5)
        self.wait(1)

        #打印答案
    def show_answer(self): 
        n1=61
        n2=39   
        ans_text = Text(str(n1-n2), font="Noto Sans CJK", font_size=40).move_to(RIGHT * 6)
        equal_text = Text("=", font="Noto Sans CJK", font_size=40).move_to(RIGHT * 4 + DOWN * 2.5)

        self.play(FadeIn(ans_text))
        self.wait(1)
        self.play(equal_text.animate.move_to(RIGHT * 1 + DOWN * 2))
        self.play(ans_text.animate.move_to(RIGHT * 2 + DOWN * 2))
        self.play(Write(self.ans))
        self.wait(2)
        

