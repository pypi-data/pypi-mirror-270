from .. import IconBase


class IconGlobe(IconBase):
    class_name = "lucide lucide-globe"
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
            "path": {
                "d": "M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"
            }
        },
        {
            "path": {
                "d": "M2 12h20"
            }
        }
    ]
}
