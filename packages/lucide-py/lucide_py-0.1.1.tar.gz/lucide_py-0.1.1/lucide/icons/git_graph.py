from .. import IconBase


class IconGitGraph(IconBase):
    class_name = "lucide lucide-git-graph"
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
                "cx": "5",
                "cy": "6",
                "r": "3"
            }
        },
        {
            "path": {
                "d": "M5 9v6"
            }
        },
        {
            "circle": {
                "cx": "5",
                "cy": "18",
                "r": "3"
            }
        },
        {
            "path": {
                "d": "M12 3v18"
            }
        },
        {
            "circle": {
                "cx": "19",
                "cy": "6",
                "r": "3"
            }
        },
        {
            "path": {
                "d": "M16 15.7A9 9 0 0 0 19 9"
            }
        }
    ]
}
