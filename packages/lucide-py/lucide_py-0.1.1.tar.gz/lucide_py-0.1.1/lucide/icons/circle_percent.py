from .. import IconBase


class IconCirclePercent(IconBase):
    class_name = "lucide lucide-circle-percent"
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
            "path": {
                "d": "m15 9-6 6"
            }
        },
        {
            "path": {
                "d": "M9 9h.01"
            }
        },
        {
            "path": {
                "d": "M15 15h.01"
            }
        }
    ]
}
