from .. import IconBase


class IconTorus(IconBase):
    class_name = "lucide lucide-torus"
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
            "ellipse": {
                "cx": "12",
                "cy": "11",
                "rx": "3",
                "ry": "2"
            }
        },
        {
            "ellipse": {
                "cx": "12",
                "cy": "12.5",
                "rx": "10",
                "ry": "8.5"
            }
        }
    ]
}
