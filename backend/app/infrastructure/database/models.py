from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class ProviderModel(Base):
    __tablename__ = "providers"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    display_name: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class AIModelModel(Base):
    __tablename__ = "models"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    provider_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("providers.id"), nullable=False
    )
    model_name: Mapped[str] = mapped_column(String(150), nullable=False)
    version: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class DatasetModel(Base):
    __tablename__ = "datasets"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    dataset_name: Mapped[str] = mapped_column(String(150), nullable=False)
    version: Mapped[str] = mapped_column(String(50), nullable=False)
    question_count: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class BenchmarkModel(Base):
    __tablename__ = "benchmarks"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    dataset_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("datasets.id"), nullable=False
    )
    benchmark_version: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class BenchmarkResultModel(Base):
    __tablename__ = "benchmark_results"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    benchmark_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("benchmarks.id"), nullable=False
    )
    model_id: Mapped[str] = mapped_column(String(36), ForeignKey("models.id"), nullable=False)
    score: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class ExperimentModel(Base):
    __tablename__ = "experiments"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
