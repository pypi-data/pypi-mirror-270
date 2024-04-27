from .. import IconBase


class IconDock(IconBase):
    class_name = "lucide lucide-dock"
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
                "d": "M2 8h20"
            }
        },
        {
            "rect": {
                "width": "20",
                "height": "16",
                "x": "2",
                "y": "4",
                "rx": "2"
            }
        },
        {
            "path": {
                "d": "M6 16h12"
            }
        }
    ]
}
