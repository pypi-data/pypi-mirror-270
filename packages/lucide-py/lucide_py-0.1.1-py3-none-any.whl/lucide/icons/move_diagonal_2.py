from .. import IconBase


class IconMoveDiagonal2(IconBase):
    class_name = "lucide lucide-move-diagonal-2"
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
                "points": "5 11 5 5 11 5"
            }
        },
        {
            "polyline": {
                "points": "19 13 19 19 13 19"
            }
        },
        {
            "line": {
                "x1": "5",
                "x2": "19",
                "y1": "5",
                "y2": "19"
            }
        }
    ]
}
