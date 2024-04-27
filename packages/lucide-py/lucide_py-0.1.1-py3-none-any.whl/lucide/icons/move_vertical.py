from .. import IconBase


class IconMoveVertical(IconBase):
    class_name = "lucide lucide-move-vertical"
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
            "polyline": {
                "points": "8 18 12 22 16 18"
            }
        },
        {
            "polyline": {
                "points": "8 6 12 2 16 6"
            }
        },
        {
            "line": {
                "x1": "12",
                "x2": "12",
                "y1": "2",
                "y2": "22"
            }
        }
    ]
}
