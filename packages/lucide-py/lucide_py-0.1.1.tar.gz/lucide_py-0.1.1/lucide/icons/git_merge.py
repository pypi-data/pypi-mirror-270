from .. import IconBase


class IconGitMerge(IconBase):
    class_name = "lucide lucide-git-merge"
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
                "d": "M6 21V9a9 9 0 0 0 9 9"
            }
        }
    ]
}
