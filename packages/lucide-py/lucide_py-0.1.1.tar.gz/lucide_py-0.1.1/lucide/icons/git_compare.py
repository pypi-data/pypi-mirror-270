from .. import IconBase


class IconGitCompare(IconBase):
    class_name = "lucide lucide-git-compare"
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
                "cx": "18",
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
            "path": {
                "d": "M13 6h3a2 2 0 0 1 2 2v7"
            }
        },
        {
            "path": {
                "d": "M11 18H8a2 2 0 0 1-2-2V9"
            }
        }
    ]
}
