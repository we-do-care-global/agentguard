"""Typer‑based CLI for ${PKG_NAME}."""
from __future__ import annotations
import typer
import yaml
from pathlib import Path
from .policy = Policy, load_policy
import uvicorn

cli = typer.Typer(add_completion=False, help="${PKG_NAME} CLI")

@cli.command()
def init(
    agent: str = typer.Option(..., help="Agent name, e.g. research-bot"),
    out: Path = typer.Option("policy.yaml", help="Where to write example policy"),
):
    """Create a starter policy.yaml."""
    example = Policy(
        agent=agent,
        allowed_tools=["web_search", "read_file"],
        denied_tools=["send_email", "transfer_funds"],
        limits={"max_usd_per_day": 5.00, "max_tokens_per_call": 4000},
    )
    out.write_text(yaml.dump(example.model_dump(), sort_keys=False))
    typer.secho(f"✅ Example policy written to {out}", fg=typer.colors.GREEN)

@cli.command()
def run(
    policy: Path = typer.Option("policy.yaml", help="Path to policy YAML"),
    host: str = typer.Option("0.0.0.0", help="Host to bind"),
    port: int = typer.Option(8000, help="Port to bind"),
    reload: bool = typer.Option(False, help="Enable uvicorn reload (dev)"),
):
    """Run the ${PKG_NAME} FastAPI server."""
    # Validate policy early
    try:
        load_policy(policy)
    except Exception as e:
        typer.secho(f"❌ Invalid policy: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    typer.secho(f"🚀 Starting ${PKG_NAME} on http://{host}:{port}", fg=typer.colors.BLUE)
    uvicorn.run(
        "${PKG_NAME}.main:app",
        host=host,
        port=port,
        reload=reload,
        env={"${PKG_NAME}_POLICY": str(policy)},
    )

if __name__ == "__main__":
    cli()
