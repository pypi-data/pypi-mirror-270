from .. import IconBase


class IconPi(IconBase):
    class_name = "lucide lucide-pi"
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
            "line": {
                "x1": "9",
                "x2": "9",
                "y1": "4",
                "y2": "20"
            }
        },
        {
            "path": {
                "d": "M4 7c0-1.7 1.3-3 3-3h13"
            }
        },
        {
            "path": {
                "d": "M18 20c-1.7 0-3-1.3-3-3V4"
            }
        }
    ]
}
