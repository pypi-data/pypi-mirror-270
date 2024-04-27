from .. import IconBase


class IconCircuitBoard(IconBase):
    class_name = "lucide lucide-circuit-board"
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
            "rect": {
                "width": "18",
                "height": "18",
                "x": "3",
                "y": "3",
                "rx": "2"
            }
        },
        {
            "path": {
                "d": "M11 9h4a2 2 0 0 0 2-2V3"
            }
        },
        {
            "circle": {
                "cx": "9",
                "cy": "9",
                "r": "2"
            }
        },
        {
            "path": {
                "d": "M7 21v-4a2 2 0 0 1 2-2h4"
            }
        },
        {
            "circle": {
                "cx": "15",
                "cy": "15",
                "r": "2"
            }
        }
    ]
}
