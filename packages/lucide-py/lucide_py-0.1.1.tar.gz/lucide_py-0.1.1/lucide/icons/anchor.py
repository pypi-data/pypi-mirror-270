from .. import IconBase


class IconAnchor(IconBase):
    class_name = "lucide lucide-anchor"
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
            "path": {
                "d": "M12 22V8"
            }
        },
        {
            "path": {
                "d": "M5 12H2a10 10 0 0 0 20 0h-3"
            }
        },
        {
            "circle": {
                "cx": "12",
                "cy": "5",
                "r": "3"
            }
        }
    ]
}
