import json, sys
from client import GuiScreenSomCoordinateMapperClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "gui-screen-som-coordinate-mapper", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "map_som_coordinates", "description": "Maps Set-of-Marks normalized coordinates to physical sub-pixel click targets for computer-use agents."}]}}
    elif method == "tools/call":
        client = GuiScreenSomCoordinateMapperClient()
        res = client.map_som_coordinates()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = GuiScreenSomCoordinateMapperClient()
        print(json.dumps(client.map_som_coordinates(), indent=2))
