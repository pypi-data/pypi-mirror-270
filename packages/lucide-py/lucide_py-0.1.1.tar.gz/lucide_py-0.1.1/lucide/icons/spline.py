from .. import IconBase


class IconSpline(IconBase):
    class_name = "lucide lucide-spline"
    svg_data = {
    "attrs": {
        "width": "24",
        "height": "24",
        "view_box": "0 0 24 24",
        "fill": "none",
        "stroke": "currentColor",
        "stroke_width": "2",
        "stroke_linecap": "round",
        "stroke_linejoin": "round"
    },
    "items": [
        {
            "circle": {
                "cx": "19",
                "cy": "5",
                "r": "2"
            }
        },
        {
            "circle": {
                "cx": "5",
                "cy": "19",
                "r": "2"
            }
        },
        {
            "path": {
                "d": "M5 17A12 12 0 0 1 17 5"
            }
        }
    ]
}
