import json
from typing import Dict, Any, List, Optional

class GuiScreenSomCoordinateMapperClient:
    """
    Production-grade Set-of-Marks (SoM) coordinate resolution and bounding box mapper.
    Translates normalized vision model coordinates [0, 1000] into exact physical screen pixels,
    calculates element click centroids, and handles multi-DPI viewport scale factors.
    """
    def __init__(self, viewport_width: int = 1920, viewport_height: int = 1080, dpi_scale: float = 1.25):
        self.vw = viewport_width
        self.vh = viewport_height
        self.dpi = dpi_scale

    def map_som_coordinates(
        self,
        element_id: str = "elem_btn_checkout_01",
        normalized_bbox: Optional[List[int]] = None
    ) -> Dict[str, Any]:
        # Bounding box in standard [ymin, xmin, ymax, xmax] normalized to 1000x1000
        if not normalized_bbox:
            normalized_bbox = [450, 620, 490, 780]

        ymin, xmin, ymax, xmax = normalized_bbox

        # Physical pixel coordinates
        phys_x1 = round((xmin / 1000.0) * self.vw * self.dpi)
        phys_y1 = round((ymin / 1000.0) * self.vh * self.dpi)
        phys_x2 = round((xmax / 1000.0) * self.vw * self.dpi)
        phys_y2 = round((ymax / 1000.0) * self.vh * self.dpi)

        # Centroid calculation for click target
        centroid_x = round((phys_x1 + phys_x2) / 2.0)
        centroid_y = round((phys_y1 + phys_y2) / 2.0)
        elem_width = phys_x2 - phys_x1
        elem_height = phys_y2 - phys_y1

        is_targetable = elem_width >= 10 and elem_height >= 10

        return {
            "mapping_id": "som_map_9901",
            "element_id": element_id,
            "viewport_resolution": f"{self.vw}x{self.vh} (DPI {self.dpi}x)",
            "normalized_input_bbox": normalized_bbox,
            "physical_bounding_box": {"x1": phys_x1, "y1": phys_y1, "x2": phys_x2, "y2": phys_y2},
            "target_click_centroid": {"x": centroid_x, "y": centroid_y},
            "element_dimensions_px": {"width": elem_width, "height": elem_height},
            "is_reliably_targetable": is_targetable,
            "os_input_action_string": f"mouse_click(x={centroid_x}, y={centroid_y})",
            "status": "COORDINATE_GROUNDED_SUCCESSFULLY"
        }
