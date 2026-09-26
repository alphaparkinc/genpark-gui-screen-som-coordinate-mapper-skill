import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import GuiScreenSomCoordinateMapperClient

def main():
    client = GuiScreenSomCoordinateMapperClient()
    res = client.map_som_coordinates()
    print("=== GUI Screen SoM Coordinate Mapper Output ===")
    print(f"Element: {res['element_id']} | Viewport: {res['viewport_resolution']}")
    print(f"Normalized BBox: {res['normalized_input_bbox']}")
    print(f"Physical Target: ({res['target_click_centroid']['x']}, {res['target_click_centroid']['y']}) | Size: {res['element_dimensions_px']['width']}x{res['element_dimensions_px']['height']}px")
    print(f"OS Action Directive: {res['os_input_action_string']}")

if __name__ == '__main__':
    main()
