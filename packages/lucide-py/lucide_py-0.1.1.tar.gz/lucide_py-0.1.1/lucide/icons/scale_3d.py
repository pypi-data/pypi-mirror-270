from .. import IconBase


class IconScale3D(IconBase):
    class_name = "lucide lucide-scale-3d"
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
                "cx": "19",
                "cy": "19",
                "r": "2"
            }
        },
        {
            "circle": {
                "cx": "5",
                "cy": "5",
                "r": "2"
            }
        },
        {
            "path": {
                "d": "M5 7v12h12"
            }
        },
        {
            "path": {
                "d": "m5 19 6-6"
            }
        }
    ]
}
