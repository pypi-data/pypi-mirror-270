from .. import IconBase


class IconEclipse(IconBase):
    class_name = "lucide lucide-eclipse"
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
                "d": "M12 2a7 7 0 1 0 10 10"
            }
        }
    ]
}
