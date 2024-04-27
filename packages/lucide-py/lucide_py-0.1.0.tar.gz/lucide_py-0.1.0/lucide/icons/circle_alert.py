from .. import IconBase


class IconCircleAlert(IconBase):
    class_name = "lucide lucide-circle-alert"
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
            "circle": {
                "cx": "12",
                "cy": "12",
                "r": "10"
            }
        },
        {
            "line": {
                "x1": "12",
                "x2": "12",
                "y1": "8",
                "y2": "12"
            }
        },
        {
            "line": {
                "x1": "12",
                "x2": "12.01",
                "y1": "16",
                "y2": "16"
            }
        }
    ]
}
