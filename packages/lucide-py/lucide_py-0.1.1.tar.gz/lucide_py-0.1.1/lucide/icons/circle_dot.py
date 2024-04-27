from .. import IconBase


class IconCircleDot(IconBase):
    class_name = "lucide lucide-circle-dot"
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
                "cx": "12",
                "cy": "12",
                "r": "10"
            }
        },
        {
            "circle": {
                "cx": "12",
                "cy": "12",
                "r": "1"
            }
        }
    ]
}
