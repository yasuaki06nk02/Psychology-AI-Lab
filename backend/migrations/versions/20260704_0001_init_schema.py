"""init schema

Revision ID: 20260704_0001
Revises: 
Create Date: 2026-07-04 00:00:00

"""

from alembic import op
import sqlalchemy as sa


revision = "20260704_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "providers",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("display_name", sa.String(length=100), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "datasets",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("dataset_name", sa.String(length=150), nullable=False),
        sa.Column("version", sa.String(length=50), nullable=False),
        sa.Column("question_count", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "experiments",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "models",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("provider_id", sa.String(length=36), nullable=False),
        sa.Column("model_name", sa.String(length=150), nullable=False),
        sa.Column("version", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["provider_id"], ["providers.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "benchmarks",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column("dataset_id", sa.String(length=36), nullable=False),
        sa.Column("benchmark_version", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["dataset_id"], ["datasets.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "benchmark_results",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("benchmark_id", sa.String(length=36), nullable=False),
        sa.Column("model_id", sa.String(length=36), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["benchmark_id"], ["benchmarks.id"]),
        sa.ForeignKeyConstraint(["model_id"], ["models.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("benchmark_results")
    op.drop_table("benchmarks")
    op.drop_table("models")
    op.drop_table("experiments")
    op.drop_table("datasets")
    op.drop_table("providers")
