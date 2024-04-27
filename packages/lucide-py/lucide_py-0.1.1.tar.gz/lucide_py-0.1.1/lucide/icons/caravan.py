from .. import IconBase


class IconCaravan(IconBase):
    class_name = "lucide lucide-caravan"
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
            "rect": {
                "width": "4",
                "height": "4",
                "x": "2",
                "y": "9"
            }
        },
        {
            "rect": {
                "width": "4",
                "height": "10",
                "x": "10",
                "y": "9"
            }
        },
        {
            "path": {
                "d": "M18 19V9a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v8a2 2 0 0 0 2 2h2"
            }
        },
        {
            "circle": {
                "cx": "8",
                "cy": "19",
                "r": "2"
            }
        },
        {
            "path": {
                "d": "M10 19h12v-2"
            }
        }
    ]
}
