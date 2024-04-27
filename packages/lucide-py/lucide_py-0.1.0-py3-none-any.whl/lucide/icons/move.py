from .. import IconBase


class IconMove(IconBase):
    class_name = "lucide lucide-move"
    svg_data = {
    "attrs": {
        "width": "24",
        "height": "24",
        "viewBox": "0 0 24 24",
        "fill": "none",
        "stroke": "currentColor",
        "stroke_width": "2",
        "stroke_linecap": "round",
        "stroke_linejoin": "round"
    },
    "items": [
        {
            "polyline": {
                "points": "5 9 2 12 5 15"
            }
        },
        {
            "polyline": {
                "points": "9 5 12 2 15 5"
            }
        },
        {
            "polyline": {
                "points": "15 19 12 22 9 19"
            }
        },
        {
            "polyline": {
                "points": "19 9 22 12 19 15"
            }
        },
        {
            "line": {
                "x1": "2",
                "x2": "22",
                "y1": "12",
                "y2": "12"
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
