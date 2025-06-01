import asyncio
from pathlib import Path
from autogenstudio.teammanager import TeamManager


async def main():
    project_root = Path(__file__).parent.parent
    team_config_path = project_root / "team.json"
    manager = TeamManager()

    response = await manager.run(
        team_config=str(team_config_path),
        task="Write a short story about cat.",
    )
    print(response)


asyncio.run(main())
