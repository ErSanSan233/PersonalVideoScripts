from manimlib.imports import *

mode = 0  # 1 for black background, 0 for white
black_white = [BLACK, WHITE]


class g(Scene):

    CONFIG = {
        "camera_config": {"background_color": black_white[1 - mode]},


    }

    def construct(self):
        t1 = TexMobject(
            "g(x)")
        t1.set_color(BLUE)

        self.play(ShowCreation(t1))
        self.wait(3)


class f(Scene):

    CONFIG = {
        "camera_config": {"background_color": black_white[1 - mode]},


    }

    def construct(self):
        t1 = TexMobject(
            "f(x)")
        t1.set_color(GREEN)

        self.play(ShowCreation(t1))
        self.wait(3)


class convolutionDef(Scene):

    CONFIG = {
        "camera_config": {"background_color": black_white[1 - mode]},


    }

    def construct(self):
        t1 = TexMobject(
            "(f*g)(x)", "=\\int_{-\\infty}^{\\infty}", "f", "(t)", "g", "(x-t){\\rm d}t")
        t1.set_color(black_white[mode])

        t1[0].set_color(RED)

        self.play(ShowCreation(t1))
        self.wait(1)


class convolutionDis(Scene):

    CONFIG = {
        "camera_config": {"background_color": black_white[1 - mode]},


    }

    def construct(self):
        t1 = TexMobject(
            "f(x)&=\\begin{cases}1, & x=0\\\\4, & x=4\\\\3, & x=5\\\\2, & x=9\\\\0, &\\rm{otherwise}\\end{cases}\\\\g(x)&=\\begin{cases}-0.1x+1, & 0 < x < 1\\\\0, &\\rm{otherwise}\\end{cases}")
        t1.set_color(BLACK)

        self.play(ShowCreation(t1))
        self.wait(1)
