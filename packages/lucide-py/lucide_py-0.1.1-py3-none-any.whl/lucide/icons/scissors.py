from .. import IconBase


class IconScissors(IconBase):
    class_name = "lucide lucide-scissors"
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
                "cx": "6",
                "cy": "6",
                "r": "3"
            }
        },
        {
            "path": {
                "d": "M8.12 8.12 12 12"
            }
        },
        {
            "path": {
                "d": "M20 4 8.12 15.88"
            }
        },
        {
            "circle": {
                "cx": "6",
                "cy": "18",
                "r": "3"
            }
        },
        {
            "path": {
                "d": "M14.8 14.8 20 20"
            }
        }
    ]
}
