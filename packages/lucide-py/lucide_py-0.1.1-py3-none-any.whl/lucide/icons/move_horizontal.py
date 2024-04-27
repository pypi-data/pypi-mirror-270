from .. import IconBase


class IconMoveHorizontal(IconBase):
    class_name = "lucide lucide-move-horizontal"
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
                "points": "18 8 22 12 18 16"
            }
        },
        {
            "polyline": {
                "points": "6 8 2 12 6 16"
            }
        },
        {
            "line": {
                "x1": "2",
                "x2": "22",
                "y1": "12",
                "y2": "12"
            }
        }
    ]
}
