from .. import IconBase


class IconMoveDiagonal(IconBase):
    class_name = "lucide lucide-move-diagonal"
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
                "points": "13 5 19 5 19 11"
            }
        },
        {
            "polyline": {
                "points": "11 19 5 19 5 13"
            }
        },
        {
            "line": {
                "x1": "19",
                "x2": "5",
                "y1": "5",
                "y2": "19"
            }
        }
    ]
}
