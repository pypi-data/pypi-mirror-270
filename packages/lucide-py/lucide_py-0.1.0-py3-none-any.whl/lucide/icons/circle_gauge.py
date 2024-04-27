from .. import IconBase


class IconCircleGauge(IconBase):
    class_name = "lucide lucide-circle-gauge"
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
                "d": "M15.6 2.7a10 10 0 1 0 5.7 5.7"
            }
        },
        {
            "circle": {
                "cx": "12",
                "cy": "12",
                "r": "2"
            }
        },
        {
            "path": {
                "d": "M13.4 10.6 19 5"
            }
        }
    ]
}
