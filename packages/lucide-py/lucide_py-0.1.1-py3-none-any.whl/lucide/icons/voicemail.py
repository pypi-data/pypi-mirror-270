from .. import IconBase


class IconVoicemail(IconBase):
    class_name = "lucide lucide-voicemail"
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
                "cx": "6",
                "cy": "12",
                "r": "4"
            }
        },
        {
            "circle": {
                "cx": "18",
                "cy": "12",
                "r": "4"
            }
        },
        {
            "line": {
                "x1": "6",
                "x2": "18",
                "y1": "16",
                "y2": "16"
            }
        }
    ]
}
