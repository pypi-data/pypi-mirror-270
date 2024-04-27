from .. import IconBase


class IconCylinder(IconBase):
    class_name = "lucide lucide-cylinder"
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
            "ellipse": {
                "cx": "12",
                "cy": "5",
                "rx": "9",
                "ry": "3"
            }
        },
        {
            "path": {
                "d": "M3 5v14a9 3 0 0 0 18 0V5"
            }
        }
    ]
}
