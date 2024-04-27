from .. import IconBase


class IconLamp(IconBase):
    class_name = "lucide lucide-lamp"
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
                "d": "M8 2h8l4 10H4L8 2Z"
            }
        },
        {
            "path": {
                "d": "M12 12v6"
            }
        },
        {
            "path": {
                "d": "M8 22v-2c0-1.1.9-2 2-2h4a2 2 0 0 1 2 2v2H8Z"
            }
        }
    ]
}
