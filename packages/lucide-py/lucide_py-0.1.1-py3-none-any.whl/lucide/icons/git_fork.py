from .. import IconBase


class IconGitFork(IconBase):
    class_name = "lucide lucide-git-fork"
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
                "cy": "18",
                "r": "3"
            }
        },
        {
            "circle": {
                "cx": "6",
                "cy": "6",
                "r": "3"
            }
        },
        {
            "circle": {
                "cx": "18",
                "cy": "6",
                "r": "3"
            }
        },
        {
            "path": {
                "d": "M18 9v2c0 .6-.4 1-1 1H7c-.6 0-1-.4-1-1V9"
            }
        },
        {
            "path": {
                "d": "M12 12v3"
            }
        }
    ]
}
