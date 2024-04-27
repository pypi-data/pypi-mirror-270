from .. import IconBase


class IconUnderline(IconBase):
    class_name = "lucide lucide-underline"
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
            "path": {
                "d": "M6 4v6a6 6 0 0 0 12 0V4"
            }
        },
        {
            "line": {
                "x1": "4",
                "x2": "20",
                "y1": "20",
                "y2": "20"
            }
        }
    ]
}
