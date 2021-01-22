# use manim -c 'GREEN' -pl axis.py to change background color
# new version of graph_scene.py file required for manim
from manimlib.imports import *

mode = 0  # 1 for black background, 0 for white
black_white = [BLACK, WHITE]


class CandleAxes(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_min": -1,
        "x_max": 11,
        "y_min": 0,
        "y_max": 1.2,
        "graph_origin": 3 * DOWN + 4 * LEFT,

        "x_tick_frequency": 10,
        "x_leftmost_tick": 0,
        # "x_axis_width": 8,

        "x_labeled_nums": [0, 2, 4, 6, 8, 10],
        # "x_labeled_nums": [-2, 0, 2, 3, 7, 10],
        "x_axis_label": "$x$ ",
        # "x_axis_label": "$t$ (min)",


        "y_labeled_nums": [1],
        "y_axis_label": "$g$",
        # "y_axis_label": "$m$ (la)",
        "exclude_zero_label": False,

        # to switch background
        "axes_color": black_white[mode],
        "label_color": black_white[mode],
        "label_nums_color": black_white[mode],
        "camera_config": {"background_color": black_white[1-mode]},
    }

    def candle(self, t):
        if t <= 0:
            return 1
        elif t <= 10:
            return 1 - (0.1 * t)
        else:
            return 0

    def construct(self):
        self.setup_axes(animate=True)
        candle_curve = self.get_graph(self.candle, BLUE, x_min=-2, x_max=12)
        self.play(ShowCreation(candle_curve))
        self.wait(1)


class LightenAxis(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 11,
        "y_min": 0,
        "y_max": 5.5,
        "graph_origin": 3 * DOWN + 4 * LEFT,

        "x_tick_frequency": 10,
        "y_tick_frequency": 100,
        "x_leftmost_tick": 0,

        "x_labeled_nums": [0, 4, 5, 9, 10],
        "x_axis_label": "$x$ ",
        # "x_axis_label": "$t$ (min)",

        "y_labeled_nums": [1, 2, 3, 4, 5],
        "y_axis_label": "$f$",
        # "y_axis_label": "$\#$candle",
        "exclude_zero_label": False,

        # to switch background
        "axes_color": black_white[mode],
        "label_color": black_white[mode],
        "label_nums_color": black_white[mode],
        "camera_config": {"background_color": black_white[1-mode]},
    }

    def _draw(self, _shape, local_x, local_y):
        _shape.move_arc_center_to([self.coords_to_point(local_x, local_y)[
                                   0], self.coords_to_point(local_x, local_y)[1], 0])
        return ShowCreation(_shape)

    def drawCircle(self, local_x, local_y):
        _circle = Circle(
            color=GREEN,
            # fill_color=WHITE,
            fill_color=black_white[1-mode],
            fill_opacity=1.0,
            radius=0.15,
        )
        return self._draw(_circle, local_x, local_y)

    def drawDot(self, local_x, local_y):
        _dot = g2 = Dot(
            color=GREEN,
            radius=0.15,
        )
        return self._draw(_dot, local_x, local_y)

    def zero(self, t):
        return 0

    def construct(self):
        self.setup_axes(animate=True)
        lighten_nb = self.get_graph(self.zero, GREEN, x_min=-2, x_max=12)
        self.play(ShowCreation(lighten_nb),
                  self.drawCircle(0, 0), self.drawDot(0, 1),
                  self.drawCircle(4, 0), self.drawDot(4, 4),
                  #   self.drawCircle(5, 0), self.drawDot(5, 3),
                  self.drawCircle(5, 0), self.drawDot(5, 5),
                  self.drawCircle(9, 0), self.drawDot(9, 2),
                  )

        self.wait(1)

        # curcurCircle1 = Circle(
        #     color=BLUE,
        #     radius=0.2,
        # )
        # curcurCircle1_4 = Circle(
        #     color=TEAL,
        #     radius=0.2,
        # )
        # curcurCircle4 = Circle(
        #     color=TEAL,
        #     radius=0.2,
        # )
        # self.play(ShowCreation(
        #     curcurCircle1.move_arc_center_to(self.coords_to_point(0, 1))))
        # self.play(ReplacementTransform(
        #     curcurCircle1,
        #     curcurCircle1_4.move_arc_center_to(self.coords_to_point(4, 0))))
        # self.play(ReplacementTransform(
        #     curcurCircle1_4,
        #     curcurCircle4.move_arc_center_to(self.coords_to_point(4, 4))))

        # curcurCircle1 = Circle(
        #     color=BLUE,
        #     radius=0.2,
        # )
        # curcurCircle1_3 = Circle(
        #     color=ORANGE,
        #     radius=0.2,
        # )
        # curcurCircle3 = Circle(
        #     color=ORANGE,
        #     radius=0.2,
        # )
        # self.play(ShowCreation(
        #     curcurCircle1.move_arc_center_to(self.coords_to_point(0, 1))))
        # self.play(ReplacementTransform(
        #     curcurCircle1,
        #     curcurCircle1_3.move_arc_center_to(self.coords_to_point(5, 0))))
        # self.play(ReplacementTransform(
        #     curcurCircle1_3,
        #     curcurCircle3.move_arc_center_to(self.coords_to_point(5, 3))))

        # curcurCircle1 = Circle(
        #     color=BLUE,
        #     radius=0.2,
        # )
        # curcurCircle1_2 = Circle(
        #     color=PURPLE,
        #     radius=0.2,
        # )
        # curcurCircle2 = Circle(
        #     color=PURPLE,
        #     radius=0.2,
        # )
        # self.play(ShowCreation(
        #     curcurCircle1.move_arc_center_to(self.coords_to_point(0, 1))))
        # self.play(ReplacementTransform(
        #     curcurCircle1,
        #     curcurCircle1_2.move_arc_center_to(self.coords_to_point(9, 0))))
        # self.play(ReplacementTransform(
        #     curcurCircle1_2,
        #     curcurCircle2.move_arc_center_to(self.coords_to_point(9, 2))))

        # curcurCircle1 = Circle(
        #     color=BLUE,
        #     radius=0.2,
        # )
        # self.play(ShowCreation(
        #     curcurCircle1.move_arc_center_to(self.coords_to_point(0, 1))))

        # self.wait(1)

        # self.play(FadeOut(curcurCircle1), FadeOut(curcurCircle2),
        #           FadeOut(curcurCircle3), FadeOut(curcurCircle4))
        # self.wait(1)


class MultipleCandleSerial(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 11,
        "y_min": 0,
        "y_max": 12,
        "graph_origin": 3 * DOWN + 4 * LEFT,

        "x_tick_frequency": 10,
        "y_tick_frequency": 10,
        "x_leftmost_tick": 0,

        "x_labeled_nums": [0, 2, 4, 6, 8, 10],
        "x_axis_label": "$t$ (min)",

        "y_labeled_nums": [1, 2, 10],
        "y_axis_label": "$m$ (la)",
        "exclude_zero_label": False,

        # to switch background
        "axes_color": black_white[mode],
        "label_color": black_white[mode],
        "label_nums_color": black_white[mode],
        "camera_config": {"background_color": black_white[1-mode]},
    }

    def candle1(self, t):
        return CandleAxes.candle(self, t)

    def candle2(self, t):
        return 2 * CandleAxes.candle(self, t)

    def candle10(self, t):
        return 10 * CandleAxes.candle(self, t)

    def construct(self):
        self.setup_axes(animate=True)
        self.play(ShowPassingFlash(self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=12)),
        )

        self.play(ShowPassingFlash(self.get_graph(
            self.candle2, PURPLE, x_min=-2, x_max=12)),
        )

        self.play(ShowPassingFlash(self.get_graph(
            self.candle10, RED, x_min=-2, x_max=12)),
        )

        self.play(AnimationGroup(
            ShowCreation(self.get_graph(
                self.candle1, BLUE, x_min=-2, x_max=11.5)),
            ShowCreation(self.get_graph(
                self.candle2, PURPLE, x_min=-2, x_max=12)),
            ShowCreation(self.get_graph(
                self.candle10, RED, x_min=-2, x_max=12.5)),

            lag_ratio=0.4))

        self.wait(1)


class MultipleCandleParallel(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 20,
        "y_min": 0,
        "y_max": 12,
        "graph_origin": 3 * DOWN + 4 * LEFT,

        "x_tick_frequency": 19,
        "y_tick_frequency": 10,
        "x_leftmost_tick": 0,

        "x_labeled_nums": [0, 4, 5, 9, 10, 14, 15, 19],
        "x_axis_label": "$t$ (min)",

        "y_labeled_nums": [1, 2, 3, 4, 10],
        "y_axis_label": "$m$ (la)",
        "exclude_zero_label": False,

        # to switch background
        "axes_color": black_white[mode],
        "label_color": black_white[mode],
        "label_nums_color": black_white[mode],
        "camera_config": {"background_color": black_white[1-mode]},
    }

    def candle1(self, t):
        return 1 * CandleAxes.candle(self, t)

    def candle1_4(self, t):
        return CandleAxes.candle(self, t - 4)

    def candle4(self, t):
        return 4 * CandleAxes.candle(self, t - 4)

    def candle3(self, t):
        return 3 * CandleAxes.candle(self, t - 5)

    def candle1_3(self, t):
        return CandleAxes.candle(self, t - 5)

    def candle2(self, t):
        return 2 * CandleAxes.candle(self, t - 9)

    def candle1_2(self, t):
        return CandleAxes.candle(self, t - 9)

    def candle_sum(self, t):
        return self.candle1(t) + \
            self.candle2(t) + \
            self.candle3(t) + \
            self.candle4(t)

    def construct(self):
        self.setup_axes(animate=True)

        self.wait(1)

        C1 = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        C2 = self.get_graph(
            self.candle2, PURPLE, x_min=-2, x_max=21)

        C3 = self.get_graph(
            self.candle3, ORANGE, x_min=-2, x_max=21)

        C4 = self.get_graph(
            self.candle4, TEAL, x_min=-2, x_max=21)

        C1_2 = self.get_graph(
            self.candle1_2, PURPLE, x_min=-2, x_max=21)

        C1_3 = self.get_graph(
            self.candle1_3, ORANGE, x_min=-2, x_max=21)

        C1_4 = self.get_graph(
            self.candle1_4, TEAL, x_min=-2, x_max=21)

        C = self.get_graph(
            self.candle_sum, RED, x_min=-2, x_max=21)

        self.play(ShowCreation(C1))
        self.play(ReplacementTransform(C1, C1_4))
        self.play(ReplacementTransform(C1_4, C4))
        # self.play(FadeOut(C4))

        C1 = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        self.play(ShowCreation(C1))
        self.play(ReplacementTransform(C1, C1_3))
        self.play(ReplacementTransform(C1_3, C3))
        # self.play(FadeOut(C3))

        C1 = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        self.play(ShowCreation(C1))
        self.play(ReplacementTransform(C1, C1_2))
        self.play(ReplacementTransform(C1_2, C2))
        # self.play(FadeOut(C2))

        C1 = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        self.play(ShowCreation(C1))

        self.wait(1)

        self.play(
            ReplacementTransform(C1, C),
            ReplacementTransform(C2, C),
            ReplacementTransform(C3, C),
            ReplacementTransform(C4, C)
        )

        self.wait(1)


class LightenOnlyXAxis(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 11,
        "y_min": 0.3,
        "y_max": 0.5,
        "graph_origin": 3 * DOWN + 4 * LEFT,

        "x_tick_frequency": 10,
        "x_leftmost_tick": 0,

        "x_labeled_nums": [0, 4, 5, 9, 10],
        "x_axis_label": "$t$ (min)",

        "y_axis_label": "",
        "exclude_zero_label": False,

        # to switch background
        "axes_color": black_white[mode],
        "label_color": black_white[mode],
        "label_nums_color": black_white[mode],
        "camera_config": {"background_color": black_white[1-mode]},
    }

    def construct(self):
        self.setup_axes(animate=True)
        self.wait(1)


class fAndGConvolution(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 20,
        "y_min": 0,
        "y_max": 12,
        "graph_origin": 3 * DOWN + 4 * LEFT,

        "x_tick_frequency": 19,
        "y_tick_frequency": 10,
        "x_leftmost_tick": 0,

        "x_labeled_nums": [0, 4, 5, 9, 10, 14, 15, 19],
        "x_axis_label": "$x$",

        "y_labeled_nums": [1, 2, 3, 4, 10],
        "y_axis_label": "$y$",
        "exclude_zero_label": False,

        # to switch background
        "axes_color": black_white[mode],
        "label_color": black_white[mode],
        "label_nums_color": black_white[mode],
        "camera_config": {"background_color": black_white[1-mode]},
    }

    def _draw(self, _shape, local_x, local_y):
        _shape.move_arc_center_to([self.coords_to_point(local_x, local_y)[
                                   0], self.coords_to_point(local_x, local_y)[1], 0])
        return ShowCreation(_shape)

    def drawCircle(self, local_x, local_y):
        _circle = Circle(
            color=GREEN,
            # fill_color=WHITE,
            fill_color=black_white[1-mode],
            fill_opacity=1.0,
            radius=0.15,
        )
        return self._draw(_circle, local_x, local_y)

    def drawDot(self, local_x, local_y):
        _dot = g2 = Dot(
            color=GREEN,
            radius=0.15,
        )
        return self._draw(_dot, local_x, local_y)

    def zero(self, t):
        return 0

    def candle1(self, t):
        return 1 * CandleAxes.candle(self, t)

    def candle1_4(self, t):
        return CandleAxes.candle(self, t - 4)

    def candle4(self, t):
        return 4 * CandleAxes.candle(self, t - 4)

    def candle3(self, t):
        return 3 * CandleAxes.candle(self, t - 5)

    def candle1_3(self, t):
        return CandleAxes.candle(self, t - 5)

    def candle2(self, t):
        return 2 * CandleAxes.candle(self, t - 9)

    def candle1_2(self, t):
        return CandleAxes.candle(self, t - 9)

    def candle_sum(self, t):
        return self.candle1(t) + \
            self.candle2(t) + \
            self.candle3(t) + \
            self.candle4(t)

    def construct(self):
        self.setup_axes(animate=True)

        self.wait(1)

        lighten_nb = self.get_graph(self.zero, GREEN, x_min=-2, x_max=21)

        C1 = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        C1b = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        C1c = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        C1d = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        C2 = self.get_graph(
            self.candle2, PURPLE, x_min=-2, x_max=21)

        C3 = self.get_graph(
            self.candle3, ORANGE, x_min=-2, x_max=21)

        C4 = self.get_graph(
            self.candle4, TEAL, x_min=-2, x_max=21)

        C1_2 = self.get_graph(
            self.candle1_2, PURPLE, x_min=-2, x_max=21)

        C1_3 = self.get_graph(
            self.candle1_3, ORANGE, x_min=-2, x_max=21)

        C1_4 = self.get_graph(
            self.candle1_4, TEAL, x_min=-2, x_max=21)

        C = self.get_graph(
            self.candle_sum, RED, x_min=-2, x_max=21)

        self.play(ShowCreation(lighten_nb),
                  self.drawCircle(0, 0), self.drawDot(0, 1),
                  self.drawCircle(4, 0), self.drawDot(4, 4),
                  self.drawCircle(5, 0), self.drawDot(5, 3),
                  self.drawCircle(9, 0), self.drawDot(9, 2),
                  ShowCreation(C1)
                  )

        self.wait(1)

        curcurCircle1 = Circle(
            color=BLUE,
            radius=0.2,
        )
        curcurCircle1_4 = Circle(
            color=TEAL,
            radius=0.2,
        )
        curcurCircle4 = Circle(
            color=TEAL,
            radius=0.2,
        )

        self.play(
            ShowCreation(curcurCircle1.move_arc_center_to(self.coords_to_point(0, 1))))

        self.play(ReplacementTransform(C1, C1_4),
                  ReplacementTransform(curcurCircle1,
                                       curcurCircle1_4.move_arc_center_to(self.coords_to_point(4, 1))))

        self.play(ReplacementTransform(C1_4, C4),
                  ReplacementTransform(curcurCircle1_4,
                                       curcurCircle4.move_arc_center_to(self.coords_to_point(4, 4))))
        # self.play(FadeOut(C4))

        curcurCircle1 = Circle(
            color=BLUE,
            radius=0.2,
        )
        curcurCircle1_3 = Circle(
            color=ORANGE,
            radius=0.2,
        )
        curcurCircle3 = Circle(
            color=ORANGE,
            radius=0.2,
        )

        self.play(ShowCreation(C1b),
                  ShowCreation(curcurCircle1.move_arc_center_to(
                      self.coords_to_point(0, 1))))
        self.play(ReplacementTransform(C1b, C1_3),            ReplacementTransform(
            curcurCircle1,
            curcurCircle1_3.move_arc_center_to(self.coords_to_point(5, 1))))
        self.play(ReplacementTransform(C1_3, C3), ReplacementTransform(
            curcurCircle1_3,
            curcurCircle3.move_arc_center_to(self.coords_to_point(5, 3)))
        )

        curcurCircle1 = Circle(
            color=BLUE,
            radius=0.2,
        )

        curcurCircle1_2 = Circle(
            color=PURPLE,
            radius=0.2,
        )

        curcurCircle2 = Circle(
            color=PURPLE,
            radius=0.2,
        )

        self.play(ShowCreation(C1c), ShowCreation(
            curcurCircle1.move_arc_center_to(self.coords_to_point(0, 1))))
        self.play(ReplacementTransform(C1c, C1_2), ReplacementTransform(
            curcurCircle1,
            curcurCircle1_2.move_arc_center_to(self.coords_to_point(9, 1))))
        self.play(ReplacementTransform(C1_2, C2), ReplacementTransform(
            curcurCircle1_2,
            curcurCircle2.move_arc_center_to(self.coords_to_point(9, 2))))
        # self.play(FadeOut(C2))

        curcurCircle1 = Circle(
            color=BLUE,
            radius=0.2,
        )

        self.play(ShowCreation(C1d),
                  ShowCreation(
            curcurCircle1.move_arc_center_to(self.coords_to_point(0, 1))))

        self.wait(1)

        self.play(
            ReplacementTransform(C1d, C),
            ReplacementTransform(C2, C),
            ReplacementTransform(C3, C),
            ReplacementTransform(C4, C),
            FadeOut(curcurCircle1),
            FadeOut(curcurCircle2),
            FadeOut(curcurCircle3),
            FadeOut(curcurCircle4),
        )

        self.wait(1)


class fAndGConvolution_syn(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 20,
        "y_min": 0,
        "y_max": 12,
        "graph_origin": 3 * DOWN + 4 * LEFT,

        "x_tick_frequency": 19,
        "y_tick_frequency": 10,
        "x_leftmost_tick": 0,

        "x_labeled_nums": [0, 4, 5, 9, 10, 14, 15, 19],
        "x_axis_label": "$x$",

        "y_labeled_nums": [1, 2, 3, 4, 10],
        "y_axis_label": "$y$",
        "exclude_zero_label": False,

        # to switch background
        "axes_color": black_white[mode],
        "label_color": black_white[mode],
        "label_nums_color": black_white[mode],
        "camera_config": {"background_color": black_white[1-mode]},
    }

    def _draw(self, _shape, local_x, local_y):
        _shape.move_arc_center_to([self.coords_to_point(local_x, local_y)[
                                   0], self.coords_to_point(local_x, local_y)[1], 0])
        return ShowCreation(_shape)

    def drawCircle(self, local_x, local_y):
        _circle = Circle(
            color=GREEN,
            # fill_color=WHITE,
            fill_color=black_white[1-mode],
            fill_opacity=1.0,
            radius=0.15,
        )
        return self._draw(_circle, local_x, local_y)

    def drawDot(self, local_x, local_y):
        _dot = g2 = Dot(
            color=GREEN,
            radius=0.15,
        )
        return self._draw(_dot, local_x, local_y)

    def zero(self, t):
        return 0

    def candle1(self, t):
        return 1 * CandleAxes.candle(self, t)

    def candle1_4(self, t):
        return CandleAxes.candle(self, t - 4)

    def candle4(self, t):
        return 4 * CandleAxes.candle(self, t - 4)

    def candle3(self, t):
        return 3 * CandleAxes.candle(self, t - 5)

    def candle1_3(self, t):
        return CandleAxes.candle(self, t - 5)

    def candle2(self, t):
        return 2 * CandleAxes.candle(self, t - 9)

    def candle1_2(self, t):
        return CandleAxes.candle(self, t - 9)

    def candle_sum(self, t):
        return self.candle1(t) + \
            self.candle2(t) + \
            self.candle3(t) + \
            self.candle4(t)

    def construct(self):
        self.setup_axes(animate=True)

        self.wait(1)

        lighten_nb = self.get_graph(self.zero, GREEN, x_min=-2, x_max=21)

        C1 = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        C1b = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        C1c = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        C1d = self.get_graph(
            self.candle1, BLUE, x_min=-2, x_max=21)

        C2 = self.get_graph(
            self.candle2, PURPLE, x_min=-2, x_max=21)

        C3 = self.get_graph(
            self.candle3, ORANGE, x_min=-2, x_max=21)

        C4 = self.get_graph(
            self.candle4, TEAL, x_min=-2, x_max=21)

        C1_2 = self.get_graph(
            self.candle1_2, PURPLE, x_min=-2, x_max=21)

        C1_3 = self.get_graph(
            self.candle1_3, ORANGE, x_min=-2, x_max=21)

        C1_4 = self.get_graph(
            self.candle1_4, TEAL, x_min=-2, x_max=21)

        C = self.get_graph(
            self.candle_sum, RED, x_min=-2, x_max=21)

        curcurCircle1b = Circle(
            color=BLUE,
            radius=0.2,
        )
        curcurCircle1_4 = Circle(
            color=TEAL,
            radius=0.2,
        )
        curcurCircle4 = Circle(
            color=TEAL,
            radius=0.2,
        )

        curcurCircle1c = Circle(
            color=BLUE,
            radius=0.2,
        )
        curcurCircle1_3 = Circle(
            color=ORANGE,
            radius=0.2,
        )
        curcurCircle3 = Circle(
            color=ORANGE,
            radius=0.2,
        )

        curcurCircle1d = Circle(
            color=BLUE,
            radius=0.2,
        )

        curcurCircle1_2 = Circle(
            color=PURPLE,
            radius=0.2,
        )

        curcurCircle2 = Circle(
            color=PURPLE,
            radius=0.2,
        )

        curcurCircle1a = Circle(
            color=BLUE,
            radius=0.2,
        )

        self.play(ShowCreation(lighten_nb),
                  ShowCreation(C1b),
                  ShowCreation(C1c),
                  ShowCreation(C1d),
                  self.drawCircle(0, 0), self.drawDot(0, 1),
                  self.drawCircle(4, 0), self.drawDot(4, 4),
                  self.drawCircle(5, 0), self.drawDot(5, 3),
                  self.drawCircle(9, 0), self.drawDot(9, 2),
                  ShowCreation(C1)
                  )

        self.wait(1)

        self.play(
            ShowCreation(curcurCircle1b.move_arc_center_to(
                self.coords_to_point(0, 1))),
            ShowCreation(curcurCircle1c.move_arc_center_to(
                self.coords_to_point(0, 1))),
            ShowCreation(curcurCircle1d.move_arc_center_to(
                self.coords_to_point(0, 1))),
            ShowCreation(curcurCircle1a.move_arc_center_to(
                self.coords_to_point(0, 1))))

        self.play(ReplacementTransform(C1, C1_4),
                  ReplacementTransform(curcurCircle1b,
                                       curcurCircle1_4.move_arc_center_to(self.coords_to_point(4, 1))),
                  ReplacementTransform(C1b, C1_3),
                  ReplacementTransform(curcurCircle1c,
                                       curcurCircle1_3.move_arc_center_to(self.coords_to_point(5, 1))),
                  ReplacementTransform(C1c, C1_2),
                  ReplacementTransform(curcurCircle1d,
                                       curcurCircle1_2.move_arc_center_to(self.coords_to_point(9, 1))))

        self.play(ReplacementTransform(C1_4, C4),
                  ReplacementTransform(curcurCircle1_4,
                                       curcurCircle4.move_arc_center_to(self.coords_to_point(4, 4))),
                  ReplacementTransform(C1_3, C3),
                  ReplacementTransform(curcurCircle1_3,
                                       curcurCircle3.move_arc_center_to(self.coords_to_point(5, 3))),
                  ReplacementTransform(C1_2, C2),
                  ReplacementTransform(curcurCircle1_2,
                                       curcurCircle2.move_arc_center_to(self.coords_to_point(9, 2))))

        self.play(
            ReplacementTransform(C1d, C),
            ReplacementTransform(C2, C),
            ReplacementTransform(C3, C),
            ReplacementTransform(C4, C),
            FadeOut(curcurCircle1a),
            FadeOut(curcurCircle2),
            FadeOut(curcurCircle3),
            FadeOut(curcurCircle4),
        )

        self.wait(1)


class CandleAxesScaling(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 11,
        "y_min": 0,
        "y_max": 1.2,
        "graph_origin": 3 * DOWN + 4 * LEFT,

        "x_tick_frequency": 5,
        "y_tick_frequency": 0.5,
        "x_leftmost_tick": 0,
        # "x_axis_width": 8,

        # "x_labeled_nums": [0, 2, 4, 6, 8, 10],
        "x_labeled_nums": [0, 5, 10],
        "x_axis_label": "$t$ (min)",

        "y_labeled_nums": [1],
        "y_axis_label": "$m$ (la)",
        "exclude_zero_label": False,

        # to switch background
        "axes_color": black_white[mode],
        "label_color": black_white[mode],
        "label_nums_color": black_white[mode],
        "camera_config": {"background_color": black_white[1-mode]},
    }

    def candle(self, t):
        if t <= 0:
            return 1
        elif t <= 10:
            return 1 - (0.1 * t)
        else:
            return 0

    def candle2(self, t):
        return 1.15 * self.candle(t)

    def candle8(self, t):
        return 0.8 * self.candle(t)

    def candleFake(self, t):
        return .5 * self.candle(t)

    def candleReal(self, t):
        if t <= 0:
            return 0.5
        elif t <= 5:
            return 0.5 - (0.1 * t)
        else:
            return 0

    def construct(self):
        self.setup_axes(animate=True)
        c1 = self.get_graph(self.candle, BLUE, x_min=-2, x_max=12)
        c2 = self.get_graph(self.candle2, BLUE, x_min=-2, x_max=12)
        c8 = self.get_graph(self.candle8, BLUE, x_min=-2, x_max=12)
        self.play(ShowCreation(c1))
        self.wait(1)
        self.play(ReplacementTransform(c1, c2))
        self.play(ReplacementTransform(c2, c8))
        c1 = self.get_graph(self.candle, BLUE, x_min=-2, x_max=12)
        self.play(ReplacementTransform(c8, c1))

        self.wait(1)
        cT = self.get_graph(self.candleReal, GREEN, x_min=-2, x_max=12)
        cF = self.get_graph(self.candleFake, RED, x_min=-2, x_max=12)

        self.play(ShowCreation(cT))
        self.wait(1)
        self.play(ReplacementTransform(cT, cF), ReplacementTransform(c1, cF))
        self.wait(1)
