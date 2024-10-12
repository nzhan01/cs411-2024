
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Dictionary of flood stages and their corresponding AR model URLs
flood_stages = {
    "action_stage": "assets/action_stage.glb",
    "minor_flood_stage": "assets/minor_flood_stage.glb",
    "moderate_flood_stage": "assets/moderate_flood_stage.glb",
    "major_flood_stage": "assets/major_flood_stage.glb",
    "record_flood_stage": "assets/record_flood_stage.glb"
}

@app.get("/flood_simulation/{stage}")
async def get_flood_simulation(stage: str):
    if stage in flood_stages:
        return {"model_url": flood_stages[stage]}
    else:
        return JSONResponse(status_code=404, content={"message": "Flood stage not found"})
